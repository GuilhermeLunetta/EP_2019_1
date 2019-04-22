# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Guilherme Lunetta, guilhermecl1@al.insper.edu.br
# - aluno B: Marcelo Neves, marcelosn2@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "elevador": "Tomar o elevador para outros andares",
                "biblioteca": "Ir para a biblioteca",
                "auditorio": "Ir para o auditório"
            }
        },
        "elevador": {
            "titulo": "Elevador",
            "descricao": "Você está no elevador, ele te da acesso aos outros andares",
            "opcoes": {
                "andar1": "Primeiro andar",
                "andar2": "Segundo andar",
                'andar3': 'Terceiro andar',
                'andar4': 'Quarto andar',
                'andar5': 'Quinto andar',
                'subsolo': 'Subsolo',
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                'auditorio': 'Ir ao auditório',
                'procurar': 'Procurar por algo que possa te ajudar'
            }
        },
        'auditorio': {
            'titulo': 'Auditório',
            'descricao': 'Você está no auditório, aparentemente não há nada aqui.',
            'opcoes': {
                'inicio': 'Voltar para o saguão de entrada',
                'elevador': 'Tomar o elevador para outros andares',
                'vasculhar': 'O lugar está escuro, vasculhar a área não deve te fazer mal'
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
    "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
    "na entrada do Insper, e quer procurar o professor para pedir um "
    "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        print()
        print(cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual['descricao'])
        print()
        for opcao, opcao1 in cenario_atual['opcoes'].items():
            print(opcao,':', opcao1)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            escolha=input('O que quer fazer agora? ')
            escolha=escolha.lower()
            escolha="".join(escolha.split())

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
