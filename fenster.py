def toast():
    from win10toast import ToastNotifier

    toast = ToastNotifier()
    toast.show_toast(
        f'Aktivezeit',
        f'240',
        #duration=20,
        threaded=True,
    )


if __name__ == '__main__':

    toast()
