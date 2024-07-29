from django.http import JsonResponse, HttpResponse
from .models import Aluno, Acesso, Relatorio
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

import csv
import io


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('visualizar_acessos')
            else:
                form.add_error(None, 'Email ou senha inválidos')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@csrf_exempt
def registrar_acesso(request):
    cpf = request.POST.get('cpf')
    try:
        aluno = Aluno.objects.get(cpf=cpf)
        novo_acesso = Acesso.objects.create(
            numero_cartao=aluno.numero_cartao,
            matricula=aluno.matricula,
            nome=aluno.nome,
            data_hora=timezone.now()
        )
        novo_acesso.save()
        return JsonResponse(
            {'status': 'sucesso', 'mensagem': 'Acesso registrado para o aluno ' + aluno.nome})
    except Aluno.DoesNotExist:
        return JsonResponse(
            {'status': 'erro', 'mensagem': 'Aluno não encontrado'})


@login_required
def visualizar_acessos(request):
    quantidade = Acesso.objects.all().count()
    acessos = Acesso.objects.all().order_by(
        '-data_hora')
    return render(
        request, 'home.html', {
            'acessos': acessos, 'quantidade': quantidade})


@csrf_exempt
def gerar_relatorio(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            "Você precisa estar autenticado para gerar relatórios.",
            status=401)

    now_local = timezone.localtime()
    relatorio = Relatorio.objects.create(
        solicitante=request.user, timestamp=now_local)

    today = timezone.localdate()
    acessos = Acesso.objects.filter(
        data_hora__date=today).order_by('-data_hora')

    fieldnames = ['Nome', 'Matrícula',
                  'Número do Cartão', 'Data/Hora do Acesso']
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for acesso in acessos:
        local_datetime = timezone.localtime(acesso.data_hora)
        writer.writerow({
            'Nome': acesso.nome,
            'Matrícula': acesso.matricula,
            'Número do Cartão': acesso.numero_cartao,
            'Data/Hora do Acesso': local_datetime.strftime('%d/%m/%Y %H:%M')
        })

    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_acessos_{}.csv"'.format(
        relatorio.timestamp.strftime('%d-%m-%Y_%H-%M'))

    return response
