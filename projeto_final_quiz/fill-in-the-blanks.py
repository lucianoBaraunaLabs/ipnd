# -*- coding: utf-8 -*-

frase_lacunas_resposta = {
    "iniciante": {
        "frase": "O rato roeu __1__ __2__ do __3__ de __4__",
        "lacunas": ["__1__", "__2__",  "__3__",  "__4__"],
        "respostas":["a", "roupa", "rei", "roma"]
    },
    "facil": {
        "frase": "__1__ __2__ do pé __3__ pedro é __4__",
        "lacunas": ["__1__", "__2__", "__3__", "__4__"],
        "respostas":["o", "peito", "do",  "preto" ]
    },
    "medio": {
        "frase": "O Brasil foi descoberto pelos __1__ em __2__ de __3__ de __4__",
        "lacunas": ["__1__", "__2__", "__3__", "__4__"],
        "respostas":[ "portugueses", "22", "abril", "1500"]
    },
    "dificil": {
        "frase": "A Bomba de __1__ e __2__ aconteceu em __3__ e __4__ de agosto em __5__",
        "lacunas": ["__1__", "__2__", "__3__", "__4__", "__5__"],
        "respostas":["Hiroshima", "Nagasaki", "6", "9", "1945"]
    }
}

def saudacoes():
    """
    Exibe mensagem de boas vindas
    """
    print "Bem vindo ao jogo !!!!"

def pergunta_dificuldade():
    """
    Pegunta dificuldade ao usuário

    Return:
    string: Nível de dificuldade

    """
    dificuldade = raw_input('>>> Escolha um nível de dificuldade : (iniciante | facil | medio | dificil) \n').lower()
    while True:
        if dificuldade == 'iniciante':
            return dificuldade
        if dificuldade == 'facil':
            return dificuldade
        elif dificuldade == 'medio':
            return dificuldade
        elif dificuldade == 'dificil':
            return dificuldade
        else:
            dificuldade = raw_input('> Opção inválida, tente novamente.\n')

def obtem_dados_jogo(dificuldade):
    """
    Obtem a frase, lacunas, repostas
   
    Args:

    dificuldade (string): Dificuldade selecionada pelo usuário

    Returns:

    string: Frase com lacunas, 
    list: Lista de Lacunas, 
    list: Lista de Respostas

    """
    configuracoes_jogo = frase_lacunas_resposta[dificuldade]
    return configuracoes_jogo["frase"], configuracoes_jogo["lacunas"], configuracoes_jogo["respostas"]

def pergunta_resposta(frase, lista_lacunas, lista_respostas):
    """
    Realiza a pergunta, validando a resposta retornandoa

    Args:

    frase (string): Frase com lacunas
    lista_lacunas (list): Lista de lacunas
    lista_respostas (list): Lista de respostas

    Return:
    (string): Resposta

    """
    frase_nova = frase.replace(lista_lacunas[0], lista_respostas[0])
    for indice_atual, lacuna_atual in enumerate(lista_lacunas):
        input_resposta = raw_input('> A palavra do campo ' + lacuna_atual + ' é ? \n')
        while input_resposta != lista_respostas[indice_atual]:
            print '> Resposta errada! Tente novamete.'
            input_resposta = raw_input('A palavra do campo ' + lacuna_atual + ' é ?\n')
        print '> Resposta certa! Veja como está ficando a frase:\n'
        frase_nova = frase_nova.replace(lista_lacunas[indice_atual], lista_respostas[indice_atual])
        print frase_nova

    
def start():
    """
    Inicia o jogo
    """
    saudacoes()
    dificuldade = pergunta_dificuldade()
    frase, lista_lacunas, lista_respostas = obtem_dados_jogo(dificuldade)
    print frase
    pergunta_resposta(frase, lista_lacunas, lista_respostas)
start()


