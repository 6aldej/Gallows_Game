from game_functions import print_hidden_word, is_valid, is_win, show_menu, show_rules
import game_functions
import pytest


def test_print_hidden_word(capsys):
    print_hidden_word('TEST', [])
    assert capsys.readouterr().out == '\n_  _  _  _ \n'
    print_hidden_word('XXXX', ['X'])
    assert capsys.readouterr().out == '\nX  X  X  X \n'
    print_hidden_word('SKILL', ['S', 'I'])
    assert capsys.readouterr().out == '\nS  _  I  _  _ \n'


def test_is_valid():
    assert is_valid('a') is True
    assert is_valid('df') is False
    assert is_valid('') is False


def test_is_win():
    assert is_win('test', ['t', 's', 'e']) is True
    assert is_win('skill', ['s', 'l']) is False
    assert is_win('xxxx', []) is False


def test_show_menu(capsys):
    show_menu()
    assert capsys.readouterr().out == 'Нажмите 1, чтобы начать новую игру\n'\
                                      'Нажмите 2, чтобы узнать правила игры\n'\
                                      'Нажмите 0, чтобы выйти из игры\n'


def test_show_rules(capsys):
    show_rules()
    assert capsys.readouterr().out == '\n1. Вы должны угадать слово. Введите с клавиатуры букву. Одна буква - один ход.\n'\
                                        '2. Если вы угадаете правильно, то увидите буквы, которые присутствуют в слове.\n'\
                                        '3. Если такой буквы нет - вы получаете штрафное очко. Четыре штрафных очка - конец игры :(\n\n'


def test_play_game_win(capsys):
    input_values = ['t', 'E', 's', 'i', 'n', 'g', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nВаш ход: ',
                           '\nT  _  _  T  _  _  _ \n\nВаш ход: ',
                           '\nT  E  _  T  _  _  _ \n\nВаш ход: ',
                           '\nT  E  S  T  _  _  _ \n\nВаш ход: ',
                           '\nT  E  S  T  I  _  _ \n\nВаш ход: ',
                           '\nT  E  S  T  I  N  _ \n\nВаш ход: ',
                           '\nВы победили!🎉🎉🎉 Загаданное слово: TESTING\n'                       
                           '\nНажмите 1, чтобы начать новую игру\n'
                           'Нажмите 2, чтобы узнать правила игры\n'
                           'Нажмите 0, чтобы выйти из игры\n'])
    assert err == ''


def test_play_game_fail(capsys):

    input_values = ['h', 'y', 'f', 'j', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nВаш ход: ',
                           '\nШтрафные очки:  1\n\nВаш ход: ',
                           '\nШтрафные очки:  2\n\nВаш ход: ',
                           '\nШтрафные очки:  3\n\nВаш ход: ',
                           '\nШтрафные очки:  4\n
                           '\nВы проиграли!💀\n'
                           '\nНажмите 1, чтобы начать новую игру\n'
                           'Нажмите 2, чтобы узнать правила игры\n'
                           'Нажмите 0, чтобы выйти из игры\n'])
    assert err == ''


def test_play_game_invalid_input(capsys):

    input_values = ['t', 'yy', 'y', 'p', 'f', 'j', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nВаш ход: ',
                           '\nT  _  _  T  _  _  _ \n\nВаш ход: ',
                           'Нет нет нет, только одна буква за ход!\n\nВаш ход: ',
                           '\nШтрафные очки:  1\n\nВаш ход: ',
                           '\nШтрафные очки:  2\n\nВаш ход: ',
                           '\nШтрафные очки:  3\n\nВаш ход: ',
                           '\nШтрафные очки:  4\n
                           '\nВы проиграли!💀\n'
                           '\nНажмите 1, чтобы начать новую игру\n'
                           'Нажмите 2, чтобы узнать правила игры\n'
                           'Нажмите 0, чтобы выйти из игры\n'])
    assert err == ''


@pytest.mark.parametrize('input_value,output', [
                         ('0', ''),

                         ('2', '\n1. Вы должны угадать слово. Введите с клавиатуры букву. Одна буква - один ход.\n'
                                 '2. Если вы угадаете правильно, то увидите буквы, которые присутствуют в слове.\n'
                                 '3. Если такой буквы нет - вы получаете штрафное очко. Четыре штрафных очка - конец игры :(\n'
                                 
                                 '\nНажмите 1, чтобы начать новую игру\n'
                                 'Нажмите 2, чтобы узнать правила игры\n'
                                 'Нажмите 0, чтобы выйти из игры\n'),

                         ('3',   '\nНет такого варианта! :( Попробуйте ещё раз\n'
                                
                                 '\nНажмите 1, чтобы начать новую игру\n'
                                 'Нажмите 2, чтобы узнать правила игры\n'
                                 'Нажмите 0, чтобы выйти из игры\n'),

                         ('g',   '\nНет такого варианта! :( Попробуйте ещё раз\n'
                                 
                                 '\nНажмите 1, чтобы начать новую игру\n'
                                 'Нажмите 2, чтобы узнать правила игры\n'
                                 'Нажмите 0, чтобы выйти из игры\n')])


def test_option_handler(capsys, input_value, output):

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return 0

    game_functions.input = spoof_input
    game_functions.option_handler(input_value)

    out, err = capsys.readouterr()

    assert out == output
    assert err == ''
