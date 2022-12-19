import  create_schedule as cs
import  work_with_user as wwu

def schedule_bot():
    flag = True
    while flag == True:
        print('1 - новое событие, 2 - показать расписание, 3 - расписание на конкретный день, 4 - закрыть')
        action = int(input('Что будем делать? '))
        if action == 1:
            print('На какой день недели сделать напоминание?')
            day = wwu.what_day()
            cs.create_event(day)
        elif action == 2:
            wwu.print_shedule()
        elif action == 3:
            print('Какой день недели показать? ')
            day = wwu.what_day()
            wwu.print_day(day)
        elif action == 4:
            print('Бот отключен!')
            flag = False
schedule_bot()