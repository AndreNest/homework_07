import work_with_user as wwu
def create_event(day):
    if day == 1:
        with open('schedule/monday.txt', 'a', encoding='utf-8') as data:
            data.writelines(wwu.new_event())
    elif day == 2:
        with open('schedule/tuesday.txt', 'a', encoding='utf-8') as data:
            data.writelines(wwu.new_event())
    elif day == 3:
        with open('schedule/wednesday.txt', 'a', encoding='utf-8') as data:
            data.write(wwu.new_event())
    elif day == 4:
        with open('schedule/thursday.txt', 'a', encoding='utf-8') as data:
            data.write(wwu.new_event())
    elif day == 5:
        with open('schedule/friday.txt', 'a', encoding='utf-8') as data:
            data.write(wwu.new_event())
    elif day == 6:
        with open('schedule/saturday.txt', 'a', encoding='utf-8') as data:
            data.write(wwu.new_event())
    elif day == 7:
        with open('schedule/sunday.txt', 'a', encoding='utf-8') as data:
            data.write(wwu.new_event())


