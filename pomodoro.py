import time
import json
import sys
import tkinter as tk
import winsound

CONFIG_DATA = 'config_pomo.json'


class Clock:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text='',
                   font=('Arial', 45),
                   fg='green',
                   bg='black',
                   width=20,
                   height=4)
        self.label.pack()
        self.root.mainloop()

    def update_clock(self, pomotime):
        self.label.configure(text=pomotime)
        self.root.after(1000, self.update_clock)


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


def timer_for_big_break():
    sound()
    make_it_beauty()
    print('Große Pause')
    make_it_beauty()
    countdown(_big_break())


def timer_for_break():
    sound()
    make_it_beauty()
    print('Pause')
    make_it_beauty()
    countdown(_break())


def timer_for_aktiv():
    sound()
    make_it_beauty()
    print('Aktivezeit')
    make_it_beauty()
    countdown(_aktiv())


def create_list_big_break(interval_intensity):
    break_list = [2]
    start_break = 2
    for elm in range(calculate_big_break(interval_intensity)):
        start_break = start_break + 3
        break_list.append(start_break)
    return break_list


def sound():
    winsound.PlaySound('*', winsound.SND_ALIAS)


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
            b_list = create_list_big_break(inpt)
            for t in range(inpt):
                if t in b_list:
                    timer_for_aktiv()
                    timer_for_big_break()
                elif t == inpt-1:
                    timer_for_aktiv()
                    finished()
                else:
                    timer_for_aktiv()
                    timer_for_break()
        i = 2
