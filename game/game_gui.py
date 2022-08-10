import arcade.gui
import arcade

start_screen = arcade.gui.UIBoxLayout()
start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
start_screen.add(start_button.with_space_around(bottom=20))


quit_button = arcade.gui.UIFlatButton(text="Exit", width=200)
start_screen.add(quit_button)


@quit_button.event
def on_click(event):
    arcade.exit()
