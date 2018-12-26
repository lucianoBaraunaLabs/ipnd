# -*- coding: utf-8 -*-

frase_lacuna_resposta = {
    "facil": {
        "frase": "O __1__ do __2__ do __3__ é __4__",
        "lacuna": ["__1__", "__2__", "__3__", "__4__"],
        "resposta":["peito", "pé", "pedro", "preto"]
    },
    "medio": {
        "frase": "O __1__ foi __2__ em __3__ de __4__ de __5__",
        "lacuna": ["__1__", "__2__", "__3__", "__4__", "__5__"],
        "resposta":["Brasil", "descoberto", "22", "abril", "1500"]
    },
    "dificil": {
        "frase": "A __1__ de __2__ e __3__ aconteceu em __4__ e __5__ de __6__ em __7__",
        "lacuna": ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"],
        "resposta":["Bomba", "Hiroshima", "Nagasaki", "6", "9", "agosto", "1945"]
    }
}

def saudacoes():
    """
    Exibe mensagem de boas vindas
    """
    print "Bem vindo ao jogo !!!!"

def pergunta_dificuldade():
    dificuldade = raw_input('>>> Escolha um nível de dificuldade : (facil | medio | dificil) \n')
    while True:
        if dificuldade == 'facil':
            return dificuldade
        elif dificuldade == 'medio':
            return dificuldade
        elif dificuldade == 'dificil':
            return dificuldade
        else:
            dificuldade = raw_input('> Opção inválida, tente novamente.\n')

def obtem_frase_dificuldade(dificuldade):
    return frase_lacuna_resposta[dificuldade]["frase"], frase_lacuna_resposta[dificuldade]["lacuna"], frase_lacuna_resposta[dificuldade]["resposta"]

# def pergunta_resposta_lacuna(lacuna_atual, frase, indice_atual, resposta):
#     input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ? ')
#     # if input_resposta == resposta[indice_atual]:
#     #     print 'opa ta certo', frase.replace(lacuna_atual, input_resposta) 
#     # else:
#     #     print('Resposta errada! Tente Novamente.')

#     # if input_resposta != resposta[indice_atual]:
#     #     print('Resposta errada! Tente Novamente.')
#     #     input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ? ')
#     # else:
#     #     print 'opa ta certo', frase.replace(lacuna_atual, input_resposta) 

#     while indice_atual < len(resposta):
#         if input_resposta == resposta[indice_atual]:
#             print 'frase nova ', frase.replace(lacuna_atual, input_resposta)
#             nova_frase = frase.replace(lacuna_atual, input_resposta)
#             return nova_frase
#         else:
#             print('Resposta errada! Tente Novamente.')
#             input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ? ')
    
    
        


        









#     print 'lacuna atual: ', lacuna_atual
#     print 'frase: ', frase
#     print 'indice_atual: ', indice_atual
#     print 'resposta: ', resposta

#     return lacuna_atual
#     # resposta_pergunta = raw_input('> A palavra do campo ' + lacuna + ' é ?')
#     # if resposta_pergunta === 
    
def start():
    saudacoes()
    dificuldade = pergunta_dificuldade()
    frase, lista_lacunas, lista_respostas = obtem_frase_dificuldade(dificuldade)
    print frase
    frase_nova = frase.replace(lista_lacunas[0], lista_respostas[0])
    # resposta_quiz = pergunta_resposta_lacuna(lacuna_atual, frase, indice_atual, resposta)
    for indice_atual, lacuna_atual in enumerate(lista_lacunas):
        input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ? ')
        while input_resposta != lista_respostas[indice_atual]:
            print 'Resposta errada! Tente novamete.'
            input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ? ')
        print 'Resposta certa! Veja como está ficando a frase:'
        frase_nova = frase_nova.replace(lista_lacunas[indice_atual], lista_respostas[indice_atual])
        print frase_nova
start()


