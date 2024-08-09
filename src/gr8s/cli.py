from typing import List, Dict, Callable
import curses

class CLIMenu:
    def __init__(self, menu_options: Dict[str, Callable]):
        self.options: List[str] = list(menu_options.keys())
        self.callables: List[Callable] = list(menu_options.values())

    def display(self):
        curses.wrapper(self.display_menu)

    def display_menu(self, stdscr):
        curses.curs_set(0)  # Hide cursor
        current_selection = 0
        prev_selection = -1

        stdscr.clear()
        while True:
            if current_selection != prev_selection:
                stdscr.clear()
                for i, option in enumerate(self.options):
                    if i == current_selection:
                        stdscr.addstr(f"> {option}\n", curses.A_REVERSE)  # Highlight selected option
                    else:
                        stdscr.addstr(f"  {option}\n")
                stdscr.refresh()
                prev_selection = current_selection

            key = stdscr.getch()

            if key == curses.KEY_UP or key == ord('k'):
                current_selection = (current_selection - 1) % len(self.options)
            elif key == curses.KEY_DOWN or key == ord('j'):
                current_selection = (current_selection + 1) % len(self.options)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                selected_callable = self.callables[current_selection]
                output: str = selected_callable()
                if not output.endswith("\n"):
                    output += "\n"

                stdscr.clear()
                stdscr.addstr(output)
                stdscr.addstr("Press any key to return to the menu.")
                stdscr.refresh()
                stdscr.getch()

                # After displaying output, reset the previous selection
                prev_selection = -1

            elif key == ord('q'):
                break

        curses.endwin()

if __name__ == "__main__":
    def up(c: str) -> str:
        return c.upper()

    cm = CLIMenu(
        {
            "a": up,
            "b": up,
        }
    )
    cm.display()
