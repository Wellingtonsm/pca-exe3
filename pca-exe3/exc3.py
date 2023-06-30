import random

def quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operadores = ['+', '-', '*']
    operador = random.choice(operadores)
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    else:
        resultado = num1 * num2
    pergunta = 'Quanto é ' + str(num1) + ' ' + operador + ' ' + str(num2) + '? '
    resposta = int(input(pergunta))
    if resposta == resultado:
        print('Correto!')
        return True
    else:
        print('Incorreto. A resposta correta é', resultado)
        return False

def jogo():
    pontuacao = 0
    num_perguntas = 5
    reiniciar = True
    
    while reiniciar:
        for i in range(num_perguntas):
            print('Pergunta', i+1)
            if quiz():
                pontuacao += 1
            print()
         
        print('Você acertou', pontuacao, 'perguntas de', num_perguntas)
        
        if pontuacao <= 3:
            print('O resultado foi ruim, estude mais!')
        else:
            print('Parabéns, continue assim!')
        
        resposta = input('Deseja jogar novamente? (S/N): ')
        if resposta.lower() != 's':
            reiniciar = False
        else:
            pontuacao = 0

jogo()