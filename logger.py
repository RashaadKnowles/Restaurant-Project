
class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transactions(self,order,store_number):
        self.transaction_count = self.transaction_count + 1
        self.daily_sales = self.daily_sales + order.dish_price 
        file = open("log.txt", "a")
        file.write(f"The current transaction count is {self.transaction_count} is 0,the name of the dish is {order.dish_name},the store number is {store_number},the price of the dish is {order.dish_price}  ,and the combined daily income is {self.daily_sales}.\n")
        file.close
    
        

logger_1 = Logger()
