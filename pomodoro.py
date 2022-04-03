import time
import json
import sys

CONFIG_DATA = 'config_pomo.json'


def get_timer_config():
    with open(CONFIG_DATA, 'r') as cd:
        config_data = json.load(cd)
        return config_data


def request():
    inp = str(input(f"Intervall easy = ({get_timer_config()['intervall'][0]}), "
                    f"normal = ({get_timer_config()['intervall'][1]}), hard = ({get_timer_config()['intervall'][2]})?: "))

    if inp == 'easy':
        return get_timer_config()['intervall'][0]
    elif inp == 'normal':
        return get_timer_config()['intervall'][1]
    elif inp == 'hard':
        return get_timer_config()['intervall'][2]
    elif inp == 'exit' or inp == 'quit':
        sys.exit()
    else:
        print('Falsche Eingabe!')
        return False


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='\n')
        num_of_secs -= 1
        time.sleep(1)


def _aktiv():
    return int(get_timer_config()['aktiv'] * get_timer_config()['timer_config'])


def _break():
    return int(get_timer_config()['break'] * get_timer_config()['timer_config'])


def _big_break():
    return int(get_timer_config()['big_break'] * get_timer_config()['timer_config'])


def finished():
    print('Du hast es geschafft. Hurra!')


if __name__ == '__main__':
    if request() == get_timer_config()['intervall'][0]:
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        finished()
    elif request() == get_timer_config()['intervall'][1]:
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Große Pause')
        countdown(_big_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        finished()
    elif request() == get_timer_config()['intervall'][2]:
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Große Pause')
        countdown(_big_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Große Pause')
        countdown(_big_break())
        print('Aktivezeit')
        countdown(_aktiv())
        print('Pause')
        countdown(_break())
        print('Aktivezeit')
        countdown(_aktiv())
        finished()
