# First, define the function with parameters
def describe_pet(animal_type, pet_name):
  """
  Displays information about a pet.

  :param animal_type: The type of animal (e.g., 'dog', 'cat').
  :param pet_name: The name of the pet.
  """
  print(f"I have a {animal_type}.")
  print(f"Its name is {pet_name.title()}.")
  print("-" * 20)


# 1. Using positional arguments (standard order)
# The values are assigned to parameters based on their position:
# "dog" goes to animal_type
# "Buddy" goes to pet_name
print("--- Positional Arguments ---")
describe_pet("dog", "Buddy") # positional

# 2. Using keyword arguments (reverse the order)
# The values are explicitly assigned to parameters using the parameter's name,
# so the order in the function call doesn't matter.
# "Milo" is explicitly assigned to pet_name
# "cat" is explicitly assigned to animal_type
print("--- Keyword Arguments (Order Reversed) ---")
describe_pet(pet_name="Milo", animal_type="cat") # keyword

# Example showing keyword arguments in the original order (still works!)
print("--- Keyword Arguments (Standard Order) ---")
describe_pet(animal_type="fish", pet_name="Nemo")