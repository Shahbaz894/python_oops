class Atm():
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menue()
        
    def menue(self):
         user_input=input(
             
             '''
             1.how can i help you.
             2.create the pin
             3.check the balance
             4.chnage the pin
             5.with draw money
             
             '''
         )
         if user_input=='2':
            self.createPin()
         elif user_input=='3':
             self.checkBalance()
         elif user_input=='4':
             self.changePin()
         elif user_input=='5':
             self.withDrawBalance()
          
         else:
             self.menue()
           
    def createPin(self):
        pin=input('enter pin')
        balance=int(input('enter balnace'))
        self.pin=pin
        self.balance=balance
        print('pin create successfuly')
        self.menue()
        
    def checkBalance(self):
        print(self.balance)
    def changePin(self):
        oldPin=input('enter old pin')
        if self.pin==oldPin:
            newPin=input('enter new pin')
            self.pin=newPin
            print('pin change successfully')
        else:
            self.menue()
    
             
    def withDrawBalance(self):
          amount=int(input('enter amount'))
          
          remainBalance=self.balance-amount
          self.balance=remainBalance
          print(self.balance)
          self.menue()
             
            
             
a=Atm()