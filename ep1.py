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
        },
        'vasculhar': {
            'titulo': 'Vasculhar',
            'descricao': 'Você foi vasculhar e morreu!',
            'opcoes': {}
        },
        'andar1': {
            'titulo': '1º Andar',
            'descricao': 'Você está no primeiro andar',
            'opcoes': {
                'sala1': 'Entrar na sala do primeiro andar',
                'dani': 'Falar com a Dani, professora de GDE',
                'elevador': 'Pegar o elevador'
            }
        },
        'sala1': {
            'titulo': 'Sala 1',
            'descricao': 'Você entrou na sala 1 do primeiro andar, a sala está vazia, apenas o projetor ligado',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'dani': 'Falar com a Dani, professora de GDE'
            }
        },
        'dani': {
            'titulo': 'Dani: Professora de GDE',
            'descricao': 'Olá querido aluno! Ouvi rumores que o Toshi está no 3º andar',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'sala1': 'Entrar na sala 1'
            }
        },
        'andar2': {
            'titulo': '2º Andar',
            'descricao': 'Você está no segundo andar, o lugar está movimentado e você avistou a Paulina!',
            'opcoes': {
                'sala2': 'Entrar na sala 2',
                'paulina': 'Falar com a professora de ModSim, Paulina!',
                'elevador': 'Pegar o elevador'
            }
        },
        'sala2': {
            'titulo': 'Sala 2',
            'descricao': 'Você entrou na sala 2 e avistou um objeto no chão do fundo da sala, pegou e descobriu que era um documento do Toshi e resolveu guardar',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'paulina': 'Ir falar com a paulina'
            }
        },
        'paulina': {
            'titulo': 'Paulina: Professora de ModSim',
            'descricao': 'Você foi falar com a Paulina, ela te lembrou do Exercício 3, a entrega está chegando! Você rebateu e disse: Eu já acabei! E perguntou por Toshi, ela disse que viu ele entrando no banheiro agora há pouco!',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'banheiro': 'Procurar por Toshi no banheiro',
                'sala2': 'Entrar na sala 2'
            }
        },
        'banheiro': {
            'titulo': 'Banheiro',
            'descricao': 'Você entrou no banheiro a procura de Toshi, ele não aparenta estar aqui!',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'sala2': 'Entrar na sala 2'
            }
        },
        'andar3': {
            'titulo': '3º Andar',
            'descricao': 'Você chega no terceiro andar e avista o Fábio, professor de InstruMed!',
            'opcoes': {
                'sala3': 'Entrar na sala 3',
                'fabio': 'Falar com Fábio',
                'elevador': 'Pegar o elevador'
            }
        },
        'sala3': {
            'titulo': 'Sala 3',
            'descricao': 'Você entra na sala 3 e vê que está tudo apagado!',
            'opcoes': {
                'vasculhar': 'Vasculhar a sala',
                'fabio': 'Falar com fabio',
                'elevador': 'Pegar o elevador'
            }
        },
        'fabio': {
            'titulo': 'Fábio: Professor de InstruMed',
            'descricao': 'Você foi falar com Fábio sobre Toshi, afirmando que viram ele aqui, ele disse que não o viu por aqui, mas disse que a sala dele fica no 5 andar!',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'sala3': 'Ir para a sala 3'
            }
        },
        'andar4': {
            'titulo': '4º Andar',
            'descricao': 'Você chegou ao quarto andar e avistou o Durão, professor de NatDes',
            'opcoes': {
                'elevador': 'Pegar o elevador',
                'durao': 'Falar com Durão',
                'laboratorio': 'Entrar no laboratório de InstruMed'
            }
        },
        
        
            
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
            print("\nAcabaram-se suas opções! Mwo mwo mwooooo...")
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
