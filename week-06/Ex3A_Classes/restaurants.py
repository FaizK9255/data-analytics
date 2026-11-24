# Faiz Khan

class Restaurant:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

TacoBell = Restaurant('Taco Bell', 'Burritos and Tacos')
Subway = Restaurant('Subway', 'Sandwiches')
Wendys = Restaurant('Wendys', 'Fresh Burgers and Fries')

TacoBell.describe_rest()
TacoBell.rest_open()

Subway.describe_rest()
Subway.rest_open()

Wendys.describe_rest()
Wendys.rest_open()




