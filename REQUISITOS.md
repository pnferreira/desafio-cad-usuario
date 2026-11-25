# SONORA | Especificação funcional

Revisão 3 — Ambiente de treinamento. Dados exclusivamente fictícios.

## Cadastro

| ID | Critério de aceitação |
|---|---|
| RF01 | Nome, e-mail, idade, senha e confirmação são obrigatórios. |
| RF02 | Nome com pelo menos duas palavras; espaços extras são ignorados. Máximo de 150 caracteres na entrada. |
| RF03 | Idade inteira de 18 a 120, inclusive. |
| RF04 | E-mail válido, com no máximo 150 caracteres. |
| RF05 | E-mail único, sem distinção de maiúsculas e minúsculas; espaços nas extremidades são ignorados. |
| RF06 | Senha de 8 a 128 caracteres, inclusive. |
| RF07 | Senha deve conter os quatro tipos: letra maiúscula, letra minúscula, dígito decimal e símbolo (não alfanumérico e não espaço). |
| RF08 | Senha não pode conter a sequência `senha` nem qualquer palavra do nome informado, mesmo inserida em uma sequência maior. A comparação ignora maiúsculas/minúsculas, mas não acentos. Caracteres isolados ou fora de ordem são permitidos. |
| RF09 | Senha e confirmação exatamente iguais, inclusive espaços e maiúsculas/minúsculas. |

O backend deve rejeitar entradas inválidas e apresentar mensagem de validação.

## Fluxo completo

| ID | Critério de aceitação |
|---|---|
| RF10 | Cadastro aceito deve persistir uma conta e um perfil, com senha armazenada por hashing. |
| RF11 | Conta criada permite login com e-mail e senha corretos; senha incorreta é recusada. |
| RF12 | Cadastro concluído e área autenticada exibem o nome e a credencial digital do usuário. |
| RF13 | Cada perfil tem um identificador de credencial único, estável nos acessos posteriores. |

A credencial não é ingresso nem comprovante de compra.
