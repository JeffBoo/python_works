
class Weapon:
    def __init__(self, name, damage_value):
        self.name = name
        self.damage_value = damage_value

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage_value