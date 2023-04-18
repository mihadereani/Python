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
