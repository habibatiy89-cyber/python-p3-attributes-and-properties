# lib/dog.py

approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
                   "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Unknown", breed="Beagle"):
        self.name = name   # use property setter
        self.breed = breed # use property setter

    # ----- Name Property -----
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # ----- Breed Property -----
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)


# --- Testing the class ---
fido = Dog(name="Fido", breed="Mastiff")
print(fido.name)  # Fido
print(fido.breed) # Mastiff

fido.name = ""    # Invalid
# Name must be string between 1 and 25 characters.

fido.breed = "Dragon Dog" # Invalid
# Breed must be in list of approved breeds.
