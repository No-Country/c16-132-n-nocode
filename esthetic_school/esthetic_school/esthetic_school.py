from rxconfig import config
import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.center(
        rx.text("Hola mudno")
    )


app = rx.App()
app.add_page(index)
