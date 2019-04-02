
import click
import curses
import traceback

from curses import wrapper

'''
Make a file
Enter a shell like environment
Write text to file

Write over mode
Append mode
Edit Mode
'''


def backspace(stdscr, x, y):
    stdscr.delch(x, y - 1)
    stdscr.move(x, y - 1)


def start(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()


def main(stdscr):
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


def teardown(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


@click.command()
@click.argument('f')
def mini(f):
    stdscr = curses.initscr()
    try:
        start(stdscr)
        main(stdscr)
    except Exception:
        traceback.print_exc()
    finally:
        teardown(stdscr)


if __name__ == '__main__':
    mini()

