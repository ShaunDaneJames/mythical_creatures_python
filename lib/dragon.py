class Dragon:
    def __init__(self, name, color, rider, hungry = True, satiety = 0):
        self.name = name
        self.color = color
        self.rider = rider
        self.hungry = hungry
        self.satiety = satiety

    def is_hungry(self):
        if self.satiety > 2:
            self.hungry = False
        return self.hungry

    def eat(self):
        self.satiety += 1
