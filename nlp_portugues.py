#Pacote criado por Amarildo Magalhães para tratamento de text em Português
#Data: 25-05-2020
#Versão 1.0
#Escola de Ciência da Informação - UFMG
#Foi criada uma lista de 400mil verbos e suas conjugações 
#Foi criada uma lista com XX ajedtivos 
#Foi criada uma lista ocm XX conjunções, preposições, advérbios e concatenada com as stop_words do NTLK em português

class preprocessing_ptBR():

    def __init__(self):
        
        ##carrega arquivos de verbos, stop-words e adjetivos
        
        import io
        import json
        # from nltk.corpus import stopwords
        
        ##STOP_WORDS
        stop_words_file       = io.open('listas_ptBR/stop_words.txt', mode='r',encoding="utf-8") 
        stops                 = stop_words_file.read().split()
        # stops                 = stopwords.words("portuguese")
        # stops                += conj_prep
        stop_words            = [self.clear_text(w) for w in stops]
        #stop_words      = pluraltosingular(stop_words)
        self.dic_stop_words   = dict.fromkeys(stop_words,1)

        ##VERBOS
        file_verbs            = "listas_ptBR/verbos.json" #lista de verbs e sua conjugacoes
        with open(file_verbs) as data_file:    
            verbs = json.load(data_file)
        verbs                 = [self.clear_text(w) for w in verbs]
        self.dic_verbs        = dict.fromkeys(verbs,1)

        ##ADJETIVOS
        file_adj              = "listas_ptBR/adjetivos.json" #lista com 4065 adjectives
        with open(file_adj) as data_file:    
            adjectives        = json.load(data_file)
        adjectives            = [self.clear_text(w) for w in adjectives]
        self.dic_adjectives   = dict.fromkeys(adjectives,1)
        
    def plural2_singular(self,tokens):
        new_lista = []
        #print(tokens)
        for palavra in tokens:

            if len(palavra) <= 2:
                new_lista.append(palavra)
            elif palavra[-1] != 's':
                new_lista.append(palavra)
            #albuns batons marrons
            elif palavra[-2] == 'n':
                new_lista.append(palavra[0:-2]+'m')
            #flores gizes vezes tenis
            elif not any((c in 'aeou') for c in palavra[:1]) and palavra[-2] == 'e' and any((c in 'nrsz') for c in palavra[-3]):
                new_lista.append(palavra[:-2])
            # aneis anzois jornais
            elif palavra[-2:] == "is" and any((c in 'aeiou') for c in palavra[-3]): 
                new_lista.append(palavra[:-2]+'l')    
            # frances portugues
            elif palavra[-2:] == "es" and any((c in 'clu') for c in palavra[-3]): 
                new_lista.append(palavra)
            # caes paes
            elif palavra[-3:] == "aes": 
                new_lista.append(palavra[:-2]+'o')
            # pequenas lobos
            elif palavra[-2] == "a" or palavra[-2] == "o": 
                new_lista.append(palavra[:-1])
            # leoes
            elif palavra[-3:] == "oes": 
                new_lista.append(palavra[:-3]+'ao')
            elif not any((c in 'ius') for c in palavra[-2]) and palavra[-3] != 'n':
                new_lista.append(palavra[:-1])
            #museus
            elif palavra[-1] == 's':
            	new_lista.append(palavra[:-1])
            #print(palavra)
        return new_lista        
        
    def clear_text(self,text_str):
        #limpar o text - retira acentos e caracteres especiais do text\n",        
        import unicodedata
        import re

        #Unicode normalize transforma um caracter em seu equivalente em latin
        try: 
            nfkd             = unicodedata.normalize('NFKD', text_str)
            text_no_accent   = u"".join([c for c in nfkd if not unicodedata.combining(c)])
            # Usa expressão regular para retornar a palavra apenas com números, letras e espaço\n",
            text       = re.sub('[^a-zA-Z ]', '', text_no_accent.lower()).split(" ")
            text_clean = [w for w in text if w != '']
            return ' '.join(map(str,text_clean))   
        except:
            return text_str            
    
    #por padrão, não remove nem verbos nem adjetivos, apenas stop_words
    def proc_text(self, text, verbs=False, string=False, text_add = '',adjectives=False, plural=False):
        
        ##limpando o texto  
        ## - removendo caracteres especiais, 
        ## - transformando maiuscula em minuscula, 
        ## - removendo numeros - 
        ## - passando de plural para singular
        ## - retorna - tokens

        text_clean = self.clear_text(text_str = text).split(" ")
        #text_clean = [w for w in text_clean if w != '']

        ##vamos remover stop-words padrão
        text = [w for w in text_clean if w not in self.dic_stop_words]

        ##removendo do texto original texto adicional inserindo para remover
        if text_add != '':
        	text_add_clean = self.clear_text(text_add).split()
        	text           = [w for w in text if w not in text_add_clean]

        ##passa todas palavras para singular
        if plural == True:
            text = self.plural2_singular(text)

        ##se eh para remover os verbs tambem
        if verbs==True:
            text = [w for w in text if w not in self.dic_verbs]

        ##se eh para remover os adjectives tambem
        if adjectives==True:
            text = [w for w in text if w not in self.dic_adjectives]

        if string==False:
            return text
        else:
            return ' '.join(map(str,text))    