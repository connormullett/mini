
import click
import curses

from curses import wrapper

'''
Make a file
Enter a shell like environment
Write text to file

Write over mode
Append mode
Edit Mode
'''

def main():
    stdscr = curses.initscr()
    curses.endwin()

@click.command()
@click.argument('f')
def mini(f):
    main()

