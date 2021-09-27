
class Player:
    def __init__(self, pseudo, health, attack, weapon):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage_value):
        self.health -= damage_value

    def attack_player(self, target_player):
        target_player.damage(self.attack)

        # si le joueur a une arme
        if self.has_weapon():
            # ajoute les dégats de l'arme au point d'attaque du joueur
            damage_value += self.weapon.get_damage_amount()

        target_player.damage(damage_value)

        # méthode pour changer l'arme du joueur

    def set_weapon(self, weapon):
        self.weapon = weapon

        # méthode pour verifier si le joueur a une arme

    def has_weapon(self):
        return self.weapon is not None