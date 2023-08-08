class Character:

    def __init__(self, x, y, velocity, power):

        self.x = x
        self.y = y
        self.velocity = velocity
        self.power = power

    def move(self, delta_x, delta_y):

        self.x = max(min(self.x + delta_x, 98), 1)  # plansza 100 x 100, odrzucone skrajne wartości (0 i 99)
        self.y = max(min(self.y + delta_y, 98), 1)
