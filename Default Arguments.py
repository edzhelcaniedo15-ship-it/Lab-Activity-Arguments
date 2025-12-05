def describe_pet(pet_name, animal_type="dog"):
    """
    Displays information about a pet, using 'dog' as the default animal type.
    """
    print(f"I have a {animal_type} and its name is {pet_name.title()}.")

# Task 1: Call with only one positional argument ("Brownie").
# The default argument "dog" is used for animal_type.
print("--- Task 1 (Using Default) ---")
describe_pet("Brownie")

# Task 2: Call with both arguments ("Nugget", "chicken").
# The provided value "chicken" overrides the default "dog".
print("--- Task 2 (Overriding Default) ---")
describe_pet("Nugget", "chicken")