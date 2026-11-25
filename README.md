# SONORA — desafio de debugging

Projeto local e fictício. Não use dados pessoais nem senhas reais.

## Como executar

Requer Python 3.10–3.14 e internet para instalar as dependências na primeira execução. Extraia o ZIP, abra a pasta no VS Code e pressione Ctrl+Shift+B (Windows/Linux) ou Cmd+Shift+B (macOS). Alternativamente, no terminal da pasta:

- Windows: `py -3 iniciar.py`
- macOS/Linux: `python3 iniciar.py`
- Se `python` apontar para Python 3 compatível: `python iniciar.py`

Abra http://127.0.0.1:8000/. O inicializador cria `.venv`, instala Django e pytest, aplica migrações e prepara os dados locais. Ctrl+C encerra o servidor. Caso a porta esteja ocupada, use `--port 8001`.

## Materiais e investigação

Leia `REQUISITOS.md` e `CHAMADOS_ABERTOS.docx`. Comece pelos chamados, relacione cada relato ao requisito, escreva testes unitários para confirmar a falha e só então corrija. Depois, investigue os chamados que permanecerem abertos. Testes de Django ficam como atividade complementar. Nem todo relato implica um defeito. Registre evidências antes de encerrar cada chamado.

Conta de referência já existente: `demo@example.com`, senha `Sonora2026!`. Use apenas dados fictícios. Os bancos manuais não são os bancos temporários de teste. Para repetir cadastros já aceitos, use uma nova identificação de e-mail ou reinicialize os bancos locais conforme instrução abaixo.

## Testes

Execute `py -3 iniciar.py --test` no Windows ou `python3 iniciar.py --test` no macOS/Linux. O pytest está configurado em `pytest.ini`; escreva os testes em `tests/test_cadastro.py` ou crie novos arquivos `test_*.py`. O teste inicial só verifica o funcionamento do pytest.

- Funções puras de validação não precisam acessar o banco.
- Para testar formulários e requisições que acessam o banco, use `@pytest.mark.django_db(databases="__all__")`.
- A fixture `client` simula requisições HTTP sem servidor; `reverse("cadastros:cadastro")`, `reverse("cadastros:login")` e `reverse("cadastros:area")` resolvem as rotas.
- Crie os próprios dados de teste em cada caso, sem depender dos registros de demonstração. Os testes não executam `seed_demo`.

## Organização

- `config/settings.py`: configuração Django
- `cadastros/models.py`: modelo de perfil
- `cadastros/forms.py`: validação de formulários
- `cadastros/validacoes.py`: funções de regras de negócio
- `cadastros/services.py`: operações de cadastro e credencial
- `cadastros/views.py`: fluxo HTTP
- `cadastros/urls.py`: rotas
- `cadastros/templates/` e `templates/`: HTML
- `cadastros/static/`: CSS e JavaScript
- `tests/`: testes escritos pelos participantes

Não distribua bancos com dados reais. Para recomeçar a demonstração, encerre o servidor e exclua os arquivos `db.sqlite3` e `cadastros.sqlite3` (isso apaga os cadastros locais); execute o inicializador novamente.
