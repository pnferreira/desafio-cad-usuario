from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import CadastroForm, LoginForm
from .services import criar_conta, dados_credencial


@require_http_methods(["GET", "POST"])
def cadastro(request):
    form = CadastroForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        try:
            perfil = criar_conta(form.cleaned_data)
        except IntegrityError:
            form.add_error("email", "Não foi possível cadastrar esse e-mail.")
        else:
            request.session["credencial_recente"] = dados_credencial(perfil)
            return redirect("cadastros:sucesso")
    return render(request, "cadastros/cadastro.html", {"form": form})


@require_GET
def sucesso(request):
    credencial = request.session.get("credencial_recente")
    if not credencial:
        return redirect("cadastros:cadastro")
    return render(request, "cadastros/sucesso.html", {"credencial": credencial})


@require_http_methods(["GET", "POST"])
def entrar(request):
    form = LoginForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        usuario = authenticate(request, username=form.cleaned_data["email"].lower(), password=form.cleaned_data["senha"])
        if usuario is not None:
            login(request, usuario)
            request.session.pop("credencial_recente", None)
            return redirect("cadastros:area")
        form.add_error(None, "E-mail ou senha inválidos.")
    return render(request, "cadastros/login.html", {"form": form})


@login_required
@require_GET
def area(request):
    return render(request, "cadastros/area.html", {"credencial": dados_credencial(request.user.perfil)})


@require_POST
def sair(request):
    logout(request)
    return redirect("cadastros:login")
