class Character():
    def __init__(self, real_name, superhero_name):
        self.real_name = real_name
        self.superhero_name = superhero_name

    def set_power(self, superhero_power):
        self.power = superhero_power

    def get_power(self):
        print(f"The secret identity of {self.real_name} is {self.superhero_name} and their super power is {self.power}.")