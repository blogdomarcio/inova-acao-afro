from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from sweetify import sweetify

from peoples.forms import PessoaForm
from peoples.models import People


@login_required()
def index(request):
    usuario = User.objects.get(id=request.user.id)
    pessoas = People.objects.all()
    masc = People.objects.filter(sexo='M').count()
    fem = People.objects.filter(sexo='F').count()

    context = {
        'usuario': usuario,
        'pessoas': pessoas,
        'masc': masc,
        'fem': fem,
    }

    return render(request, 'people/dashboard/index.html', context)


@login_required()
def lista(request):

    usuario = User.objects.get(id=request.user.id)

    if request.POST:

        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            sweetify.success(request, 'Registro cadastrado com sucesso!')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    else:

        pessoas = People.objects.all()

        form = PessoaForm()

        context = {
            'usuario': usuario,
            'pessoas': pessoas,
            'form': form
        }

        return render(request, 'people/dashboard/pessoas.html', context)


@login_required()
def detalhe(request, codigo):

    usuario = User.objects.get(id=request.user.id)
    pessoa = People.objects.get(codigo=codigo)

    if request.POST:

        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.data_nasc = request.POST['data_nasc']
        pessoa.celular = request.POST['celular']
        pessoa.rg = request.POST['rg']
        pessoa.pai = request.POST['pai']
        pessoa.mae = request.POST['mae']
        if request.POST['altura']:
            pessoa.altura = request.POST['altura']
        if request.POST['peso']:
            pessoa.peso = request.POST['peso']
        pessoa.tipo_sanguineo = request.POST['tipo_sanguineo']
        pessoa.sexo = request.POST['sexo']
        pessoa.save()

        sweetify.success(request, 'Registro atualizado com sucesso!')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # else:
        #
        #     sweetify.error(request, 'Erro ao atualizar sucesso!')
        #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:

        context = {
            'usuario': usuario,
            'pessoa': pessoa,
        }

        return render(request, 'people/dashboard/pessoa_detalhe.html', context)


@login_required()
def excluir(request, codigo):
    usuario = User.objects.get(id=request.user.id)
    pesssoa = People.objects.get(codigo=codigo)
    pesssoa.delete()

    sweetify.success(request, 'Registro excluído com sucesso!', timer=700)

    return redirect('/pessoas/lista')


@login_required()
def relatorios(request):
    usuario = User.objects.get(id=request.user.id)

    context = {

        'usuario': usuario,
    }

    return render(request, 'people/dashboard/relatorios.html', context)


@login_required()
def lista_homens(request):
    usuario = User.objects.get(id=request.user.id)
    if request.POST:

        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            sweetify.success(request, 'Registro cadastrado com sucesso!')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    else:

        pessoas = People.objects.filter(sexo='M')

        form = PessoaForm()

        context = {
            'pessoas': pessoas,
            'usuario': usuario,
            'form': form
        }

        return render(request, 'people/dashboard/pessoas.html', context)


@login_required()
def lista_mulheres(request):
    usuario = User.objects.get(id=request.user.id)
    if request.POST:

        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            sweetify.success(request, 'Registro cadastrado com sucesso!')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    else:

        pessoas = People.objects.filter(sexo='F')

        form = PessoaForm()

        context = {
            'pessoas': pessoas,
            'form': form,
            'usuario': usuario,
        }

        return render(request, 'people/dashboard/pessoas.html', context)


@login_required()
def maisvelhas(request):
    usuario = User.objects.get(id=request.user.id)
    pessoas = People.objects.all().order_by('data_nasc', 'nome')[0:10]

    context = {
        'pessoas': pessoas,
        'usuario': usuario,
    }

    return render(request, 'people/dashboard/pessoas_table.html', context)


@login_required()
def maisnovas(request):
    usuario = User.objects.get(id=request.user.id)
    pessoas = People.objects.all().order_by('-data_nasc', 'nome')[0:10]

    context = {
        'pessoas': pessoas,
        'usuario': usuario,
    }

    return render(request, 'people/dashboard/pessoas_table.html', context)


def json(request, codigo):
    qs = People.objects.filter(codigo=codigo)
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def json_maisvelhas(request):
    qs = People.objects.all().order_by('data_nasc', 'nome')[0:10]
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def json_maisnovas(request):
    qs = People.objects.all().order_by('-data_nasc', 'nome')[0:10]
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def busca(request):

    busca = request.GET.get('nome')
    usuario = User.objects.get(id=request.user.id)
    Pessoa = People.objects.all()

    if busca:
        Pessoa = People.objects.filter(nome__icontains=busca)

    context = {
        'pessoas': Pessoa,
        'usuario': usuario,
    }

    return render(request, 'people/dashboard/pessoas.html', context)