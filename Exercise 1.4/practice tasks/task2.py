import pickle

recipe = {
    'Ingredient Name': 'Tea',
    'Ingredients': ['Tea leave\'s', 'Water', 'Sugar'],
    'Cooking Time': '5 minutes',
    'Difficulty': 'Easy'
}

with open('recipe_binary.bin', 'wb') as recipe_bin:
    pickle.dump(recipe, recipe_bin)

with open('recipe_binary.bin', 'rb') as recipe:
    recipe = pickle.load(recipe)

print("Ingredient Name: " + recipe['Ingredient Name'])
print("Ingredients: ", recipe['Ingredients'])
print("Cooking Time: " + recipe['Cooking Time'])
print("Difficulty: " + recipe['Difficulty'])
