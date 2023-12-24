
class Unit:
    def __init__(self,name,health):
        self.name = name
        self.health = health
class Soldier(Unit):
    def __init__(self,name,health,attack_power):
        self.attack_power = attack_power
        super().__init__(name,health)
    def attack(self,unit):
        unit.health -= self.attack_power
class Archer(Unit):
    def __init__(self,name,health,range_attack_power):
        self.range_attack_power = range_attack_power
        super().__init__(self,name,health)
    def attack(self,unit):
        unit.health -= self.range_attack_power
big_warior = Soldier("Big Boy",200,50)
little_archer = Archer("Little Boy",120,70)

