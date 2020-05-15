from game_functions import show_menu, option_handler, LOGO


print(LOGO)
print('\nДобро пожаловать в игру!')
show_menu()
option = input()
option_handler(option)
