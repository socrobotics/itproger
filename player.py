from variants import Variants


class Player:
    name = ""
    choice = 0

    def __init__(self, choice=Variants.PAPER, name="Валера"):
        self.name = name
        self.choice = choice

    def whoWins(self, name, choice):
        self.name = name
        self.choice = choice

        if self.choice != choice:
            return f'Победил {self.name}'
        else:
            return 'Ничья'