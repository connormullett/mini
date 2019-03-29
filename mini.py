
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

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()


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
        main(stdscr)
    except Exception:
        traceback.print_exc()
    finally:
        teardown(stdscr)


if __name__ == '__main__':
    mini()

