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
        self.nome = "{Computeiros}"  # substitua!


    def jogar(self, estado_atual_oponente, navios_afundados) -> Ataque:
        """Método para realizar uma jogada.

        Parâmetros:
        estado_atual_oponente -- O estado atual do tabuleiro.
        navios_afundados -- Lista de nomes navios afundados (em ordem de afundamento).

        Retorna um objeto do tipo Ataque com as coordenadas (x,y) da jogada.
        """
        
        for x in range(10):
            if x % 2 == 0:
                for y in range(10):
                    if y % 2 == 0:
                        continue
                    if [x,y] not in self.movimentos_realizados:
                            self.movimentos_realizados.append([x, y])
                            return Ataque(x, y)
            else:
                for y in range(10):
                    if y % 2 != 0:
                        continue
                    if [x,y] not in self.movimentos_realizados:
                        self.movimentos_realizados.append([x,y])
                        return Ataque(x,y)


    def posicoes_navios(self) -> list[Navio]:
        """Determina as posições dos 5 navios no tabuleiro e retorna uma lista de objetos do tipo Navio.
        
        É preciso determinar as posições de TODOS os 5 navios, ou seja,
        um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.
        O nome do navio será determinado automaticamente pelo tamanho do navio dentro da classe Navio."""

        carrier_5 = Navio(5, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
        
        battleship_4 = Navio(4, [(9, 9), (9, 8), (9, 7), (9, 6)])

        cruiser_3 = Navio(3, [(3, 3), (3, 4), (3, 5)])

        submarine_3 = Navio(3, [(4, 4), (5, 4), (6, 4)])

        destroyer_2 = Navio(2, [(5, 2), (5, 3)])

        navios = [carrier_5, battleship_4, cruiser_3, submarine_3, destroyer_2]
        return navios