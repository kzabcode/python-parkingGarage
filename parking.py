# Create class for parking garage.
# Needs Methods to
    # - take ticket
        # include a parkingSpace count and decrese with each entry
    # - pay for parking
        # store input into a variable
        # after they pay display a message that the ticket has been paid and they have 15 mins to leave
        # updates the "currentTicket" dictionary key "paid" to True
    # - leave garage
        # if ticket has been paid display TY message
        # if ticket not paid, display payment message
        # update parkingSpaces list to increase by 1


class parkingGarage():

    def __init__(self):
        self.tickets = 100
        self.parkingSpaces = 100
        self.currentTicket = {'owed':[], 'paid':[]}
        self.profit = []

    def takeTicket(self):
        name = input('What is your name? ')
        name = name.lower()
        self.currentTicket['owed'].append(name)
        self.tickets = self.tickets -1
        self.parkingSpaces = self.parkingSpaces -1 
        print(f'Their are now {self.tickets} parking spots left. Please park in an open space.')
        # I left this print in for testing and so you can see the code is working.
        print(self.currentTicket)

    def paying(self):
        out = input('Are you ready to pay now? ')
        if out.lower() == 'yes':
            who = input('What is your name? ')
            who = who.lower()
            if who in self.currentTicket['owed']:
                payment = int(input('How much you like to pay? '))
                if payment >0:
                    print(f'Thank you for your payment of ${payment}. You have 15 minutes to leave. Thank you.')
                    self.profit.append(payment)
                    self.currentTicket['owed'].remove(who)
                    self.currentTicket['paid'].append(who)
                    self.tickets = self.tickets+1
                    # I left these print for testing and so you can see the code is working.
                    print(sum(self.profit))
                    print(self.currentTicket)
                else:
                    print('Please enter a different amount')
            elif who not in self.currentTicket['owed']:
                print("Your name was not found")
            elif who in self.currentTicket['paid']:
                print('Looks like you aready paid! You have 15 minutes to leave the garage.')
        else:
            print('Please return when you are ready to pay. ')   
        
    def leaveGarage(self):
        paid = input("What is your name? ")
        paid = paid.lower()
        if paid in self.currentTicket['paid']:
            print('Thank you, have a nice day!' )
            self.parkingSpaces = self.parkingSpaces+1
        elif paid in self.currentTicket['owed']:
            parkingGarage.paying(self)
        else:
            print('Name could not be found. Please try again.')

lot_1 = parkingGarage()

def run():
    while True:
        space = input('Are you entering, paying or leaving the Parking Garage? ')
        if space.lower() == 'entering':
            lot_1.takeTicket()
        elif space.lower() == 'paying':
            lot_1.paying()
        elif space.lower() == 'leaving':
            lot_1.leaveGarage()
        else:
            print('Try again. Plase choose entering, paying or leaving. ')

run()



