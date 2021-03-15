class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)
    
class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name
    self.hp = 10
    self.damage = damage

  def info(self):
    print("Sono", self.name, "ho ", self.hp, "/10 hp", "e mi trovo a", self.x, ",", self.y)

  def attack(self, enemy):
        if self.hp <= 0:
            print("Il fantasma di", self.name, "prova ad attaccare invano.")
        else: 
            print(self.name, "attacca", enemy.name)

        if (enemy.hp <= 0):
            print(enemy.name, "e' morto.")
        else:
            enemy.hp -= self.damage

def move(self, direction):
    if direction == "up" and self.y >= 1:
      self.y -= 1
    elif direction == "down" and self.y <= 10:
      self.y += 1
    elif direction == "left" and self.x >= 1:
      self.x -= 1
    elif direction == "right" and self.x <= 10:
      self.x += 1
    else:
        print("Il mostro",self.name,"tenta invano di uscire dall'arena.")
        
class Field:
  def __init__(self):
    self.w= 10
    self.h = 10
    self.entities = []

  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[x]", end = "")
            break    
        else:
          print("[ ]", end = "")
      print()

field = Field()
m1 = Monster(2, 2, "Bulbasaur", 2, field)
m2 = Monster(1, 1, "Charmander", 2, field)
m1.info()
m2.info()
field.draw()
m1.attack(m2)
m2.info()
m1.move("up")
field.draw()
m2.attack(m1)
m1.info()
m2.move("down")
m2.move("left")
field.draw()
m1.attack(m2)
m2.info()
m2.attack(m1)
m1.info()
m1.attack(m2)
m2.info
m2.attack(m1)
m1.info()
