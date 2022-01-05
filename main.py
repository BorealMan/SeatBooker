
class SeatBookingService : 

    def __init__(self, col_length=2, row_length=6):
        self.col_length = col_length
        self.row_length = row_length
        self.Seats = []
        self.newSeatTable()

    def newSeatTable(self):
        self.clearSeatTable()
        self.Seats = [[0 for row in range(self.row_length)] for col in range(self.col_length)]

    def clearSeatTable(self):
        self.Seats.clear()

    def printSeats(self):
        print()
        for row in self.Seats:
            for seat in row:
                print(seat, end=" ")
            print()
        print()

    def checkColLength(self, col):
        return col < self.col_length and col >= 0

    def checkRowLength(self, row):
        return row < self.row_length and row >= 0

    def checkSeatRange(self, col, row):
        return self.checkColLength(col) and self.checkRowLength(row)

    def checkSeatAvailability(self, col, row):
        return self.Seats[col][row] == 0
    

    def BookSeat(self, col, row): 
        if self.checkSeatRange(col, row):
            if self.checkSeatAvailability(col, row):
                self.Seats[col][row] = 1
            
    def UnBookSeat(self, col, row):
        if self.checkSeatRange(col, row):
            if not self.checkSeatAvailability(col, row):
                self.Seats[col][row] = 0

    def BookingHandler(self):
        try:
            c = int(input("Enter Column:: "))
            r = int(input("Enter Row:: "))
            self.BookSeat(c - 1, r - 1)
        except:
            pass

    def UnBookingHandler(self):
        try:
            c = int(input("Enter Column:: "))
            r = int(input("Enter Row:: "))
            self.UnBookSeat(c - 1, r - 1)
        except:
            pass

    def Controller(self):
        r = int(input('1) Book Seat\n2) UnBook Seat\n3) Print Seats\n0) Quit\n::'))
        if r == 1:
            self.BookingHandler()
        elif r == 2:
            self.UnBookingHandler()
        elif r == 3:
            self.printSeats()
        elif r == 0:
            return False
        return True

    def Run(self):
        RUN = True
        while(RUN):
            try:
                RUN = self.Controller()
            except:
                print("\nUser Entered Garbage\n")


if __name__ == '__main__':
    a = SeatBookingService()
    a.Run()
