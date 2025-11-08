""""sdfdsfdsfsdf"""
import datetime
#!/usr/bin/env python3

import json
import os
import string
import subprocess
def print_info(our_string):
    """
    Print a string
    Example set default printer
        lpstat -p
        lpadmin -d Brother_HL-2170W_series
"""
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.stdin.write(bytes(our_string,'utf-8'))

def print_menu(our_string):
    top_line = '\n'*2
    new_string = f"Menu{top_line}{our_string} {top_line}Correct as of {datetime.datetime.now()}"
    print_info(new_string)

def getlist(adictionary):
    """dgdfgdf"""
    return adictionary.keys()

def make_a_string_from_list(my_list):
    return ' \n'.join([str(elem) for elem in my_list])

class MakeDrinks:
    """Kdklefkl"""

    def __init__(self, current_receipes, drinks_available_at_home):
        """Kdklefkl"""
        self.name = None
        self.drink_receipe = ""
        self.drinks_string = None
        self.shoppinglist = None
        self.best_buy_dict = None
        self.best_item_to_buy = None
        self.how_many = None
        self.available_drinks_with_ingredients = None
        self.drink_components = None
        self.available_drinks_with_previous_ingredients = None
        self.receipe_string = None
        self.current_receipes = self.open_receipes(current_receipes)
        self.drinks_cabinet = self.open_drinks_cabinet(drinks_available_at_home)
        self.drinks()
        self.drink_selection_broken_by_ingredient_string = self.drink_selection_broken_by_ingredient()


    def open_receipes(self, current_receipes):
        """dsfdsfs"""
        try:
            if os.path.isfile(current_receipes):
                with open(current_receipes, "r", encoding='utf-8') as my_receipes:
                    return json.load(my_receipes)
        except TypeError:
            if type(current_receipes) is dict:
                return current_receipes

    def open_drinks_cabinet(self, drinks_available_at_home):
        """sdfsdfds"""
        try:
            if os.path.isfile(drinks_available_at_home):
                with open(drinks_available_at_home, "r", encoding='utf-8') as txt_file:
                    return txt_file.read()
        except TypeError as e:
            if type(drinks_available_at_home) is list:
                return "\n".join(drinks_available_at_home)

    def drinks(self):
        """Kdklefkl"""
        self.possible_drinks = []
        self.drinks_cant_make = []
        for drink, ingredients in self.current_receipes.items():
            if all(elem in self.drinks_cabinet for elem in ingredients.keys()):
                self.possible_drinks.append(drink)
            else:
                self.drinks_cant_make.append(drink)
        self.number_drinks_can = len(self.possible_drinks)
        return self.possible_drinks, self.drinks_cant_make, self.number_drinks_can

    def possible_drinks_string(self ):
        """Kdklefkl"""
        self.drinks_string = ""
        for drink in sorted(self.possible_drinks, reverse=True):
            line = f"{string.capwords(drink)} - {string.capwords(', '.join(self.current_receipes[drink]))}. \n"
            self.drinks_string = line + self.drinks_string
        lines = self.drinks_string.splitlines()
        lines.sort()
        self.drinks_string = make_a_string_from_list(lines)
        return self.drinks_string


    def possible_drinks_string_component(self, component):
        """Kdklefkl"""
        self.drinks_string = ""
        for drink in sorted(component, reverse=True):
            line = f"{drink} - {', '.join(self.current_receipes[drink])} xx \n"
            self.drinks_string = line + self.drinks_string
        return self.drinks_string


    def countdrinks(self):
        """Count the number of possible drinks"""
        return len(self.possible_drinks)

    def print_menu(self):
        """Kdklefkl"""

        print(
            f"\nWe are able to offer {len(self.possible_drinks)} drinks from our menu.\n\n"
        )
        self.possible_drinks_string()

    def next_time(self):
        """Kdklefkl"""

        self.shoppinglist = set()
        for drink in self.drinks_cant_make:
            ingredients = self.current_receipes[drink]
            for my_item in ingredients:
                if my_item not in self.drinks_cabinet:
                    self.shoppinglist.add(my_item)
        return self.shoppinglist

    def create_new_drinks_lists(self):
        """Kdklefkl"""
        self.next_time()
        self.best_buy_dict = {}
        for missing_ingredient in self.shoppinglist:
            new_drinks_list = []
            new_drinks_list.append(missing_ingredient)
            new_thing = new_drinks_list + self.drinks_cabinet.splitlines()
            new_menu = MakeDrinks(self.current_receipes, new_thing)
            self.best_buy_dict[missing_ingredient] = new_menu.number_drinks_can
        self.best_item_to_buy = max(self.best_buy_dict, key=self.best_buy_dict.get)
        self.how_many = self.best_buy_dict[self.best_item_to_buy]
        return self.best_buy_dict, self.best_item_to_buy, self.how_many

    def zzzzavailable_drinks_with_ingredient(self, component):
        """Kdklefkl"""
        self.available_drinks_with_ingredients = []
        for ingredient_in in self.possible_drinks:
            if component in self.current_receipes[ingredient_in]:
                self.available_drinks_with_ingredients.append(ingredient_in)
        return self.available_drinks_with_ingredients.sort()

    def available_drinks_with_ingredient_x(self, component):
        """Kdklefkl"""
        self.available_drinks_with_previous_ingredients = []
        for ingredient_in in self.possible_drinks:
            if component in self.current_receipes[ingredient_in]:
                self.available_drinks_with_previous_ingredients.append(ingredient_in)
        return self.available_drinks_with_previous_ingredients.sort()


    def whats_in_drink(self, name):
        """sdgdgdfgd"""
        self.name = name.lower()
        self.drink_receipe = ""
        for ingredient, measure in self.current_receipes[name.rstrip()].items():
            self.drink_receipe = (
                    self.drink_receipe + measure + " " + ingredient.capitalize() + ", "
            )
        return self.name, self.drink_receipe

    def drink_receipe_with_an_ingredient(self, ingredient):
        ingredient = ingredient.lower()
        self.available_drinks_with_ingredient_x(ingredient)
        self.receipe_string = ""
        for drink in self.available_drinks_with_previous_ingredients:
            self.whats_in_drink(drink)
            self.receipe_string = self.name.capitalize() + " - " \
                                  + self.drink_receipe[:-2] \
                                  + ".\n" + self.receipe_string
        lines = self.receipe_string.splitlines()
        lines.sort()
        self.receipe_string = make_a_string_from_list(lines)
        if len(self.receipe_string) < 1:
            self.receipe_string = f"We dont have any {ingredient.capitalize()}"
        return self.receipe_string

    def drink_selection_broken_by_ingredient(self):
        drinks = []
        for x in ['bacardi','cointreau','gin','jack daniels','vodka']:
            self.drink_receipe_with_an_ingredient(x)
            drinks.append(x.capitalize() + "\n" + self.receipe_string + '\n\n')
        return "".join(drinks)

        #return self.drink_selection_broken_by_ingredient_string
def main():
    """dsfdsf"""
    cabinet = "./drinkscabinet.txt"
    receipes = "./receipes.json"
    x = MakeDrinks(receipes,cabinet)
    print(x.possible_drinks_string())
    #print(x.drink_receipe)
    #print(x.drink_selection_broken_by_ingredient())
    #print(x.print_menu())

if __name__ == "__main__":
    main()