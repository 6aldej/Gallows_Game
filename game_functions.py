from random import choice


WORDS_LIST = ['SKILLFACTORY',
              'TESTING',
              'BLACKBOX',
              'PYTEST',
              'UNITTEST',
              'COVERAGE']

LOGO = '''
██╗░░░██╗██╗░██████╗███████╗██╗░░░░░██╗████████╗░██████╗░█████╗░
██║░░░██║██║██╔════╝██╔════╝██║░░░░░██║╚══██╔══╝██╔════╝██╔══██╗
╚██╗░██╔╝██║╚█████╗░█████╗░░██║░░░░░██║░░░██║░░░╚█████╗░███████║
░╚████╔╝░██║░╚═══██╗██╔══╝░░██║░░░░░██║░░░██║░░░░╚═══██╗██╔══██║
░░╚██╔╝░░██║██████╔╝███████╗███████╗██║░░░██║░░░██████╔╝██║░░██║
░░░╚═╝░░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝
'''


def show_menu():
    print(
          'Нажмите 1, чтобы начать новую игру\n'
          'Нажмите 2, чтобы узнать правила игры\n'
          'Нажмите 0, чтобы выйти из игры')


def show_rules():
    print('\n1. Вы должны угадать слово. Введите с клавиатуры букву. Одна буква - один ход.\n'
          '2. Если вы угадаете правильно, то увидите буквы, которые присутствуют в слове.\n'
          '3. Если такой буквы нет - вы получаете штрафное очко. Четыре штрафных очка - конец игры :(\n')


def option_handler(option):
    try:
        option = int(option)
        if option == 0:
            return 0
        elif option == 1:
            play_game()
        elif option == 2:
            show_rules()
            show_menu()
            option_handler(input())
        else:
            print('\nНет такого варианта! :( Попробуйте ещё раз\n')
            show_menu()
            option_handler(input())
    except ValueError:
        print('\nНет такого варианта! :( Попробуйте ещё раз\n')
        show_menu()
        option_handler(input())


def print_hidden_word(word, letters: list):
    print()
    if letters:
        print(*[f'{char} ' if char in letters else '_ ' for char in word])
    else:
        print(*['_ ' for _ in word])


def is_valid(letter):
    return len(letter) == 1


def is_win(word, letters: list):
    return set(letters) == set(word)


def play_game():
    word = choice(WORDS_LIST)
    score = 0
    letters = []
    print_hidden_word(word, letters)
    while score < 4:
        letter = input('\nВаш ход: ').strip().capitalize()
        if is_valid(letter):
            if letter in word:
                letters.append(letter)
                if is_win(word, letters):
                    print(f'\nВы победили!🎉🎉🎉 Загаданное слово: {word}\n')
                    show_menu()
                    option = input()
                    option_handler(option)
                    break
                print_hidden_word(word, letters)
            else:
                score += 1
                print('\nШтрафные очки: ', score)

        else:
            print('Нет нет нет, только одна буква за ход!')
    else:
        print('\nВы проиграли!💀\n')

        show_menu()
        option = input()
        option_handler(option)
