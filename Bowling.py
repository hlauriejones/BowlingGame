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
        

    def findTotal(self):
        num = 0
        frame = 0
        first = 0
        two = 0
        before = 0
        after = 0
        one = 0
        

        for i in range(len(self.throws)):

            if self.throws[i] == '-':
                frame = frame + 1
                if frame == 9:
                    bonusPoints = self.bonus(i+1)
                    self.total = self.total + bonusPoints
                    break

            elif self.throws[i] == "/":
                prev = i - 1
                first = self.throws[prev]
                # print("first", first)
                adder = 10 - int(first)
                self.total = self.total + adder

                #includes the next value
                spare = int(self.next(i))
                self.total = self.total + int(spare)

            elif (self.throws[i] == "X"):

                self.total = self.total + 10
                #bc you need to account for the number you are on,
                #the dash, the next number and then finally you get 
                #to the number you want

                #this gets the next number
                one =  int(self.next(i))
                two = self.next(i+2)

                num = one + int(two)
                # print("num",num)

                self.total = self.total + int(num)
                
            else:
                integer = int(self.throws[i])
                self.total = self.total + integer
                #print(self.total)

        # print("frames",frame)

        return print(self.total)

    


    #accepts the position of the number you want to find the next of 
    def next(self, position):
        number = 0 
        first = 0
        prev = 0

        #skips to next number  
        position = position + 1

        if self.throws[position] == '-':
            position = position + 1

        if self.throws[position] == "/":
            prev = position -1
            # print("prev", prev)

            first = self.throws[position-1]
            # print("first", first)

            adder = 10 - int(first)
            number = adder
            

        elif self.throws[position] == "X":
            number = 10

        else: 
            number = self.throws[position]

        return number
        


    def bonus(self, position):
        
        if self.throws[position] == "X":
            bFirst = self.next(position)
            position = position + 1
            bSecond = self.next(position)

            bPts = int(bFirst) + int(bSecond) + 10

        elif self.throws[position+1] == "/":
            extra = self.throws[position+2]

            if extra == "X":
                extra = 10
            
            bPts = 10 + int(extra)

        else:
            bPts = int(self.throws[position]) + int(self.throws[position+1])


        return bPts
   


def main():
    #throws = input("Enter your throws for your game: ")

    print("it is done!")
    print("---- testing spares -------")
    throws = "5/-5/-5/-5/-5/-5/-5/-5/-5/-5/5"
    b = Bowling(throws)
    b.findTotal()
    print("should be 150")

    print("---- testing integers -------")
    throws = "45-54-36-27-09-63-81-18-90-72"
    b = Bowling(throws)
    b.findTotal()
    print("should be 90")


    print("---- testing strikes -------")
    throws = "X-X-X-X-X-X-X-X-X-XXX"
    b = Bowling(throws)
    b.findTotal()
    print("should be 300")

    print("---- testing fun cases -------")
    throws = "X-X-5/-44-X-72-7/-X-81-9/X"
    b = Bowling(throws)
    b.findTotal()
    print("should be 163")

if __name__ == "__main__":
   main()