class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount


# Create two heroes
Arthur = Hero("Arthur", 100)
Morgana = Hero("Morgana", 100)

# Arthur takes 10 damage
Arthur.take_damage(10)

# Print their HP
print(Arthur.name, "HP:", Arthur.hp)
print(Morgana.name, "HP:", Morgana.hp)
