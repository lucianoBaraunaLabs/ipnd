# Anotações sobre python sobre - Cap03 - Lesson 9 - Depuração profunda

### Estratégisas para debug
Depuração: Revisando estratégias
Nós analisamos cinco estratégias de debugging nesta aula.

Examinar as mensagens de erro que, quando programas, dão erro

A última linha de Python Tracebacks dirá a você o que deu errado. Ler de trás para frente, a partir daí, dirá cada vez mais sobre em que ponto o problema ocorreu.

Partir de um exemplo de código funcional

Caso seu código modificado não funcione, comente as linhas e faça modificações passo a passo ao código de exemplo até conseguir o resultado esperado.

Verificar se o exemplo funciona

Só porque você encontrou um código de exemplo, não significa que ele funcionará em seu sistema. Verifique o código de exemplo que você está usando para ter certeza que ele se comporta como você espera.

Verificar (print) resultados intermediários

Quando seu código não dá erros, mas não se comporta como esperado, adicione declarações print a seu programa para ver onde as coisas param de se comportar corretamente no código.

Manter e comparar versões antigas
Quando você tem uma versão que funciona, salve-a antes de adicioná-la ao código. Isso permitirá que você volte caso introduza muitos bugs.

### Comentar seu código para ajudar a debugar


Você já deve ter notado diversos comentários no código que usamos no Nanodegree. Comentários são linhas de código ignoradas pelo computador, que existem para fazer anotações (para si próprio ou outros programadores) sobre o programa. Adicionar comentários pode ajudar (você ou outra pessoa) a depurar seu código: quando algo der errado, basta comparar o que o comentário diz que o código deveria fazer ao que ele realmente faz.

Em Python, # indica o começo de um comentário. Tudo escrito nessa linha (depois do #) é ignorado pelo computador. Outras linguagens de programação usam símbolos diferentes, mas toda linguagem tem alguma forma de fazê-lo.

Programadores têm diversas regras sobre como escrever comentários descritivos sem interferir na legibilidade do código. Durante este Nanodegree e o restante da sua carreira como programador, você precisará seguir esse princípio. Aqui vão algumas dicas sobre como fazer isso:

1) Não comente códigos "óbvios"
O que é óbvio pode mudar conforme você desenvolve suas habilidades, mas, em geral, se o código já permite entender o objetivo, ele não deve ser comentado. Um exemplo de comentário supérfluo a se evitar:
```
print "Hello" # imprime "hello"
```
2) Comece suas funções com um comentário
Todas as funções devem começar com um comentário descrevendo o que ela recebe (os inputs, também chamados de parâmetros ou argumentos da função) e o que ela devolve (os outputs, ou saída da função), e explicar seu comportamento. Isso ajuda a entender o objetivo da função. Exemplo:
```
def eh_bissexto(ano):
    # Recebe um número e devolve True se ele representa
    # um ano bissexto ou False, caso contrário.
Em Python (mas não em todas as linguagens), você também pode (e deve!) comentar suas funções com um docstring. Esse é um tipo de string de múltiplas linhas que age como um comentário descritivo para a função, mas é ignorado quando o código é executado, e pode ser acessado por usuários de sua função.

def  eh_bissexto(ano):
    '''Recebe um número e devolve True se ele representa
    um ano bissexto ou False, caso contrário.'''
Em funções mais complexas, você pode dar mais detalhes sobre os argumentos e saídas da função, (dizendo seu tipo e o que representa no código). Opcionalmente, também é possível dar exemplos de uso (como usar a função, qual é a saída esperada) e citar as exceções que ela pode gerar (exceções são as mensagens de erro caso seu código trave). No caso da função acima, isso é desnecessário. Entretanto, se precisássemos de mais detalhes, o estilo a seguir seria este:

def eh_bissexto(ano):
    '''
    Verifica se o argumento 'ano' corresponde a um ano bissexto,

    Argumentos:
        ano (int): o ano que desejamos verificar se é bissexto.

    Saída:
        bool: 'True' se o ano passado é bissexto ou
        'False', caso contrário.

    Exceções:
        TypeError: Se 'ano' não for um inteiro

    Exemplos:
        >>> eh_bissexto(2000)
        True
        >>> eh_bissexto(2001)
        False
    '''
```
Você pode documentar suas funções com comentários (#) ou docstrings (''' '''), mas seja consistente: não misture ambos. A mesma coisa vale para classes (um conceito que você aprenderá mais à frente).

3) Mantenha comentários atualizados
Seu código pode se tornar extremamente confuso se você mudar alguma parte e não atualizar o comentário que o descreve. Certifique-se de manter comentários e código alinhados, para evitar que um leitor de seu código (inclusive você mesmo) se confunda. O principal propósito de comentários é, afinal, ajudar quem lê seu código a entender como ele deveria funcionar, caso algo desse errado. Isso se torna difícil se seus comentários tiverem informações incorretas!

4) Seja conciso
Comentários devem ser curtos e explicar apenas os detalhes mais importantes. Se você notar que precisa de comentários muito longos para esclarecer partes confusas do código, talvez precise repensar sua abordagem. Em geral, um código bem escrito precisa de poucos comentários.