class Dad:
    Basketball=1
    RainDance=2

class Son(Dad):
    Dance=1
    Basketball = 3
    def This_is_str(self):
        return f"str"

    def printdance(self):
        return f"This is {self.Dance}"

class Grandson(Son):
    Dance = 6
    def printdance(self):
        return f"This is {self.Dance}"

Darry=Dad()
Sarry=Son()
Garry=Grandson()

print(Garry.printdance())
print(Garry.Basketball)
print(Garry.RainDance)
print(Garry.This_is_str())