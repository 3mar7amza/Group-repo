# Class for Resorces 
class Resorces:
    def __init__(self,Water,Milk,Coffee,Money):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Money = Money

resorces_in_machine=Resorces(300,150,100,0)

# Class for Drinks
class Drinks:
    def __init__(self, Water, Milk, Coffee, Cost):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Cost = Cost
        
espresso = Drinks(50,30,25,30)
latte = Drinks(60,50,35,25.5)
cappuccino = Drinks(55,45,30,40)


# Print func
def printing_func():
    print("The Water In Ur Machine is {} \nThe Milk Is {}\nThe Coffee is {}\nThe Money is {} ".format(resorces_in_machine.Water,resorces_in_machine.Milk,resorces_in_machine.Coffee,resorces_in_machine.Money))


Menu = {
    "espresso" : espresso,
    "latte" : latte,
    "cappuccino" : cappuccino
}

# function for comparing resources
def compare():
    pass

























#Loop for the program
while True:
    choice=input("Enter ur choice: ")
    if choice.lower() == "report":
        printing_func()
    elif choice.lower() == "off":
        break
    elif choice.lower()  in Menu:
        pass

