user_preference = input(
    "Do you want to travel? Enter 'Y' for yes and 'N' for no:   ")

if user_preference.upper() == 'Y':
    destination = input("Where do you wish to travel?   ")

    if destination.capitalize() == 'Dubai':
        print('Enjoy your stay in Dubai!')
    elif destination.capitalize() == 'London':
        print('Enjoy your stay in London!')
    elif destination.capitalize() == 'New York':
        print('Enjoy your stay in New York!')
    else:
        print('Ooops, that destination is not curently avaliable.')

else:
    print('Thanks for checking!')
