from django import forms
from django.contrib.auth.models import User
from . import validacoes


class CadastroForm(forms.Form):
    nome = forms.CharField(label="Nome completo", max_length=150)
    email = forms.EmailField(label="E-mail", max_length=150)
    idade = forms.IntegerField(label="Idade", min_value=1, max_value=120)
    senha = forms.CharField(
        label="Senha", strip=False,
        help_text="De 8 a 128 caracteres. Use maiúscula, minúscula, número e símbolo. Não inclua a palavra senha nem palavras do seu nome.",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    confirmacao = forms.CharField(label="Confirme sua senha", strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}))

    def clean_nome(self):
        nome = " ".join(self.cleaned_data["nome"].split())
        if not validacoes.nome_valido(nome):
            raise forms.ValidationError("Informe pelo menos duas palavras no nome.")
        return nome

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if any(User.objects.using(alias).filter(username__iexact=email).exists() for alias in ("default", "legacy")):
            raise forms.ValidationError("Já existe uma conta com esse e-mail.")
        return email

    def clean_idade(self):
        idade = self.cleaned_data["idade"]
        if not validacoes.idade_valida(idade):
            raise forms.ValidationError("O cadastro é permitido a partir dos 18 anos.")
        return idade

    def clean_senha(self):
        senha = self.cleaned_data["senha"]
        erros = []
        if not validacoes.tamanho_senha_valido(senha):
            erros.append("A senha deve ter entre 8 e 128 caracteres.")
        if not validacoes.composicao_senha_valida(senha):
            erros.append("Use os quatro tipos de caracteres: maiúscula, minúscula, número e símbolo.")
        if erros:
            raise forms.ValidationError(erros)
        return senha

    def clean(self):
        dados = super().clean()
        senha, confirmacao = dados.get("senha"), dados.get("confirmacao")
        if senha is not None and confirmacao is not None:
            if not validacoes.senhas_coincidem(senha, confirmacao):
                self.add_error("confirmacao", "As senhas não coincidem.")
        nome = dados.get("nome")
        if nome is not None and senha is not None:
            if not validacoes.conteudo_senha_valido(senha, nome):
                self.add_error("senha", "A senha não pode conter a palavra senha nem palavras do seu nome.")
        return dados


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", max_length=150)
    senha = forms.CharField(label="Senha", max_length=128, strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))
