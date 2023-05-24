# build all us coins

import random 

class Coin:
    def __init__(self, rare=False, clean=True, heads=True):
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color
    
    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print('Coin Spent!')

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    

