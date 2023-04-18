import pickle


def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficluty'] = 'Easy'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficluty'] = 'Medium'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficluty'] = 'Intermediate'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficluty'] = 'Hard'


def take_recipe():
    name = str(input('Enter Name of Recipe?   '))
    cooking_time = int(input('Enter cooking time?   '))
    ingredients = input('Enter the ingredients for this recipe?   ')
    ingredients = ingredients.split()
    ingredients = [ingredient.lower() for ingredient in ingredients]

    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    difficluty = calc_difficulty(recipe)

    return recipe


recipes_list = []
all_ingredients = []

filename = str(input(
    "Enter the filename where you've stored your recipes: (type N if there's not) "))
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print("File doesn't exist - creating new file")
    data = {'recipes_list': [], 'all_ingredients': []}

except:
    print("An unexpected error occurred - creating new file")
    data = {'recipes_list': [], 'all_ingredients': []}

else:
    recipes_file.close()

finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
