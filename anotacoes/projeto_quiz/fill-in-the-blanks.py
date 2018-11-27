# -*- coding: utf-8 -*-
# IPND Projeto Final

# Você construiu um jogo Mad-Libs com alguma ajuda de Sean.
# Agora você vai trabalhar em seu próprio jogo para praticar suas habilidades e demonstrar o que aprendeu.

# Para este projeto, você estará construindo um questionário "Preencha os Espaços em Brancos".
# Seu questionário exibirá ao usuário um parágrafo contendo vários espaços em branco.
# O usuário deve então ser solicitado a preencher cada espaço em branco adequadamente para completar o parágrafo.
# Isso pode ser usado como uma ferramenta de estudo para ajudá-lo a lembrar o vocabulário importante!

# Nota: Seu jogo terá que aceitar a entrada do usuário, assim como o gerador Mad Libs,
# yvocê não poderá executá-lo usando o recurso `Build` do Sublime.
# Em vez disso, você precisará executar o programa no Terminal ou no IDLE.

# Para ajudar você a começar, fornecemos um parágrafo de amostra que você pode usar ao testar seu código.
# Seu jogo deve consistir de 3 ou mais níveis, então você deve adicionar seus próprios parágrafos também!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# A resposta para ___1___ é 'function'. Você pode descobrir os outros?

# Também fornecemos um arquivo chamado fill-in-the-blanks.pyc, que é uma versão funcional do projeto.
# Um arquivo .pyc é um arquivo Python que foi traduzido em "código de bytes".
# Isso significa que o código será executado da mesma forma que o arquivo .py original, mas quando você o abrir
# não será parecido com o código Python! Mas você pode executá-lo como um arquivo normal do Python
# para ver como seu código deve se comportar.

# Dica: Pode ajudar a pensar sobre como este projeto se relaciona com o gerador Mad Libs que você construiu com Sean.
# No gerador Mad Libs, você pega um parágrafo e substitui todas as instâncias de NOUN e VERB.
# Como você pode adaptar esse design para trabalhar com espaços em branco numerados?

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


def start():
    saudacoes()

start()


