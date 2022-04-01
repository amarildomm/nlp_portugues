<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

## Biblioteca para Processamento de Linguagem Natural em Português - nlp_portugues

Biblioteca para pré-processamento de Natural Language Processing (NLP) completa no idioma português

Conteúdo criado durante o PhD em Information Science pela Universidade Federal de Minas Gerais
Escola de Ciência da Informação Data: 25/05/2020

## Listas de verbos, adjetivos e stop-words em português:

	* listas_ptBR/stop_words.txt = Lista contendo 1731 stop-words em português
	* listas_ptBR/adjetivos.json = Lista contendo 6627 adjetivos em português
	* listas_ptBR/verbos.json    = Lista contendo 260524 verbos/conjugações em português

### Classe preprocessing_pt_BR em Python:

Para usar as funções e listas de forma fácil, foi criada uma classe chamada preprocessing_ptBR dentro do pacote nlp_portugues.py. Para instanciar a classe, é necessário usar os comandos:

```sh
import nlp_portugues as nlp
nlp_pt = nlp.preprocessing_ptBR() 
```
### Usando métodos da classe:

1. Método clear_text():
Esse método remove de uma string acentos, caracteres especiais, números e converte todas de maíusculo para minúsculo:

* plural2_singular(self,tokens):

Esse método converte uma lista de tokens que contenham termos no plural para singular:

```sh
nlp_pt.clear_text('Esse é um exemplo texto limpo com o método clear_text() 999 !!!')
```
_'esse e um exemplo texto limpo com o metodo cleartext'_

2. Método plural2_singular():
Esse método converte uma lista de tokens que contenham termos no plural para singular.

Para utilizá-lo passe os tokens já limpos sem acentos, caracteres especiais e números, que pode ser feito com o método clear_text().

```sh
tokens_converter = ['caldos','leoes', 'nos', 'iguarias','marrons', 'jornais','caes', 'flores']
nlp_pt.plural2_singular(tokens_converter)
*['caldo', 'leao', 'no', 'iguaria', 'marrom', 'jornal', 'cao', 'flor']*
```

### Versões Anteriores
Para ver as versões anteriores da biblioteca (Incluindo as que fazem web scraping), veja as tags do projeto.

### Licença
The MIT License (MIT)

Copyright (c) 2020 Amarildo Magalhães 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

