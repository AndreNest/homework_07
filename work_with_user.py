def new_event():
    '''
    Запись события
    '''
    event = input('Что добавить в расписание?  ')
    return (f'{event}\n')


def what_day():
    '''
    Выбор конкретного дня
    :return:
    '''
    print('1 - понедельник | 2 - вторник\n3 - среда       | 4 - четверг\n5 - пятница     | 6 - суббота\n7 - суббота')
    day = int(input('Выберете день недели:  '))
    return day

def print_day(day):
    '''
    Вывод на конкретный день!
    :param day:
    :return:
    '''
    if day == 1:
        print('ПОНЕДЕЛЬНИК:')
        with open('schedule/monday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 2:
        print('ВТОРНИК:')
        with open('schedule/thursday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 3:
        print('СРЕДА:')
        with open('schedule/wednesday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 4:
        print('ЧЕТВЕРГ:')
        with open('schedule/thursday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 5:
        print('ПЯТНИЦА:')
        with open('schedule/friday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 6:
        with open('schedule/saturday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)
    elif day == 7:
        print('ВОСКРЕСЕНЬЕ:')
        with open('schedule/sunday.txt', 'r', encoding='utf-8') as data:
            for line in data:
                print(line)


def print_shedule():
    '''
    вывод всего расписания
    :return:
    '''
    print('*' * 15)
    print('ПОНЕДЕЛЬНИК:')
    with open('schedule/monday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('ВТОРНИК:')
    with open('schedule/thursday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('СРЕДА:')
    with open('schedule/wednesday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('ЧЕТВЕРГ:')
    with open('schedule/thursday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('ПЯТНИЦА:')
    with open('schedule/friday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('СУББОТА:')
    with open('schedule/saturday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
    print('*' * 15)
    print('ВОСКРЕСЕНЬЕ:')
    with open('schedule/sunday.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)



