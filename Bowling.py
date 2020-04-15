"""
Name: Bowling Game Coding Exercise
Authors: Laurie Jones

given an integer array of a valid sequence of self.throws for one game of 
American Ten-Pin Bowling, produces the total score for the game

class: Bowling
functions: findTotal, spare, strike, next, bonus

"""


class Bowling():

    def __init__(self, throws):
        self.throws = throws
        self.total = 0
        
 
#returns the total poiints you aquire in a full game of bowling
    def findTotal(self):
        frame = 0

        for i in range(len(self.throws)):

            if self.throws[i] == '-':
                frame = frame + 1
                if frame == 9:
                    bonusPoints = self.bonus(i+1)
                    self.total = self.total + bonusPoints
                    break

            elif self.throws[i] == "/":
                slash = self.spare(i)
                self.total = self.total + slash

            elif (self.throws[i] == "X"):
                X = self.strike(i)
                self.total = self.total + X
                
            else:
                self.total = self.total + int(self.throws[i])

        return print("Your total points are:", self.total)



# accpets: a position integer
# returns: all of the points aquired in the frame with the spare
    def spare(self, a):
        prevNum = self.throws[a-1]
        adder = 10 - int(prevNum)
        return adder + int(self.next(a))


# accpets: a position integer
# returns: all of the points aquired in the frame with the spare
    def strike(self,b):
        one =  int(self.next(b+1))
        two = int(self.next(b+2))
        return one + two + 10


#accepts the position of the number you want to find the next of 
#returns the next number in the game
    def next(self, position): 
        position = position + 1

        if self.throws[position] == '-':
            position = position + 1

        if self.throws[position] == "/":
            prev = self.throws[position-1]
            number = 10 - int(prev)
            
        elif self.throws[position] == "X":
            number = 10

        else: 
            number = self.throws[position]

        return number
        

#accepts the position of the first number in the 10th frame 
#returns the points you recieve with the 10th frame
    def bonus(self, position):
        if self.throws[position] == "X":
            bPts = int(self.next(position)) + int(self.next(position + 1)) + 10

        elif self.throws[position+1] == "/":
            extra = self.throws[position+2]
            if extra == "X":
                extra = 10
            bPts = 10 + int(extra)

        else:
            bPts = int(self.throws[position]) + int(self.throws[position+1])

        return bPts
   


def main():
#run it yourself
    throws = input("Enter your throws for your game: ")
    b = Bowling(throws)
    b.findTotal()


#tests
    # print("---- testing spares -------")
    # throws = "5/-5/-5/-5/-5/-5/-5/-5/-5/-5/5"
    # b = Bowling(throws)
    # b.findTotal()
    # print("should be 150")

    # print("---- testing integers -------")
    # throws = "45-54-36-27-09-63-81-18-90-72"
    # b = Bowling(throws)
    # b.findTotal()
    # print("should be 90")


    # print("---- testing strikes -------")
    # throws = "X-X-X-X-X-X-X-X-X-XXX"
    # b = Bowling(throws)
    # b.findTotal()
    # print("should be 300")

    # print("---- testing fun cases -------")
    # throws = "X-X-5/-44-X-72-7/-X-81-9/X"
    # b = Bowling(throws)
    # b.findTotal()
    # print("should be 163")

if __name__ == "__main__":
   main()