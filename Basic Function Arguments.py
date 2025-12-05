# 1. Create a function named describe_pet that accepts two arguments:
#    - animal_type
#    - pet_name
def describe_pet(animal_type, pet_name):
    # 2. The function should print the specified message:
    # 3. I have a <animal_type> and its name is <pet_name>.
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("--- Calling the function three times ---")

# Task: Call the function three times with different animals and names.
# Call 1: Positional Arguments
describe_pet('dog', 'Max')

# Call 2: Positional Arguments
describe_pet('cat', 'Luna')

# Call 3: Keyword Arguments (an alternative way to call)
describe_pet(pet_name='Nemo', animal_type='fish')