{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "README.md repositório nlp_portugues",
      "provenance": [],
      "collapsed_sections": [
        "a2ZCn095uAoc"
      ],
      "authorship_tag": "ABX9TyPSUfAOClFKz4t2T7TvE149",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "<div id=\"top\"></div>\n",
        "<!--\n",
        "*** Thanks for checking out the Best-README-Template. If you have a suggestion\n",
        "*** that would make this better, please fork the repo and create a pull request\n",
        "*** or simply open an issue with the tag \"enhancement\".\n",
        "*** Don't forget to give the project a star!\n",
        "*** Thanks again! Now go create something AMAZING! :D\n",
        "-->\n",
        "\n",
        "## Biblioteca para Processamento de Linguagem Natural em Português - nlp_portugues \n",
        "\n",
        "Biblioteca para pré-processamento de Natural Language Processing (NLP) completa no idioma português\n",
        "\n",
        "Conteúdo criado durante o PhD em Information Science pela Universidade Federal de Minas Gerais  \n",
        "Escola de Ciência da Informação\n",
        "Data: 25/05/2020\n",
        "\n",
        "### Listas de verbos, adjetivos e stop-words em português:\n",
        "\n",
        "\t* listas_ptBR/stop_words.txt = Lista contendo 1731 stop-words em português\n",
        "\t* listas_ptBR/adjetivos.json = Lista contendo 6627 adjetivos em português\n",
        "\t* listas_ptBR/verbos.json    = Lista contendo 260524 verbos/conjugações em português\n",
        "\n",
        "### Classe preprocessing_pt_BR em Python:\n",
        "\n",
        "Para usar as funções e listas de forma fácil, foi criada uma classe chamada preprocessing_ptBR dentro do pacote nlp_portugues.py. Para instanciar a classe, é necessário usar os comandos:"
      ],
      "metadata": {
        "id": "IGzcyaPLr_X9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from nlp_portugues import preprocessing_ptBR\n",
        "nlp_pt = preprocessing_ptBR()"
      ],
      "metadata": {
        "id": "cRszOib8pBRp"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Usando métodos da classe:"
      ],
      "metadata": {
        "id": "2dyT8kPAtEHN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### 1. Método clear_text():\n",
        "\n",
        "Esse método remove de uma string acentos, caracteres especiais, números e converte todas de maíusculo para minúsculo:"
      ],
      "metadata": {
        "id": "SAQhxFtktL6D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nlp_pt.clear_text('Esse é um exemplo texto limpo com o método clear_text() 999 !!!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "QKn8XpCatZZ4",
        "outputId": "ae078544-4d27-4045-e0fc-890a5ee527d6"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'esse e um exemplo texto limpo com o metodo cleartext'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### 2. Método plural2_singular():\n",
        "\n",
        "Esse método converte uma lista de tokens que contenham termos no plural para singular. \n",
        "\n",
        "Para utilizá-lo passe os tokens já limpos sem acentos, caracteres especiais e números, que pode ser feito com o método clear_text()."
      ],
      "metadata": {
        "id": "G-iwceq4sZuG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tokens_converter = ['caldos','leoes', 'nos', 'iguarias','marrons', 'jornais','caes', 'flores']\n",
        "nlp_pt.plural2_singular(tokens_converter)"
      ],
      "metadata": {
        "id": "mf6x8_b0pPzj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "afa7973e-ae56-452b-b258-818bebc9ee9d"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['caldo', 'leao', 'no', 'iguaria', 'marrom', 'jornal', 'cao', 'flor']"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### 3. Método proc_text():\n",
        "\n",
        "Esse é o método principal da biblioteca. Ele possui parâmetros que são explicados abaixo e podem executar diversas tarefas de NLP de uma única vez:\n",
        "\n",
        "* **text** = texto puro sem qualquer formatação\n",
        "* **verbs** = True se quiser remover verbos do texto\n",
        "* **string** = True se quiser que seja devolvida um texto ao invés de lista com tokens\n",
        "* **text_add** = Algum texto complementar ao parâmetro **text**\n",
        "* **adjectives** = True se deseja remover os adjetivos do texto\n",
        "* **plural** = True converter todas as palavras do texto para singular\n",
        "\n"
      ],
      "metadata": {
        "id": "5DeHwY71vQZw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nlp_pt.proc_text(text = 'os corações valentes foram caminhando até chegar na Inglaterra.',verbs=True,string=True,adjectives=True,plural=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "_pUkLlrWpk3h",
        "outputId": "991d84be-a835-47e9-ac44-4d5d2f49cff2"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'coracao inglaterra'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nlp_pt.proc_text(text = 'os corações valentes foram caminhando até chegar na Inglaterra.',verbs=True,string=True,adjectives=False,plural=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "VLrI1HUnwYb_",
        "outputId": "94f92274-76e5-4735-b042-d97b199b3a3d"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'coracoes valentes inglaterra'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nlp_pt.proc_text(text = 'os corações valentes foram caminhando até chegar na Inglaterra.',verbs=False,string=False,adjectives=True,plural=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7f4CLnIdwq8l",
        "outputId": "f706003f-400a-462c-efcd-8ce6e03c1db9"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['coracao', 'caminhando', 'chegar', 'inglaterra']"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    }
  ]
}
