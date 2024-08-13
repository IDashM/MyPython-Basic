
class Enemy:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.armor = 0
        self.attack = 0

    def Mouse(self):
        self.name = "Mouse"
        self.hp = 5
        self.armor = 2
        self.attack = 1

    def Ant(self):
        self.name = "Ant"
        self.hp = 3
        self.armor = 0
        self.attack = 1

class HERO:
    def __init__(self):
        self.name = ""
        self.hp = 5
        self.attack = 2
        self.armor = 1
        self.experience = 0.0

    def outputattribute():
        print("HERO : " + newname)
        print("1. Battle\n2. Attribute\n 3. History")
     
    def change_name(self,new_name):
        self.name = new_name

    def change_hp(self,new_name):
        self.hp = new_name

    def change_armor(self,new_name):
        self.armor = new_name

    def change_experience(self,new_name):
        self.experience = new_name

    def change_attack(self,new_name):
        self.attack = new_name


class Battle:
    def __init__(self):
        pass

heroname = input("HELLO HERO WHAT IS YOUR NAME ? : ")
newname = Enemy.change_name(heroname)

print("Hello Hero "+ newname)

while True:
    HERO.outputattribute()
    select = input("Choose :")
    if select == 1:
        print("You chose Battle")
    elif select == "2":
        print("You chose Attribute")
    elif select == "3":
        print("You chose History")
    elif select == "quit":
        print("Goodbye, Hero!")
        break 
    else:
        print("Invalid choice")
  
