class Game:
    def __init__(self):
        """Inicializa os componentes do jogo."""
        self.grid_size = 5
        self.grid = Grid(self.grid_size)
        self.player = Player()
        self.monster = Monster(self.grid_size)
        self.turns = 10  # Número máximo de turnos/tentativas

    def play(self):
        """Controla o loop principal do jogo."""
        while self.turns > 0:
            player_guess = self.player.guess_position()
            
            if not self.grid.is_valid_position(*player_guess):
                print("Coordenadas inválidas. Tente novamente.")
                continue

            if self.check_victory(player_guess, self.monster.position):
                print("Você capturou o monstro!")
                break

            # O monstro se move
            self.monster.move_random(self.grid_size)

            self.turns -= 1
            print(f"Você tem {self.turns} tentativas restantes.")

        if self.turns == 0:
            print("Você perdeu! O monstro escapou.")

    def check_victory(self, player_pos: tuple, monster_pos: tuple) -> bool:
        """Verifica se o jogador capturou o monstro."""
        return player_pos == monster_pos
