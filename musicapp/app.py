#!/usr/bin/env python3
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
    curses.curs_set(1)      # The cursor is visible
    stdscr.addstr(1, 2, "Artist name: (Crtl-G to search)")

    editwin = curses.newwin(1, 40, 3, 3)
    rectangle(stdscr, 2, 2, 4, 44)
    stdscr.refresh()

    box = Textbox(editwin)
    box.edit()

    criteria = box.gather()

    return criteria

def clean_screen(stdscr):
    """ Helper function to clean the screan
    """
    stdscr.clear()
    stdscr.refresh()


def main(stdscr):
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    _data_manager = DataManager()

    criteria = show_search_screen(stdscr)
    height, width = stdscr.getmaxyx()

    albums_panel = Menu(
        'List of album for the selected artist', (height, width, 0, 0)
    )
    tracks_panel = Menu(
        'List of tracks for the selected album', (height, width, 0, 0)
    )
    artist = _data_manager.search_artist(criteria)
    albums = _data_manager.get_artist_album(artist['id'])

    clean_screen(stdscr)
    albums_panel.items = albums
    albums_panel.init()
    albums_panel.update()
    albums_panel.show()

    current_panel = albums_panel

    is_running = True
    while is_running:
        curses.doupdate()
        curses.panel.update_panels()

        key = stdscr.getch()
        action = current_panel.handle_events(key)

        if action is None:
            action_result = action()
            if current_panel == albums_panel and action_result is not None:
                _id, uri = action_result
                tracks = _data_manager.get_album_tracklist(_id)
                current_panel.hide()
                current_panel = tracks_panel
                tracks_panel.items = tracks
                tracks_panel.init()
                tracks_panel.show()
            elif current_panel == tracks_panel and action_result is not None:
                _id, uri = action_result
                _data_manager.play(uri)

        if key == curses.KEY_F2:
            current_panel.hide()
            criteria = show_search_screen(stdscr)
            artist = _data_manager.search_artist(criteria)
            albums = _data_manager.get_artist_album(artist['id'])

            clear_screen(stdscr)
            current_panel = albums_panel
            current_panel.items = albums
            current_panel.init()
            current_panel.show()

        if key == ord('q') or key == ord('Q'):
            is_running = False

        current_panel.update()


try:
    wrapper(main)
except KeyboardInterrupt:
    print("Thanks for using the app")
