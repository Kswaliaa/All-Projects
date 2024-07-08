#travel plan 
#variables - country of travel, month, and type of trip leisure or business
#if leisure trip - calculate hotel expense, food expense, local travelling expense, flight cost, other adventure costs
#if business trip - calculate hotel expense, food expense, local travelling expense, flight cost

class Travel_cost:
    def __init__(self,country,month,type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0

    def trip_info(self):
        if self.month >= 10 and self.month <=3:
            print(f"you are going to {self.country} in winter! This is {self.type} trip")
        elif self.month>3 and self.month<10:
            print(f"you are going to {self.country} in summer! This is {self.type} trip")
        else:
            print("invalid input")
    def calc_cost(self,cost):
        costs =[]
        while cost !=0:
            self.price +=cost
            costs.append(cost)
            cost = int(input("Enter another cost"))
        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice,inspect
     
    def advice(self,num):
        if num < 500:
            print("Low budget")
        elif num >= 500 and num <1500:
            print("Take a flight to anywhere")
        else:
            print("Luxury Trip")

    def list_inspect(self,costs):
        less_than_10 = 0
        for x in costs:
            if x <= 10:
                less_than_10 +=1
        if less_than_10 <=10:
            self.price +=100
            print(f"updated price : {self.price}")


location = input("which country are you planning: ").capitalize()
trip_type = input("leisure or Business: ").capitalize()
month = int(input("Enter a month: "))

test = Travel_cost(location,month,trip_type)

test.trip_info()
flight_cost = float(input("Enter flight cost: "))
test.calc_cost(flight_cost)


            
