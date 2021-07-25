from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
# Create your views here.
from epoca.forms import ContactoForms


def base (request):
    return render(request, "base.html")

def contacto(request):
    form = ContactoForms(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "base.html")

    context = {"form": form}
    return render(request, "contacto.html", context)


def conetar(request):
    if request.POST:
        email = request.POST["email"]
        senha = request.POST["senha"]
        usuario = authenticate(username=email, password=senha)
        login(request, usuario)
        return render(request, "listaProdutos.html")
    return render(request, "conectar.html")

def disconetar(request):
    logout(request)
    return render(request, "base.html")