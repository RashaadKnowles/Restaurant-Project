from orderfactory import OrderFactory
from logger import logger_1
class Franchise:
    def __init__(self) -> None:
        self.location_number = 2331


    def place_order(self):
        user = input("What food would you like to order?")
        user_order = OrderFactory.create_order(user)
        call_log = logger_1.log_transactions(user_order,self.location_number)



    
