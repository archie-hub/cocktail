""""sdfdsfdsfsdf"""
import datetime
#!/usr/bin/env python3
from fpdf import FPDF
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
        #self.drinks_we_can_make_with_receipes_dictionary = None
        self.current_receipes = self.open_receipes(current_receipes)
        self.drinks_cabinet = self.open_drinks_cabinet(drinks_available_at_home)
        self.drinks()
        self.drink_selection_broken_by_ingredient_string = self.string_available_drink_selection_broken_by_ingredient()
        self.drinks_we_can_make_with_receipes_dictionary = None
        self.drinks_we_can_make_with_receipes_json()

    def drinks_we_can_make_with_receipes_json(self):
        self.drinks_we_can_make_with_receipes_dictionary = {}
        #print(self.possible_drinks)
        for drink in self.possible_drinks:
            self.drinks_we_can_make_with_receipes_dictionary[drink] = self.current_receipes[drink]
        print(type(self.drinks_we_can_make_with_receipes_dictionary))
        return self.drinks_we_can_make_with_receipes_dictionary

    def print_possible_drinks_string_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        pdf.multi_cell(0, 10, txt=self.possible_drinks_string())
        pdf.output("outpuzzt.pdf")


    def xprint_possible_drinks_string_by_component_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=10)
        pdf.multi_cell(0, 10, txt=self.available_drink_selection_broken_by_ingredient())
        pdf.output("bycomponent.pdf")

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
            line = (f"{string.capwords(drink)} -"
                    f" {string.capwords(', '.join(dict(sorted(self.current_receipes[drink].items()))))}. \n")
            self.drinks_string = line + self.drinks_string
        lines = self.drinks_string.splitlines()
        lines.sort()
        self.drinks_string = make_a_string_from_list(lines)
        return self.drinks_string


    def possible_drinks_string_component(self, component):
        """Kdklefkl"""
        self.drinks_string = ""
        for drink in sorted(component, reverse=True):
            print(102,self.current_receipes[drink])
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
            #print(171)
            if component in self.current_receipes[ingredient_in]:
                self.available_drinks_with_previous_ingredients.append(ingredient_in)
        #print(174, self.available_drinks_with_previous_ingredients)

        return self.available_drinks_with_previous_ingredients.sort()


    def whats_in_drink(self, name):
        """sdgdgdfgd"""
        self.name = name.lower()
        self.drink_receipe = ""
        for ingredient, measure in dict(sorted(self.current_receipes[name.rstrip()].items())).items():
            self.drink_receipe = (
                    self.drink_receipe + measure + " " + ingredient.capitalize() + ", "
            )
        return self.name, self.drink_receipe

    def string_drink_receipe_with_an_ingredient(self, ingredient):
        ingredient = ingredient.lower()
        self.available_drinks_with_ingredient_x(ingredient)
        #print(191,self.available_drinks_with_previous_ingredients)
        self.receipe_string = ""
        for drink in self.available_drinks_with_previous_ingredients:
            self.whats_in_drink(drink)
            #print(192,self.name, self.drink_receipe)
            self.receipe_string = self.name.title() + " - " \
                                  + self.drink_receipe[:-2] \
                                  + ".\n" + self.receipe_string
        lines = self.receipe_string.splitlines()
        lines.sort()
        self.receipe_string = make_a_string_from_list(lines)
        if len(self.receipe_string) < 1:
            self.receipe_string = f"We dont have any {ingredient.capitalize()}"
        return self.receipe_string

    def string_available_drink_selection_broken_by_ingredient(self):
        ##print(88888)
        drinks = []
        for main_component in ['bacardi','cointreau','gin','jack daniels','vodka']:
            self.string_drink_receipe_with_an_ingredient(main_component)
            #drinks.append(main_component.capitalize() + "\n" + self.receipe_string + '\n\n')
            drinks.append(main_component.title() + "\n" + self.receipe_string + '\n\n')
        return "".join(drinks)

        #return self.drink_selection_broken_by_ingredient_string



def main():
    """dsfdsf"""
    cabinet = "./drinkscabinet.txt"
    receipes = "./receipes.json"
    ourdrinks = MakeDrinks(receipes,cabinet)
    print(ourdrinks.drinks_we_can_make_with_receipes_dictionary)
    #ourdrinks.drinks_we_can_make_with_receipes_json()
    #print(ourdrinks.whats_in_drink('White Lady'))
    #print(ourdrinks.possible_drinks_string())
    #file_name="somefile.txt"
    #with open(file_name, 'w') as file_object:
     #   file_object.write(ourdrinks.possible_drinks_string())

    #print(f"String successfully written to '{file_name}'")
    #ourdrinks.print_possible_drinks_string()
    #print(ourdrinks.available_drink_selection_broken_by_ingredient(),777)
    #print(ourdrinks.available_drink_selection_broken_by_ingredient())
    #print("\n\n",ourdrinks.string_drink_receipe_with_an_ingredient('gin'))
    #print(ourdrinks.zzzzavailable_drinks_with_ingredient('kahlua'),212)
    # Needs some tweaking.
    # print(ourdrinks.create_new_drinks_lists())
    # print(ourdrinks.best_buy_dict)
    # print(ourdrinks.best_item_to_buy)
    # print(ourdrinks.how_many)

    #print(x.drink_selection_broken_by_ingredient())
    #print(x.print_menu())
    #print(x.possible_drinks_string_component('vodka'))
    #  ourdrinks.print_possible_drinks_string_by_component()
    #print(ourdrinks.string_available_drink_selection_broken_by_ingredient())
    #print(ourdrinks.drinks(),244)
    #print(ourdrinks.possible_drinks)



if __name__ == "__main__":
    main()