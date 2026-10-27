class ATM:
    def __init__(self):
        self.amount=100000000
        self.pin=2008
        print('welcome to Divyank ATM machine')
    def card_insert(self):
        user_card=input('Please insert your card:-')
        if user_card.lower()=='card':
            print('Card inserted successfully')
            ob.enter_pin()
        else:
            print('Invalid card')
    def enter_pin(self):
        user_pin=int(input('Please enter the pin:-'))
        if user_pin==self.pin:
            print('Pin is correct')
            print('1)Check balance\n2)Withdraw')
            choice=int(input('select any option:-'))
            if choice==1:
                ob.check_balance()
            elif choice==2:
                ob.withdraw()
            else:
                print('Invalid choice')

        else:
            print('invalid pin')
    def check_balance(self):
        print('Your balance is:-',self.amount)
    def withdraw(self):
        user_amount=int(input('Enter the amount:-'))
        print('Your balance is:-',self.amount-user_amount)
ob=ATM()
ob.card_insert()