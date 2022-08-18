


class Player:

    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self):
        d = self.damage

        enemy.protection(d)

    def protection(self, d):
        h = self.health
        a = self.armor

        h -= d - a

        self.health = h

    def ex_health(self):
        if self.health < 0:
            return True
        else:
            return False


class Enemy:

    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self):
        d = self.damage

        player.protection(d)
    
    def protection(self, d):
        h = self.health 
        a = self.armor        

        h -= d - a

        self.health = h

    def ex_health(self):
        if self.health < 0:
            return True
        else:
            return False

player = Player(100, 45, 15)
enemy = Enemy(100, 45, 15)

x = 1

class Game:

    def ex_game():
        if player.ex_health() == True:
            return 'Enemy win'
        elif enemy.ex_health() == True:
            return 'Player win'
        else:
            return True

    def game():
        global x
            
        ex = game.ex_game()
        
        if ex == True:
            
            if x == 1:
                player.attack()
                x -= 1
            else:
                enemy.attack()
                x += 1
            return True
        else:
            return ex 

game = Game

g = game.game()

while g == True:
    g = game.game()

print(g)

