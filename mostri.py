'''
class Entity:
    def __init___(self, hp, x, y):
        self.hp = hp
        self.x = x
        self.y = y
    
    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -=1 
        
class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = 10
        self.damage = damage

    def info(self):
        print("Sono",self.name,"faccio",self.damage,"di danno e ho",self.hp,"punti vita su 10; e pi trovo a",self.x,self.y)
    
    def attack(self, enemy):
        if self.hp <= 0:
            print(self.name, "prova ad attaccare da morto con scarsi risultati")
        else: 
            print(self.name, "attacca", enemy.name)

        if (enemy.hp <= 0):
            print(enemy.name, "e' morto")
        else:
            enemy.hp -= self.damage

     
class Field:
    def _init_(self):
        self.h = h
        self.w = w
        
        
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                print("[]", end = "")
            else:
                print()
            
    
field1 = Field(10, 10)
field1.draw()

class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
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
m = Monster(3, 1, "Pikachu", 10, field)
m = Monster(1, 3, "Lapras", 10, field)
field.draw()
'''
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
    if direction == "up":
      self.y -= 1
    elif direction == "down":
      self.y += 1
    elif direction == "left":
      self.x -= 1
    elif direction == "right":
      self.x += 1

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
