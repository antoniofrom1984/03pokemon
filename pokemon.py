class Pokemon:
    def __init__(self, name, level, the_type):
        self.name = name
        self.level = level
        self.health = level 
        self.max_health = level
        self.the_type = the_type
        self.is_knocked_out = False
    # def __repr__(self):
    #     # Printing a pokemon will tell you its name, its type, its level and how much health it has remaining
    #     return "This level {level} {name} has {health} hit points remaining. They are a {the_type} type Pokemon".format(level = self.level, name = self.name, health=self.health, type = self.the_type)

    def __repr__(self):
        print('name: {name}'.format(name= self.name))
        # return {"name":self.name, 
        #         "level":self.level,
        #         "type": self.the_type,
        #         "health": self.health,
        #         "max Health": self.max_health,
        #         "alive": self.is_knocked_out
        #         }
    
    def gain_helth(self, amount):
        self.health += amount
        print("{name} won {amount} of health!")
        print("You have {health} to carry on")
    
    def lose_health(self, amount):
        self.health -= amount
        print("{name} lost {amount} of health!")
        print("You have {health} left.")
        if self.health == 0:
            self.knockedOut()

    def knockedOut(self):
        self.is_knocked_out = True
        print("{name} Died!")
    
    def revive(self):
        self.is_knocked_out = True
        self.health = self.max_health / 2
        print("{name} has revived!")

    # def attack(self, pokemon):


p = Pokemon("Bubu",10,"fire")

print(p.__repr__())
#step 3: lose_health, knowckout, revive, gain_health, experience

#step4 type attacks