from django.http import JsonResponse, HttpResponse
from .models import Aluno, Acesso, Relatorio
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import csv
import io


@csrf_exempt
def registrar_acesso(request):
    numero_cartao = request.POST.get('numero_cartao')
    try:
        aluno = Aluno.objects.get(numero_cartao=numero_cartao)
        novo_acesso = Acesso.objects.create(
            numero_cartao=aluno.numero_cartao,
            matricula=aluno.matricula,
            nome=aluno.nome,
            data_hora=timezone.now()
        )
        novo_acesso.save()
        return JsonResponse({'status': 'sucesso', 'mensagem': 'Acesso registrado para o aluno ' + aluno.nome})
    except Aluno.DoesNotExist:
        return JsonResponse({'status': 'erro', 'mensagem': 'Aluno não encontrado'})


def visualizar_acessos(request):
    quantidade = Acesso.objects.all().count()
    acessos = Acesso.objects.all().order_by(
        '-data_hora')
    return render(request, 'home.html', {'acessos': acessos, 'quantidade': quantidade})


@csrf_exempt
def gerar_relatorio(request):
    if not request.user.is_authenticated:
        return HttpResponse("Você precisa estar autenticado para gerar relatórios.", status=401)

    # Criar um registro de relatório com o timestamp atual
    relatorio = Relatorio.objects.create(solicitante=request.user)

    # Buscar acessos do dia atual
    today = timezone.now().date()
    acessos = Acesso.objects.filter(
        data_hora__date=today).order_by('-data_hora')

    fieldnames = ['Nome', 'Matrícula',
                  'Número do Cartão', 'Data/Hora do Acesso']
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for acesso in acessos:
        writer.writerow({
            'Nome': acesso.nome,
            'Matrícula': acesso.matricula,
            'Número do Cartão': acesso.numero_cartao,
            'Data/Hora do Acesso': acesso.data_hora.strftime('%d/%m/%Y %H:%M')
        })

    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_acessos_{}.csv"'.format(
        relatorio.timestamp.strftime('%d-%m-%Y_%H-%M'))

    return response
