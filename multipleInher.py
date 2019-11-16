class Employee:
    no_of_leves=8
    def __init__(self,name,roll,section):
        self.name=name
        self.roll=roll
        self.section=section

    def printdetails(self):
        return f"{self.name},{self.roll},{self.section}"

class player:
    no_of_leves=9
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printplayer(self):
        return f"{self.name},{self.game}"

class person(player,Employee):
    no_of_leves = 10


Harry=Employee("Harry",23,2)

# Harry=person("Harry","cricket")
# print(Harry.printplayer())
print(Harry.no_of_leves)