
class Pokemon:
    def __init__(self, name, level, the_type):
        self.name = name
        self.level = level
        self.health = level 
        self.max_health = level
        self.the_type = the_type
        self.is_knocked_out = False
        self.experience = 0
        
    def __repr__(self):
        # Make class Readable 
        return " {name} , is a level {level} with {health} hit points remaining, It's a {type} type Pokemon.".format(level = self.level, name = self.name, health=self.health, type = self.the_type)

    def gain_health(self, amount):
        self.health += amount
        print("{name} won {amount} of health! \n You have {health} to carry on".format(level = self.level, name = self.name, health=self.health, type = self.the_type))

    def cosmetic(self,type):
        #give colors to the terminal according to pokemon type
        global reset
        reset = " \u001b[0m"
        
        if type == "Grass":
            return "\u001b[48;5;28m "
        elif type == "Fire":
            return "\u001b[48;5;88m "
        elif type == "Water":
            return "\u001b[48;5;24m "

    def lose_health(self, amount):
        self.health -= amount
        color = self.cosmetic(self.the_type)
        #make sure health is not a negative number
        if self.health <= 0:    
            self.health = 0
        #make sure we know the point before we know if it's dead
        print(color + str(self.name) + " lost " + str(amount) + " health points!" +  "It has " + str(self.health) + " left."+reset)
        #make sure it dies if health hist 0
        if self.health <= 0: 
            self.knockedOut()

    def knockedOut(self):
        color = self.cosmetic(self.the_type)
        self.is_knocked_out = True
        print(color + self.name + " Sadly died!"+ reset)
    
    def revive(self):
        color = self.cosmetic(self.the_type)
        self.is_knocked_out = False
        self.health = self.max_health / 2
        print(color + self.name + " has revived!"+ reset)

    def theExperience(self):
        color = self.cosmetic(self.the_type)
        self.experience += 1
        print(color + self.name + " gained experience. Has "+ str(self.experience) + " in total!" + reset)
    
    def attack(self, pokemon):
        color1 = self.cosmetic(self.the_type)
        color2 = pokemon.cosmetic(pokemon.the_type)
        waterFire = self.the_type == "Water" and pokemon.the_type == "Fire"
        fireGrass =  self.the_type == "Fire" and pokemon.the_type == "Grass"
        grassWater = self.the_type == "Grass" and pokemon.the_type == "Water"

        # atacked and attacker gain experience  after the attack 
        self.theExperience()
        pokemon.theExperience()

        # check if its dead before it attacks
        if self.is_knocked_out == True:
            print(color1  + self.name+"  is dead! It can't attack " + pokemon.name + reset + "\n")
            return

        print("\n" + color1  + self.name + " attacked " + pokemon.name + reset + "\n")

        if waterFire or fireGrass or grassWater:
            pokemon.lose_health(5)
            print(color1 + "Super effective attack, " + pokemon.name + " lost 5 points of it's health" + reset)
        else:
            pokemon.lose_health(2.5)
            print(color1 + "Somewhat effective attack, " + pokemon.name + " lost 2.5 health points" + reset)
        
        if pokemon.is_knocked_out == True:
            print(color2  + self.name+" killed " + pokemon.name + reset)
        
        print("\n \u001b[48;5;28m  \u001b[48;5;88m  \u001b[48;5;24m "+ reset + "\n")




a = Pokemon("Bubu",5,"Grass")
b = Pokemon("PuPu",5,"Fire")
c = Pokemon("Coocoo",5,"Water")

# a.attack(b)
# b.attack(c)
# c.attack(a)
# b.attack(a)
# c.attack(b)
# a.attack(c)

class PuPu(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Pupu", "Fire", level)

class Coocoo(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Coocoo", "Water", level)

class Bubu(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bubu", "Grass", level)


class Trainer:
    def __init__(self, nPokemons,  nPotions, name):
        self.nPokemons = nPokemons
        self.name = name
        self.nPotions = nPotions
        self.currentPok = 0

    def __repr__(self):
        # Make class Readable 
        print("\n\u001b[40;1m The trainer {name} has the following pokemon: \u001b[0m".format(name = self.name))
        for pokemon in self.nPokemons:
            color1 = pokemon.cosmetic(pokemon.the_type)
            print(color1,pokemon,reset)
        return "The current active pokemon is {name}".format(name = self.nPokemons[self.currentPok].name)

    def usePotion(self):
        if self.nPotions <= 0:
            print("You don't have any potions left")
            return
        else:
            print("Trainer used potion on current Pokemon")
            self.nPokemons[self.currentPok].revive()
            # print(self.nPokemons[self.currentPok].name + " has revived")
    
    def attackTrainer(self, otherTrainer):
        
        me = self.nPokemons[self.currentPok]
        other = otherTrainer.nPokemons[otherTrainer.currentPok]
        print("Trainer " + self.name + " attaked trainer " + otherTrainer.name + ". " + str(me.name) + " attacks " + str(other.name) + ". ")
        me.attack(other)
    
    def selectPokemon(self, selection):
        self.currentPok = selection
        print("The current active pokemon is {name}".format(name = self.nPokemons[self.currentPok].name))


trainerOne = Trainer([a,b,c], 6, "antonio")
trainerTwo = Trainer([b,c,a], 6, "pedro")



print(trainerOne)
# trainerOne.selectPokemon(1)


trainerOne.attackTrainer(trainerTwo)
trainerTwo.attackTrainer(trainerOne)
trainerTwo.usePotion()
trainerOne.attackTrainer(trainerTwo)
trainerTwo.selectPokemon(0)
trainerTwo.selectPokemon(1)