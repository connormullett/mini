
import curses
import curses.ascii

from curses import wrapper


def backspace(stdscr, x, y):
    stdscr.delch(x, y - 1)
    stdscr.move(x, y - 1)


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.nl()
    stdscr.keypad(True)

    # not curses.getch
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == 127:
            x, y = stdscr.getyx()
            backspace(stdscr, x, y)
        else:
            stdscr.addch(c)
    curses.endwin()


if __name__ == '__main__':
    main()

