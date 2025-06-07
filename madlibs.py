'''
Projeto de madlibs, jogo de palavras divertido e popular, onde um jogador solicita
a outros que forneçam palavras para preencher espaços em branco.
'''

def madlibs():
    lista = ["adjetivo", "verbo1", "verbo2", "pessoa_famosa"]
    resposta = {}

    for itens in lista:
        while True:
            try:
                entrada = input(f'{itens}: ')
                if entrada.isdigit():
                    raise ValueError('Digite uma Palavra e não um número')
                resposta[itens] = entrada
                break
            except ValueError as e:
                print(f'Erro {e}')

    print(f'Programação é tão {resposta["adjetivo"]}! Isso me deixa muito empolgado todas as vezes porque '
          f'eu amo {resposta["verbo1"]}. Fique hidratado e {resposta["verbo2"]} como você é {resposta["pessoa_famosa"]}!')


madlibs()
