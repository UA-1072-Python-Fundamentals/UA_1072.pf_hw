## Menu Constructor + calories calculator, based on gender and activity level
# Import necessary modules
import sys
from datetime import datetime

class MenuConstructor: # Define a class
    # Constructor method for initializing the class
    def __init__(self):
        # Dictionary to store menu categories, production date, shell life and calories value
        self.categories = {
            'SOUP (250 g)': {
                'None': {'date': '01/01/2000', 'shelf_life': 0, 'calories': 0},  # 'None' for user to skip the category
                'Vegetable soup (vegan)': {'date': '11/11/2023', 'shelf_life': 4, 'calories': 100},
                'Borsch (vegan)': {'date': '11/11/2023', 'shelf_life': 4, 'calories': 90},
                'Fish and seafood soup': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 163},
                'Onion soup': {'date': '11/11/2023', 'shelf_life': 4, 'calories': 100},
            },
            'SIDE DISH (180 g)': {
                'None': {'date': '01/01/2000', 'shelf_life': 0, 'calories': 0},  # 'None' for user to skip the category
                'Buckwheat (vegan)': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 153},
                'Oatmeal (vegan)': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 126},
                'Quinoa': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 216},
                'Amaranth': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 666},
                'Lentils': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 198},
                'Baked potatoes': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 180},
                'Brown rice': {'date': '11/11/2023', 'shelf_life': 4, 'calories': 221}
            },
            'SALAD (300 g)': {
                'None': {'date': '01/01/2000', 'shelf_life': 5, 'calories': 0},  # 'None' for user to skip the category
                'Greek salad': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 360},
                'Cabbage salad': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 90},
                'Herring salad': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 450},
                'Caesar salad': {'date': '11/11/2023', 'shelf_life': 1, 'calories': 450}
            },
            'MEAT or FISH (120 g)': {
                'None': {'date': '01/01/2000', 'shelf_life': 0, 'calories': 0},  # 'None' for user to skip the category
                'Steamed Turkey': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 50},
                'Baked Turkey': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 110},
                'Turkey meatballs': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 50},
                'Salmon steak': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 110},
                'Seafood steamed': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 50},
            },
            'DESSERT (120 g)': {
                'None': {'date': '01/01/2000', 'shelf_life': 0, 'calories': 0},  # 'None' for user to skip the category
                'Pancakes': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 276},
                'Curd fritter': {'date': '11/11/2023', 'shelf_life': 2, 'calories': 300},
                'Chia pudding': {'date': '11/11/2023', 'shelf_life': 3, 'calories': 144}
            }
        }
        # Dictionary to store daily calorie norms based on gender and activity level
        self.daily_calories_norm = {
            'male': {
                'no_sport': 2000,
                '3_times': 2200,
                '3_+_times': 2600
            },
            'female': {
                'no_sport': 1800,
                '3_times': 2000,
                '3_+_times': 2400
            }
        }
        # Create counters and lists for defining fresh dishes and total calories calculation
        self.fresh_count = 0  # Counter for fresh dishes
        self.total_calories = 0  # Calories counter
        self.fresh_dishes = []  # List to store all the fresh dishes chosen by user
        # Create variables to store user gender and activity level
        self.gender = ''
        self.activity_level = ''

    # Method to get user gender and activity level
    def get_user_info(self):
        print('Enter your gender below')
        print('1 - Male')
        print('2 - Female')

        gender_choice = input('Answer: ')
        if gender_choice == '1':
            self.gender = 'male' #Class variable
        elif gender_choice == '2':
            self.gender = 'female' #Class variable
        else:
            print('Invalid choice. Please chose 1 or 2.') #Handling with input mistakes (recursion)
            self.get_user_info()


        print('Enter below your activity level')
        print('1 - Low (no sport)')
        print('2 - Moderate (up to 3 times per week)')
        print('3 - High (3+ sport activities per week)')

        activity_choice = input('Answer: ')
        if activity_choice == '1':
            self.activity_level = 'no_sport'
        elif activity_choice == '2':
            self.activity_level = '3_times'
        elif activity_choice == '3':
            self.activity_level = '3_+_times'
        else:
            print('Invalid choice. Please chose 1, 2, or 3.')
            self.get_user_info()

        print('*' * 26)
        print(f'{self.daily_calories_norm[self.gender][self.activity_level]} calories is your daily norm.')
        print('*' * 26)

    # Method to display the menu to the user
    def display_menu(self):
        self.get_user_info()
        print('SELECT DISHES FROM THE *MENU*\n'
              'TO CREATE YOUR HEALTHY MEAL.')
        print('*' * 26)
        for category, dishes in self.categories.items(): # Loop through menu categories
            print(f'{category} menu:')
            for i, (dish, _) in enumerate(dishes.items(), start=1):
                print(f'{i}. {dish}')

            choices = self.get_user_choices(category, len(dishes))
            self.process_choices(category, choices)

    # Method to get user choices for a specific category
    def get_user_choices(self, category, max_choices):
        while True:
            choices = input(f'- In {category} enter dish number(numbers via "space"), press "Enter": ').split()
            print(' ' * 10)
            if all(choice.isdigit() and 1 <= int(choice) <= max_choices for choice in choices):
                return choices
            else:
                print('Invalid input. Please enter valid dish number(s).')

    # Method to handle the selection of fresh dish, if Expired dish was chosen
    def choose_new_dish(self, category):
        while True:
            new_choice = self.get_user_choices(category, len(self.categories[category]))
            dish = list(self.categories[category].keys())[int(new_choice[0]) - 1]
            info = self.categories[category][dish]
            if self.is_dish_fresh(info):
                return dish
            else:
                print(f'{dish} - EXPIRED! Choose another dish.')
                print(' ' * 10)

    # Method to process user choices
    def process_choices(self, category, choices):
        for choice in choices:
            dish = list(self.categories[category].keys())[int(choice) - 1]
            if dish == 'None':
                continue
            info = self.categories[category][dish]
            if not self.is_dish_fresh(info):
                print(f'{dish} - EXPIRED !!! Choose another dish.') #Handle the choice of Expired dish
                print(' ' * 10)
                dish = self.choose_new_dish(category)
            self.fresh_count += 1  #Counters
            self.total_calories += info['calories']
            self.fresh_dishes.append(dish)
            print(f'{dish} - FRESH.')
            print(' ' * 10)

    # Method to check if a dish is fresh
    def is_dish_fresh(self, info):
        date_format = '%d/%m/%Y'
        prep_date = datetime.strptime(info['date'], date_format)
        current_date = datetime.now()
        shelf_life = info['shelf_life']
        return (current_date - prep_date).days <= shelf_life

    # Method to display a summary
    def display_summary(self):
        if self.fresh_count > 0:
            print(f"You have chosen:\n"
                  f"{self.fresh_count} dish(es) - {', '.join(self.fresh_dishes)}.")
        else:
            print('No fresh dishes were selected.')
            sys.exit()

        print(f'Totally - {self.total_calories} - calories per this meal.')
        percentage = round((self.total_calories / self.daily_calories_norm[self.gender][self.activity_level]) * 100, 0)
        print(f'It makes - {percentage}% - of your daily norm.')
        print('Bon appétit and stay fit!')

def main():
    menu_constructor = MenuConstructor()
    menu_constructor.display_menu()
    menu_constructor.display_summary()

if __name__ == '__main__':
    main()
