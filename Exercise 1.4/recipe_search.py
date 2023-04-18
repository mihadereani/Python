import pickle


def display_recipe(recipe):
    print('''Recipe details
    =====================''')
    print('Name: ', recipe['name'])
    print('Cooking time (min): ', recipe['cooking_time'])
    print('Ingredients: ', recipe['ingredients'])
    print('Difficulty: ', recipe['difficluty'])


def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('No.', ingredient[0], ' - ', ingredient[1])

    try:
        chosen_num = int(
            input('Enter the corresponding number of your chosen ingredient:   '))
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()
    except IndexError:
        print('The number you entered is not on the list!')
    except:
        print('Some error happened finding the ingredient...')
    else:
        print('Recipes that include', ingredient_searched, 'are: ')
        print('---------------------------------------------------')
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                print(recipe['name'])
