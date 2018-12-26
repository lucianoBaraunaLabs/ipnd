# Anotações gerais

Existe um padrão de comentário em python para documentar uma função, que seria:

Comentando uma função:
```
def obtem_frase_lacunas_respostas(dificuldade):
    """
    Obtém a frase, as lacunas e as respostas para uma dificuldade.
    Args:
        dificuldade (string): Dificuldade 'fácil', 'medio' ou 'dificil'.
    Returns:
        (string) Frase com lacunas.
        (list) Lista de lacunas da frase.
        (list) Lista de respostas para cada lacuna.
    """
```
Comentando uma objeto:
```
# Dicionário: dificuldade x {frase, lacunas, respostas}
frases_lacunas_respostas = {
    'facil': {
        'frase': 'Lorem ipsum',
        'lacunas': [1,2,3],
        'respostas': [21,23,25]
    }
}
```