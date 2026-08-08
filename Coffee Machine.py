# Class for Resorces 
class Resorces:
    def __init__(self,Water,Milk,Coffee,Money):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Money = Money
    def dict_func(self):
        Resorces_dict={"Water":self.Water,"Milk":self.Milk,"Coffee":self.Coffee,"Money":self.Money}
        return Resorces_dict
    
resorces_in_machine=Resorces(300,150,100,0)


# Class for Drinks
class Drinks:
    def __init__(self, Water, Milk, Coffee, Cost):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Cost = Cost
    
    def dict_func(self):
        Drinks_dict = {"Water":self.Water,"Milk":self.Milk,"Coffee":self.Coffee,"Cost":self.Cost}
        return Drinks_dict
    
espresso = Drinks(50,30,25,3)
latte = Drinks(60,50,35,2.5)
cappuccino = Drinks(55,45,30,4)


# Print func
def printing_func():
    print("The Water In Ur Machine is {} \nThe Milk Is {}\nThe Coffee is {}\nThe Money is {} ".format(resorces_in_machine.Water,resorces_in_machine.Milk,resorces_in_machine.Coffee,resorces_in_machine.Money))


Menu = {
    "espresso" : espresso,
    "latte" : latte,
    "cappuccino" : cappuccino
}

# function for comparing resources
def is_resource_enough(drink):
    dint_reqs = drink.dict_func()
    resorces_have = resorces_in_machine.dict_func()
    for items in ["Water", "Milk", "Coffee"] : 
        needed = dint_reqs[items]
        have = resorces_have[items]
        if needed > have:
            print("Sorry there is not enough {}".format(items))
            return False
        
    return True
            
      
# Money func
def process_coins():
   coins_quarters = int(input("How many quarters u will input: "))
   coins_dimes = int(input("How many dimes u will input: "))
   coins_nickles = int(input("How many nickles u will input: "))
   coins_pennies = int(input("How many pennies u will input: "))
   total_money = round(coins_quarters*0.25 + coins_dimes*0.10 + coins_nickles*0.05 + coins_pennies*0.01, 2)
   return total_money

#Make coffee func & changes in the resources 
def make_coffee(drink):
    drink_reqs = drink.dict_func()
    resorces_in_machine.Water -= drink_reqs["Water"]
    resorces_in_machine.Milk -= drink_reqs["Milk"]
    resorces_in_machine.Coffee -= drink_reqs["Coffee"]
    resorces_in_machine.Money += drink.Cost
    print("Here is your {}. Enjoy!".format(choice.lower()))

#Loop for the program
while True:
    choice=input("Enter ur choice: ")
    if choice.lower() == "report":
        printing_func()
    elif choice.lower() == "off":
        break
    elif choice.lower()  in Menu:
       chosen_drink=Menu[choice.lower()]
       enough=is_resource_enough(chosen_drink)
       if enough: 
        print("The resources is enough to make ur order")
        money_come = process_coins()
        if money_come > chosen_drink.Cost:
            remaining = money_come - chosen_drink.Cost
            print("Here is ${} in change.".format(remaining))
            make_coffee(chosen_drink)
        elif money_come < chosen_drink.Cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            make_coffee(chosen_drink)