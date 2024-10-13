class Grid:
    def __init__(self, size: int):
        """Inicializa a grade de tamanho size x size."""
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def is_valid_position(self, x: int, y: int) -> bool:
        """Verifica se a posição (x, y) está dentro dos limites da grade."""
        return 0 <= x < self.size and 0 <= y < self.size

    def update_positions(self, player_pos: tuple, monster_pos: tuple):
        """Atualiza as posições do jogador e do monstro na grade."""
        # Essa função pode ser expandida se quisermos "desenhar" a grade
        pass

    def display(self):
        """Exibe a grade (opcional, para debugging)."""
        pass
