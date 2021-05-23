'''
Case No8 Игра
Разработчики: Докукина К. (70%),
              Назирова Е. (50%)
'''

import random
def rule_game():
    '''
    :return: This function returns the text describing the game.
    '''
    print('Добро пожаловать в игру "Аэропорт"! Вы - настоящий владелец аэропорта. Ваша главная задача - увеличить прибыль.' ,
          'Составляющие игры:', 'Бюджет - ваши деньги', 'Топливо - необходимо закупать его, чтобы заправлять самолеты',
    'Рейсы - количество полетов в день', 'Пассажиры - количество людей в день',
          'Незабывайте, что все в этой игре взаимосвязанно! Удачи!',sep= '\n')

def character(consist):
    '''
    :param consist: Components of the game.
    :return: This function returns a list of the characteristics of the game.
    '''
    for i in consist:
        x = consist[i]
        print(i, ':' ,x)

def situation(consist):
    '''
    :param consist: Components of the game.
    :return: This function returns a list of basic situations or calls the function dop_sit.
    '''
    x = random.random()
    if x <= 0.7:
        print('Вам предстоит сделать выбор:', '1. Закупить топливо', '2. Открыть новый рейс', '3. Открыть набор на рейс',
              '4. Запустить рейс', sep= '\n')
        num = int(input())
        basic_sit(num, consist)
    if x > 0.7:
        dop_sit(consist)

def basic_sit(num, consist):
    '''
    :param num: Basic situation number.
    :param consist: Components of the game.
    :return: This function returns how the parameter values will change depending on the selected basic situation.
    '''
    if num == 1:
        budget(100000,0, consist)
        fuel(0, 1000, consist)
    if num == 2:
        fuel(5000, 0, consist)
        reys(0, 1, consist)
    if num == 3:
        reys(1, 0, consist)
        passag(0, 50, consist)
    if num == 4:
        passag(50, 0, consist)
        budget(0, 200000, consist)

def dop_sit(consist):
    '''
    :param consist: Components of the game.
    :return: This function returns how the values of the parameter will change depending on the current situation.
    '''
    x = random.randint(1,4)
    if x == 1:
        a = consist['Пассажиры']
        if a >= 100:
            print('В вашей местности начался карантин')
            passag(100, 0, consist)

    if x == 2:
        print('Одна авиакомпания запустила продажу билетов, что увеличило количество пассажиров')
        passag(0, 30, consist)
    if x == 3:
        a = consist['Пассажиры']
        b = consist['Рейсы']
        if a >= 50 and b >=1:
            print('Во время одного из полетов разбился самолет')
            reys(1, 0, consist)
            passag(50, 0, consist)
    if x == 4:
        print('Правительство выделило деньги на развитие аэропорта')
        budget(0, 100000, consist)

def budget(min, plus, consist):
    '''
    :param min: Changing the parameter to the negative side.
    :param plus: Changing the parameter to the positive  side.
    :param consist: Components of the game.
    :return: This function returns the new value of the parameter budget.
    '''
    x = consist['Бюджет']
    consist['Бюджет'] = x + plus - min

def fuel(min, plus, consist):
    '''
    :param min: Changing the parameter to the negative side.
    :param plus: Changing the parameter to the positive  side.
    :param consist: Components of the game.
    :return: This function returns the new value of the parameter fuel.
    '''
    x = consist['Топливо']
    consist['Топливо'] = x + plus - min

def reys(min, plus, consist):
    '''
    :param min: Changing the parameter to the negative side.
    :param plus: Changing the parameter to the positive  side.
    :param consist: Components of the game.
    :return: This function returns the new value of the parameter flights.
    '''
    x = consist['Рейсы']
    consist['Рейсы'] = x + plus - min

def passag(min, plus, consist):
    '''
    :param min: Changing the parameter to the negative side.
    :param plus: Changing the parameter to the positive  side.
    :param consist: Components of the game.
    :return: This function returns the new value of the parameter passengers.
    '''
    x = consist['Пассажиры']
    consist['Пассажиры'] = x + plus - min


def monitoring(consist):
    '''
    :param consist: Components of the game.
    :return: This function returns the end  of the game.
    '''
    a = consist['Бюджет']
    b = consist['Топливо']
    c = consist['Рейсы']
    d = consist['Пассажиры']
    if (a < 10000 and b <5000) or (b<5000 and c == 0) or (c ==0 and d < 50) or (d<50 and a < 10000):
        print('Игра окончена, вы проиграли')
        return 'over'
    return 1


def main():
    '''
    :return: This function returns the total of the game.
    '''
    print('АЭРОПОРТ')
    rule_game()
    consist = {'Бюджет': 1000000, 'Топливо': 10000, 'Рейсы': 2, 'Пассажиры': 100}
    print('Начальные характеристики игры:')
    character(consist)
    print('Игра будет предлагать вам различные ситуации, от выбора решения которых ваши характеристики будут меняться')
    n = 0
    answer = input('Начать игру? ')
    if answer.lower() == 'да':
        while True:
            n += 1
            print()
            character(consist)
            print()
            situation(consist)
            print()
            x = monitoring(consist)
            if x == 'over':
                print('Количество лет в игре: ', n)
                print('Ваши данные: ')
                character(consist)
                break



main()