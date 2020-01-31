# # NEW is considered a 1
# # GOOD is considered a 0.8
# # OKAY is considered a 0.5
# # BAD is considered a 0.2


# from datetime import datetime
# from enum import Enum  

# # class condition(Enum):
# #     NEW = 1
# #     GOOD = 0.8
# #     OKAY = 0.5
# #     BAD = 0.2
    
# def lookup_msrp_value(make, model):
#     # """
#     # Determine original sale price of a bike when new
#     # """
#     return 1000
    
    
# def set_sale_price(bike):
#     original_value = lookup_msrp_value(bike['make'], bike['model'])
#     current_year = datetime.now().year
#     current_value = original_value * (1 - (current_year - bike['year']) * 0.015)
#     current_value = current_value * bike['condition']
#     bike['sale_price'] = current_value
    
    
# def create_bike(cost, make, model, year, condition):
#     return {
#         'cost': cost,
#         'make': make,
#         'model': model,
#         'year': year,
#         'condition': condition,
#         'sold': False,
#     }
    
    
# def sell(bike):
#     bike['sold'] = True
#     profit = bike['sale_price'] - bike['cost']
#     return profit
    
    
# bike1 = create_bike(100, 'Univega', 'Alpina', 1999, 0.5)
    
    
# set_sale_price(bike1)
    
    
# sell(bike1)



from datetime import datetime
from enum import Enum 
    
    
class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2
    
    
class Create_bike:
    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.sold = False

    def lookup_msrp_value(self, make=None, model=None):
        """
        Determine original sale price of a bike when new
        """
        return 1000   

    def set_sale_price(self):
        original_value = self.lookup_msrp_value()
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition
        self.sale_price = current_value
     
    
    
    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit
    
    
bike1 = Create_bike(100, 'Univega', 'Alpina', 1999, Condition.OKAY.value)
    
    
bike1.set_sale_price()

print('Price for ' + Condition(bike1.condition).name + ' conditioned bike is: ' + str('${:,.2f}'.format(bike1.sell())))

# print('${:,.2f}'.format(bike1.sell()))

