class Player:
    def __init__(self):
        """Inicializa o jogador sem posição (vai adivinhar as posições)."""
        pass

    def guess_position(self) -> tuple:
        """Recebe as coordenadas do jogador."""
        x = int(input("Digite a linha: "))
        y = int(input("Digite a coluna: "))
        return (x, y)

    def validate_guess(self, x: int, y: int, grid_size: int) -> bool:
        """Valida se a tentativa está dentro dos limites da grade."""
        return 0 <= x < grid_size and 0 <= y < grid_size
