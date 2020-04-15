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
        
    #iterate through the input
    def findTotal(self):
        num = 0


        for i in range(len(self.throws)):

            if self.throws[i] == "-":
                self.total = self.total + 0

        #if its a / 
        #either subtract the last number and add 10
            elif self.throws[i] == "/": 
                self.total = self.total + 10


        #if its a X then add 10 to the total
        #plus the total pins knocked down on the next two self.throws.
            elif self.throws[i] == "X":
                self.total = self.total + 10
                num = int(self.ex(i+1)) + int(self.ex(i+2))
                print("num",num)
                self.total = self.total + int(num)
                
                
        #add up the numbers  
            else:
                integer = int(self.throws[i])
                self.total = self.total + integer
                #print(self.total)

            #print("j",j)
            print("number", self.throws[i])
            print("runningtotal",self.total)

        return print(self.total)



    #return the value of the next function
    def ex(self, position):
        print("pos", position)
        position = position +1

        if self.throws[position] == "/": 
            return 10

        elif self.throws[position] == "X":
            return 10 + int(self.ex(position + 1))
        
        else:
            return self.throws[position]
            
        
           
           


def main():
    #throws = input("Enter your throws for your game: ")
    throws = "23-5/-X-X-44"
    b = Bowling(throws)
    b.findTotal()
    print("should be 46")


if __name__ == "__main__":
   main()