class Wizard:
    def __init__(self, name, bearded = True):
        self.name = name
        self.bearded = bearded
        self.rested = True
        self.mana = 3

    def is_bearded(self):
        return self.bearded

    def incantation(self, spell):
        return "sudo " + spell

    def is_rested(self):
        return self.rested

    def cast(self):
        if self.mana > 1:
            self.mana -= 1
            return "MAGIC MISSILE!"
        else:
            self.rested = False
            return "Out Of Mana!"