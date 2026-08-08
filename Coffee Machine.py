# Class for Resorces 
class Resorces:
    def __init__(self,Water,Milk,Coffee,Money):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Money = Money
<<<<<<< HEAD
    def dict_func(self):
        Resorces_dict={"Water":self.Water,"Milk":self.Milk,"Coffee":self.Coffee,"Money":self.Money}
        return Resorces_dict
    
resorces_in_machine=Resorces(300,150,100,0)

=======

resorces_in_machine=Resorces(300,150,100,0)
>>>>>>> bfc342d8e9bffeb26f4f8fc6d3edcaf3af3dfbf3

# Class for Drinks
class Drinks:
    def __init__(self, Water, Milk, Coffee, Cost):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Cost = Cost
<<<<<<< HEAD
    
    def dict_func(self):
        Drinks_dict = {"Water":self.Water,"Milk":self.Milk,"Coffee":self.Coffee,"Cost":self.Cost}
        return Drinks_dict
    
=======
        
>>>>>>> bfc342d8e9bffeb26f4f8fc6d3edcaf3af3dfbf3
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
<<<<<<< HEAD
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
    pass      
=======
def compare():
    pass
























>>>>>>> bfc342d8e9bffeb26f4f8fc6d3edcaf3af3dfbf3

#Loop for the program
while True:
    choice=input("Enter ur choice: ")
    if choice.lower() == "report":
        printing_func()
    elif choice.lower() == "off":
        break
    elif choice.lower()  in Menu:
<<<<<<< HEAD
       chosen_drink=Menu[choice.lower()]
       enough=is_resource_enough(chosen_drink)
       if enough: 
           print("The resources is enough to make ur order")
=======
        pass

>>>>>>> bfc342d8e9bffeb26f4f8fc6d3edcaf3af3dfbf3
