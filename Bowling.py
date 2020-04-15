"""
Name: BBowling Game Coding Exercise
Authors: Laurie Jones

given an integer array of a valid sequence of self.throws for one game of 
American Ten-Pin Bowling, produces the total score for the game

"""


class Bowling():

    def __init__(self, throws):
        self.throws = throws
        self.total = 0
        self.ptr = iter(self.throws)
        

    def findTotal(self):
        num = 0

        for i in range(len(self.throws)):

            if self.throws[i] == "-":
                self.total = self.total + 0

            elif self.throws[i] == "/":

                #adds up to 10
                prev = i - 1
                first = self.throws[prev]
                print("first", first)
                adder = 10 - int(first)
                self.total = self.total + adder

                #includes the next value
                spare = int(self.next(i))
                self.total = self.total + int(spare)

            elif self.throws[i] == "X":
                self.total = self.total + 10
                num = int(self.next(i)) #+ int(self.ex(i+2))
                print("num",num)
                self.total = self.total + int(num)
                
            else:
                integer = int(self.throws[i])
                self.total = self.total + integer
                #print(self.total)

            print("number", self.throws[i])
            print("runningtotal",self.total)

        return print(self.total)


    #accepts the position of X 
    def next(self, position):
        number = 0 

        #skips to next number  
        position = position + 1

        if self.throws[position] == "-":
            position = position + 1

        if self.throws[position] == "/":
            prev = position -1

            first = self.throws[prev]
            print("first", first)


            adder = 10 - first
            number = adder


        if self.throws[position] == "X":
            number = 10

        else: 
            number = self.throws[position]

        return number
        



    # def spare(self, position):
    #     print("spare")

    #     if self.throws[position] == "-":
    #         position = position +1

    #     if self.throws[position] == "X":
    #         return 10 + int(self.ex(position + 1))
        
    #     else: 
    #         return self.throws[position+1]




            
        
           
           


def main():
    #throws = input("Enter your throws for your game: ")
    throws = "23-5/-44"
    b = Bowling(throws)
    b.findTotal()
    print("should be 27 ")


if __name__ == "__main__":
   main()