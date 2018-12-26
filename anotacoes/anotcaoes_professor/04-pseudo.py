dificuldade = pergunta_dificuldade()
frase = obtem_frase_dificuldade(dificuldade)

para cada lacuna:
    mostra_frase(frase)
    resposta = pergunta_resposta_frase(frase, lacuna)

    se resposta certa:
        mostra_parabens_lacuna()
        frase = substitui_lacuna_pro_respsota(frase, lacuna, resposta)
        passa para proxima lacuna
    
    se resposta errada:
        mostra_tente_novamente()
        repete pergunta para mesma lacuna

# Se o programa chegou até aqui, usuário acertou tudo
mostra_parabens_final()
encerra_programa()