# -*- coding: utf-8 -*-
# Funções falsas
def mostra_boas_vidnas():
    print 'Bem vindo ao meu jogo !!!'

def pergunta_dificuldade():
    return 'facil'

def obtem_frase_dificuldade(dificuldade):
    return 'frase __1__ de __2__ teste __3__', ['__1__', '__2__', '__3__']

def pergunta_resposta_lacuna(lacuna):
    return 'resposta certa'

def substitui_lacuna_por_resposta(frase, lacuna, resposta):
    return frase

def mostra_parabens_final(frase):
    print 'parabéns!!!'

# Esqueleto do programa
def inicia_jogo():
    mostra_boas_vindas()
    dificuldade = pergunta_dificuldade()
    frase, lacunas = obtem_frase_dificuldade()
    for lacuna in lacunas:
        print frase
        resposta = pergunta_resposta_lacuna(lacuna)
        frase = substitui_lacuna_por_resposta(frase, lacuna, resposta)
    mostra_parabens_final(frase)

inicia_jogo()