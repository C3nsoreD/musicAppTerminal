import curses
import curses.panel
from curses import wrapper
from curses.textpad import Textbox
from curses.textpad import rectangle

from client import Menu
from client import DataManager



def show_search_screen(stdscr):
    """ Handler function that builds a search box for the terminal player.
    """
    curses.curs_set(1)
    stdscr.addstr(1, 2, "Artist name: (Crtl-G to search)")

    editwin = curses.newwin(1, 40, 3, 3)
    rectangle(editwin, 2, 2, 4, 44)
    stdscr.refresh()

    box = Textbox(editwin)
    box.edit()

    criteria = box.gather()

    return criteria
