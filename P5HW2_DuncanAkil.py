# Random math quiz generator
# April 16, 2022
# CTI-110 P5HW2 - Math Quiz
# Akil Duncan
#

import random

def addRandom():
        n1=random.randint(0,1000)
        n2=random.randint(0,1000)
        print(f"{n1:>6}")
        print(f"+{n2:>5}")
        print("Enter answer")
        ans=int(input())
        while ans!=n1+n2:
        
                
                if ans<n1+n2:
                        print("Sorry, your guess was too low.")
                else:
                        print("Sorry, your guess was too high.")

                ans=int(input("Please try again : "))
        print("Congratulations! Your answer is correct!")

def subRandom():
        n1=random.randint(0,1000)
        n2=random.randint(0,1000)
        print(f"{n1:>6}")
        print(f"-{n2:>5}")
        print("Enter answer")
        ans=int(input())
        while ans!=n1-n2:
        
                
                if ans<n1-n2:
                        print("Sorry, your guess was too low.")
                else:
                        print("Sorry, your guess was too high.")
                ans=int(input("Please try again : "))
        print("Congratulations! Your answer is correct!")
if __name__=="__main__":

        while 1:

                print("MAIN MENU")
                print("----------------------")
                print("1) Add Random Numbers ")
                print("2) Subtract Random Numbers")
                print("3) Exit")
                num=int(input("Please choose one of the options: "))
                if num==3:
                        print("Thank you for playing!")
                        print("Bye!")
                        break
                if num==1:
                        addRandom()
                if num==2:
                        subRandom()
