print("Jogo está iniciando...")

from player import Player
from monster import Monster
from grid import Grid

class Game:
    def __init__(self, grid_size=5, max_turns=10, difficulty="medium"):
        """
        Inicializa o jogo com a grade, jogador, monstro e o número máximo de turnos.
        A dificuldade afeta o número de turnos e quando o monstro pode escapar.
        """
        self.grid_size = grid_size
        self.grid = Grid(self.grid_size)
        self.player = Player()
        self.monster = Monster(self.grid_size)
        
        # Configurações de dificuldade ajustam o número de turnos e tempo de escapada do monstro
        self.set_difficulty(difficulty, max_turns)

    def set_difficulty(self, difficulty, max_turns):
        """
        Ajusta o número de turnos e o tempo de escapada do monstro com base na dificuldade.
        """
        if difficulty == "easy":
            self.turns_left = max_turns + 5  # Mais turnos no modo fácil
            self.escape_turn = int(self.turns_left / 2) + 3  # O monstro demora mais para escapar
        elif difficulty == "hard":
            self.turns_left = max_turns - 2  # Menos turnos no modo difícil
            self.escape_turn = int(self.turns_left / 2) - 1  # O monstro escapa mais rápido
        else:
            self.turns_left = max_turns  # Configuração padrão (modo médio)
            self.escape_turn = int(self.turns_left / 2)

    def play(self):
        """
        Inicia o loop principal do jogo.
        O jogador faz tentativas, e o monstro se move após cada tentativa errada.
        """
        print(f"Bem-vindo ao Caça ao Monstro! Tente capturar o monstro em até {self.turns_left} tentativas.")
        print("Dica: O monstro pode tentar escapar após metade dos turnos!\n")

        while self.turns_left > 0:
            guess = self.get_player_guess()

            if self.check_capture(guess):
                print("Parabéns! Você capturou o monstro!")
                break

            self.give_feedback(self.calculate_distance(guess, self.monster.position))

            # O monstro se move após cada tentativa falha
            self.monster.move(self.grid_size)

            # Reduz o número de tentativas restantes
            self.turns_left -= 1
            print(f"Tentativas restantes: {self.turns_left}\n")

            if self.turns_left == 0:
                print("Você perdeu! O monstro escapou.\n")

    def get_player_guess(self):
        """
        Obtém a tentativa do jogador e garante que ela esteja dentro dos limites da grade.
        """
        while True:
            guess = self.player.guess_position()
            if self.player.validate_guess(guess[0], guess[1], self.grid_size):
                return guess
            print("Tentativa fora dos limites. Tente novamente.\n")

    def check_capture(self, player_pos: tuple) -> bool:
        """
        Verifica se o jogador capturou o monstro.
        """
        return player_pos == self.monster.position

    def calculate_distance(self, player_pos: tuple, monster_pos: tuple) -> int:
        """
        Calcula a distância Manhattan entre o jogador e o monstro.
        """
        return abs(player_pos[0] - monster_pos[0]) + abs(player_pos[1] - monster_pos[1])

    def give_feedback(self, distance: int):
        """
        Fornece feedback ao jogador sobre a proximidade do monstro.
        Quanto menor a distância, mais perto o jogador está.
        """
        feedback_messages = {
            0: "Você capturou o monstro!",
            1: "Você está muito perto! Continue atento!",
            2: "Você está perto! O monstro está a uma curta distância!",
            3: "Você está no caminho certo, o monstro está relativamente próximo.",
            4: "Você está no caminho certo, o monstro está relativamente próximo.",
            5: "Você está se afastando, o monstro está um pouco mais longe.",
            6: "Você está se afastando, o monstro está um pouco mais longe.",
        }

        # Escolher a mensagem com base na distância
        print(feedback_messages.get(distance, "Você está muito longe! O monstro está longe de sua posição atual."))


# Iniciar o jogo com escolha de dificuldade e tamanho da grade
if __name__ == "__main__":
    print("Escolha a dificuldade: fácil, médio ou difícil")
    difficulty = input("Digite a dificuldade desejada: ").lower()

    print("Escolha o tamanho da grade (mínimo 3x3, máximo 10x10):")
    grid_size = int(input("Digite o tamanho da grade: "))
    grid_size = max(3, min(grid_size, 10))  # Limita a grade entre 3 e 10

    jogo = Game(grid_size=grid_size, difficulty=difficulty)
    jogo.play()
