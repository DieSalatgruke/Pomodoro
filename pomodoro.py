import time
import json
import sys
import tkinter as tk

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
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)


def get_timer_config():
    with open(CONFIG_DATA, 'r') as cd:
        config_data = json.load(cd)
        return config_data


def request(inp):
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


def timer_to_pomodoro(interval_intensity):
    while interval_intensity > 1:
        make_it_beauty()
        print('Aktivezeit')
        make_it_beauty()
        countdown(_aktiv())

        make_it_beauty()
        print('Pause')
        make_it_beauty()
        countdown(_break())

        interval_intensity -= 1

        if interval_intensity == 3 or interval_intensity == 6 or interval_intensity == 9 or interval_intensity == 12:
            make_it_beauty()
            print('Aktivezeit, gleich kommt die große Pause!')
            make_it_beauty()
            countdown(_aktiv())

            make_it_beauty()
            print('Große Pause')
            make_it_beauty()
            countdown(_big_break())

            interval_intensity -= 1

        elif interval_intensity == 1:
            make_it_beauty()
            print('Letzte Aktivezeit')
            make_it_beauty()
            countdown(_aktiv())
            finished()


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
            timer_to_pomodoro(inpt)
            i = 2

