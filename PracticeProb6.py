class Player:
    def playtime(self,name):

        print(f"player {name} is playing now")
        import random
        ls1 = [2, 3, 5, 7]
        num = random.choice(ls1)
        print(num)
        self.count=0

        while True:
            n = int(input("Enter the number"))
            if num == n:
                print("You guess right number. you wins!")
                break

            elif num > n:
                print("Please enter greater number : ")

            else:
                print("Please enter small number : ")

            self.count += 1
            continue

        print(f"{name} you guess in {self.count} step \n")


player1=Player()
player1.playtime("khushi")

player2=Player()
player2.playtime("Priya")

if player1.count < player2.count:
    print("player 1 wins the match!")

else:
    print("Player 2 wins the match!")