Um programa para extrair os códigos pin de uma lista de poesias

## O que o código faz

A função `pin_extractor(poems)` recebe uma **lista de poesias** e devolve uma
**lista de códigos** (um código para cada poesia).

Cada código é formado por números obtidos a partir das palavras da poesia,
seguindo estas regras:

1. A poesia é dividida em linhas.
2. Cada linha é dividida em palavras.
3. Se a linha tiver uma palavra na posição do seu próprio número (contando a
   partir de 0), usa-se o **tamanho dessa palavra**.
4. Se não tiver, usa-se `0`.

Os números são juntados para formar o código daquela poesia.

## Exemplo

Para a poesia:

```
There
once
was
a
dragon
```

O resultado é `"50000"`, porque só a primeira linha (`There`) tem palavra na
posição 0 — e `There` tem 5 letras. As demais linhas não têm palavra na posição
correspondente, então viram `0`.

## Arquivos

- `pin_extractor.py` — contém a função `pin_extractor`.
- `extrator_pin.py` — usa a função com algumas poesias de exemplo e imprime o resultado.

## Como executar

```bash
cd others/extrator_pin
python3 extrator_pin.py
```
