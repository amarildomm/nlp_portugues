import os
import sys
from django.shortcuts import render

# Repo root: nlp_demo/ -> django_example/ -> repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, REPO_ROOT)

# nlp_portugues abre arquivos com caminho relativo (listas_ptBR/...),
# por isso muda temporariamente o diretorio de trabalho para a raiz do repo.
_cwd = os.getcwd()
os.chdir(REPO_ROOT)
import nlp_portugues as nlp
nlp_pt = nlp.preprocessing_ptBR()
os.chdir(_cwd)


def index(request):
    context = {}

    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        remover_verbos = request.POST.get('verbs') == 'on'
        remover_adjetivos = request.POST.get('adjectives') == 'on'
        converter_singular = request.POST.get('plural') == 'on'
        retornar_string = request.POST.get('string') == 'on'

        if texto:
            resultado = nlp_pt.proc_text(
                text=texto,
                verbs=remover_verbos,
                adjectives=remover_adjetivos,
                plural=converter_singular,
                string=retornar_string,
            )
            context['texto_original'] = texto
            context['resultado'] = resultado
            context['remover_verbos'] = remover_verbos
            context['remover_adjetivos'] = remover_adjetivos
            context['converter_singular'] = converter_singular
            context['retornar_string'] = retornar_string

    return render(request, 'nlp_demo/index.html', context)
