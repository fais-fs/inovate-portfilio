from person import Person

Faisal = Person("Faisal", "30", "6'7")

print(Faisal)

Kelly = Person("Kelly", "27", "5'7")

print(Kelly.name)

print(f"The climber is called {Kelly.name}, she is {Kelly.age} years old and is only {Kelly.height}.")

Faisal.set_hair("black and messy")

Kelly.set_hair("blonde and straight")

print(f"Faisal's hair is {Faisal.hair} but Kelly's hair is {Kelly.hair}.")

Faisal.get_hair()
Kelly.get_hair()