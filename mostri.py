class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)
  
  def move(self, direction):
    casella_vuota = True
    if direction == "up" and self.y >= 1:
      for e in field.entities:
        if self.x == e.x and self.y-1 == e.y:
          casella_vuota = False
          print("La casella è occupata")      
      if casella_vuota:
        self.y -= 1
    
    elif direction == "down" and self.y <= field.h-2:
      for e in field.entities:
        if self.x == e.x and self.y+1 == e.y:
          casella_vuota = False      
          print("La casella è occupata")
      if casella_vuota:
        self.y += 1
    
    elif direction == "left" and self.x >= 1:
      for e in field.entities:
        if self.x-1 == e.x and self.y == e.y:
          casella_vuota = False
          print("La casella è occupata")      
      if casella_vuota:
        self.x -= 1
    
    elif direction == "right" and self.x <= field.w-2:
      for e in field.entities:
        if self.x+1 == e.x and self.y == e.y:
          casella_vuota = False
          print("La casella è occupata")      
      if casella_vuota:
        self.x += 1
    
    else:
      print("Il mostro",self.name,"tenta invano di uscire dall'arena.")

      
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
m1.info()
m1.move("up")
field.draw()
m2.info()
m1.move("left")
field.draw()

