# Nome completo do primeiro membro: Roger Honorato
# RA do primeiro membro: 247617
# Nome completo do segundo membro: [Segundo membro da equipe]
# RA do segundo membro: [Segundo membro da equipe]

'''
Implemente aqui a sua estratégia de ataque e a posição dos navios.
A estratégia de ataque deve ser implementada no método "jogar" e a posição dos navios no método "posicoes_navios".
A posição dos navios deve ser uma lista de objetos do tipo Navio, onde cada objeto contém o tamanho do navio e suas coordenadas.
A lista de navios deve conter todos os 5 navios, ou seja, um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.

Observações:
- O tamanho dos navios é definido na constante NAVIOS, que é um dicionário onde cada chave é o nomes do navios e cada valor é o respectivo tamanho do navio.
- O tamanho do tabuleiro é definido na constante TABULEIRO_TAMANHO, que é um inteiro.
- O valor DESCONHECIDO representa uma posição vazia no tabuleiro.
- O valor NAVIO_ENCONTRADO representa uma posição onde um navio foi encontrado.
- O valor NAVIO_INTEIRO_ATINGIDO representa uma posição onde um navio foi atingido (todas as posições encontradas).
- Você pode consultar (mas não modificar) o arquivo constants.py para mais informações sobre os valores das constantes.
- Mais informações podem ser encontradas na documentação do projeto (arquivo README.md).'''

from constants import TABULEIRO_TAMANHO, NAVIOS, StatusTab
from classes._attack import Ataque
from classes._ship import Navio
from classes._pos_matriz import PosMatriz


global navios_encontrados
global disparos
global computado
navios_encontrados = dict()
disparos = [0]  # define em qual diagonal estamos disparando (x + y)
computado = []  # coordenadas que ja foram detectadas no radar


def radar(status, nome, afundados, x, y):
    if status == StatusTab.NAVIO_ENCONTRADO.value:
        if nome not in navios_encontrados and nome not in afundados:
            navios_encontrados[nome] = [[x, y]]
            computado.append([x, y])

        elif [x, y] not in computado:
            navios_encontrados[nome] += [[x, y]]
            computado.append([x, y])


class AlunoPlayer():
    """Classe que representa o jogador bot do aluno."""

    def __init__(self):
        """Inicializa o jogador.

        Atributos:
        movimentos_realizados -- Lista de movimentos já realizados pelo jogador.
        tabuleiro -- Tabuleiro do jogador (inicializado automaticamente assim que o jogo começa).
        nome -- Nome da equipe.
        """
        self.movimentos_realizados = list()
        self.tabuleiro = None           # o tabuleiro é inicializado automaticamente assim que o jogo começa
        self.nome = "garotos de programa"
        self.shoot = 0

    def jogar(self, estado_atual_oponente, navios_afundados) -> Ataque:
        """Método para realizar uma jogada.

        Parâmetros:
        estado_atual_oponente -- O estado atual do tabuleiro.
        navios_afundados -- Lista de nomes navios afundados (em ordem de afundamento).

        Retorna um objeto do tipo Ataque com as coordenadas (x,y) da jogada.
        """

        for x in range(10):
            for y in range(10):

                if [x, y] in self.movimentos_realizados:

                    radar(estado_atual_oponente[x][y].status, estado_atual_oponente[x][y].nome_navio_atingido, navios_afundados, x, y)

                    # tenta afundar barcos ja encontrados
                    for key, value in navios_encontrados.items():
                        if key not in navios_afundados:
                            for coords in value:
                                x1, y1 = coords[0], coords[1]

                                # direita
                                if [x1, y1 + 1] not in self.movimentos_realizados and y1 + 1 <= 9:
                                    self.movimentos_realizados.append([x1, y1 + 1])
                                    return Ataque(x1, y1 + 1)

                                # esquerda
                                if [x1, y1 - 1] not in self.movimentos_realizados and y1 - 1 >= 0:
                                    self.movimentos_realizados.append([x1, y1 - 1])
                                    return Ataque(x1, y1 - 1)

                                # baixo
                                if [x1 - 1, y1] not in self.movimentos_realizados and x1 - 1 >= 0:
                                    self.movimentos_realizados.append([x1 - 1, y1])
                                    return Ataque(x1 - 1, y1)

                                # cima
                                if [x1 + 1, y1] not in self.movimentos_realizados and x1 + 1 <= 9:
                                    self.movimentos_realizados.append([x1 + 1, y1])
                                    return Ataque(x1 + 1, y1)

                # atira em uma linha diagonal
                elif x + y == (disparos[-1] + 1):
                    self.movimentos_realizados.append([x, y])

                    if x == 9 or y == 0 or x == x + y:
                        disparos.append((x + y) + 1)
                    return Ataque(x, y)
        disparos.append(disparos[-1] + 2)
        return Ataque(7, 8)

    def posicoes_navios(self) -> list[Navio]:
        """Determina as posições dos 5 navios no tabuleiro e retorna uma lista de objetos do tipo Navio.

        É preciso determinar as posições de TODOS os 5 navios, ou seja,
        um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.
        O nome do navio será determinado automaticamente pelo tamanho do navio dentro da classe Navio."""

        carrier_5 = Navio(5, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
        battleship_4 = Navio(4, [(9, 9), (9, 8), (9, 7), (9, 6)])
        cruiser_3 = Navio(3, [(3, 3), (3, 4), (3, 5)])
        submarine_3 = Navio(3, [(4, 6), (5, 6), (6, 6)])
        destroyer_2 = Navio(2, [(5, 2), (5, 3)])

        navios = [carrier_5, battleship_4, cruiser_3, submarine_3, destroyer_2]
        return navios

# [0, 0][0, 1][0, 2][0, 3][0, 4][0, 5][0, 6][0, 7][0, 8][0, 9]
# [1, 0][1, 1][1, 2][1, 3][1, 4][1, 5][1, 6][1, 7][1, 8][1, 9]
# [2, 0][2, 1][2, 2][2, 3][2, 4][2, 5][2, 6][2, 7][2, 8][2, 9]
# [3, 0][3, 1][3, 2][3, 3][3, 4][3, 5][3, 6][3, 7][3, 8][3, 9]
# [4, 0][4, 1][4, 2][4, 3][4, 4][4, 5][4, 6][4, 7][4, 8][4, 9]
# [5, 0][5, 1][5, 2][5, 3][5, 4][5, 5][5, 6][5, 7][5, 8][5, 9]
# [6, 0][6, 1][6, 2][6, 3][6, 4][6, 5][6, 6][6, 7][6, 8][6, 9]
# [7, 0][7, 1][7, 2][7, 3][7, 4][7, 5][7, 6][7,7 ][7, 8][7, 9]
# [8, 0][8, 1][8, 2][8, 3][8, 4][8, 5][8, 6][8, 7][8, 8][8, 9]
# [9, 0][9, 1][9, 2][9, 3][9, 4][9, 5][9, 6][9, 7][9, 8][9, 9]
