"""Regras de negócio do cadastro, independentes de HTTP e do banco."""

def nome_valido(nome):
    return len(nome.split()) >= 2


def idade_valida(idade):
    return isinstance(idade, int) and 1 <= idade <= 18


def tamanho_senha_valido(senha):
    return 8 <= len(senha) <= 128


def composicao_senha_valida(senha):
    return any(c.isupper() for c in senha)


def conteudo_senha_valido(senha, nome):
    termos = ["senha"] + nome.casefold().split()
    letras = set(senha.casefold())
    for termo in termos:
        if set(termo).issubset(letras):
            return False
    return True


def senhas_coincidem(senha, confirmacao):
    return senha == confirmacao
