from django.http import JsonResponse
from .models import Aluno, Acesso
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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
    acessos = Acesso.objects.all().order_by(
        '-data_hora')
    return render(request, 'home.html', {'acessos': acessos})
