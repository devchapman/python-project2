import random

class Garage():
    def __init__(self):
        self.tickets = ['1', '2', '3', '4','5']
        self.parkingspace = ['1','2','3', '4', '5']
        self.currentTicket = ticket_info = {"paid": False}

    def takeTicket(self):
        self.tickets -= 1
        parkingspace -= 1
        pass

    def payForParking(self):
        total_amount = input("How much are you paying for parking:")
        if total_amount:
            self.currentTicket['paid'] == True
            print("Your ticket has been paid and you have 15 minutes to leave.")

    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True
            print("Thank You have a nice day!")
        else: 