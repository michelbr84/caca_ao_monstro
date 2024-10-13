import random

class Monster:
    def __init__(self, grid_size: int):
        """Inicializa o monstro em uma posição aleatória na grade."""
        self.position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    def move_random(self, grid_size: int) -> tuple:
        """Move o monstro para uma nova posição aleatória na grade."""
        self.position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        return self.position
