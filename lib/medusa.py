class Medusa:
    def __init__(self, name):
        self.name = name
        self.statues = []

    def stare(self, victim):
        self.statues.append(victim)
        victim.stoned = True
        if len(self.statues) > 3:
            person = self.statues.pop(0)
            person.stoned = False