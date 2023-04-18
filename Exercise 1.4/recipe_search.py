import pickle


def display_recipe(recipe):
    print('''Recipe details
    =====================''')
    print('Name: ', recipe['name'])
    print('Cooking time (min): ', recipe['cooking_time'])
    print('Ingredients: ', recipe['ingredients'])
    print('Difficulty: ', recipe['difficluty'])
