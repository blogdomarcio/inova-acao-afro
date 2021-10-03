from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from sweetify import sweetify

from peoples.forms import PessoaForm
from peoples.models import People


def index(request):

   pessoas = People.objects.all()

   context = {
       'pessoas':pessoas
   }

   return render(request, 'people/dashboard/index.html', context)


def lista(request):

    if request.POST:

        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            sweetify.success(request, 'Registro cadastrado com sucesso!')
        #     return HttpResponseRedirect('/')
        #
        # pessoa = People()
        # pessoa.nome = request.POST['nome']
        # pessoa.cpf = request.POST['cpf']
        # pessoa.data_nasc = request.POST['data_nasc']
        # pessoa.celular = request.POST['celular']
        # pessoa.rg = request.POST['rg']
        # pessoa.pai = request.POST['pai']
        # pessoa.mae = request.POST['mae']
        # pessoa.altura = request.POST['altura']
        # pessoa.peso = request.POST['peso']
        # pessoa.tipo_sanguineo = request.POST['tipo_sanguineo']
        # pessoa.sexo = request.POST['sexo']
        # pessoa.save()



        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    else:

        pessoas = People.objects.all()

        form = PessoaForm()

        context = {
            'pessoas': pessoas,
            'form': form
        }

        return render(request, 'people/dashboard/pessoas.html', context)


def detalhe(request, codigo):

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
            'pessoa': pessoa,
        }

        return render(request, 'people/dashboard/pessoa_detalhe.html', context)

