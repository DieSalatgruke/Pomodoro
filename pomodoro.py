import time
import json
import sys
from win10toast import ToastNotifier

CONFIG_DATA = 'config_pomo.json'

big_break = 'Große Pause'
aktive = 'Aktivezeit'
last_aktiv = 'Letzte Runde'
time_break = 'Pause'


def notification(what_is):
    toast = ToastNotifier()
    toast.show_toast(
        f'{what_is}',
        f' ',
        threaded=True
    )


def func_pomo():
    b_list = create_list_big_break(inpt)
    for t in range(inpt):
        if t in b_list:
            notification(aktive)
            timer_for_aktiv(aktive)
            notification(big_break)
            timer_for_big_break(big_break)
        elif t == inpt - 1:
            notification(last_aktiv)
            timer_for_aktiv(aktive)
            finished()
        else:
            notification(aktive)
            timer_for_aktiv(aktive)
            notification(time_break)
            timer_for_break(time_break)


def get_timer_config():
    with open(CONFIG_DATA, 'r') as cd:
        config_data = json.load(cd)
        return config_data


def request(_inp):
    if _inp == 'easy':
        return get_timer_config()['intervall'][0]
    elif _inp == 'normal':
        return get_timer_config()['intervall'][1]
    elif _inp == 'hard':
        return get_timer_config()['intervall'][2]
    elif _inp == 'exit' or _inp == 'quit':
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


def calculate_big_break(_interval):
    _big_breaks = _interval/3
    if str(_big_breaks)[-1] == '0':
        _big_breaks -= 1
        return int(_big_breaks)
    else:
        _big_breaks = _interval // 3
        return _big_breaks


def timer_for_big_break(bb):
    make_it_beauty()
    print(f'{bb}')
    make_it_beauty()
    countdown(_big_break())


def timer_for_break(b):
    make_it_beauty()
    print(f'{b}')
    make_it_beauty()
    countdown(_break())


def timer_for_aktiv(a):
    make_it_beauty()
    print(f'{a}')
    make_it_beauty()
    countdown(_aktiv())


def create_list_big_break(interval_intensity):
    break_list = [2]
    start_break = 2
    for elm in range(calculate_big_break(interval_intensity)):
        start_break = start_break + 3
        break_list.append(start_break)
    return break_list


def make_it_beauty():
    print('-' * 15)


def _aktiv():
    return int(get_timer_config()['aktiv'] * get_timer_config()['timer_config'])


def _break():
    return int(get_timer_config()['break'] * get_timer_config()['timer_config'])


def _big_break():
    return int(get_timer_config()['big_break'] * get_timer_config()['timer_config'])


def finished():
    print('Hurra! Du hast es geschafft.')


if __name__ == '__main__':
    i = 1
    while i == 1:
        inp = str(input(f"Intervall easy = ({get_timer_config()['intervall'][0]}), "
                        f"normal = ({get_timer_config()['intervall'][1]}), "
                        f"hard = ({get_timer_config()['intervall'][2]})?: "))

        inpt = request(inp)

        if inpt is False:
            i = 1
        else:
            func_pomo()
            i = 2
