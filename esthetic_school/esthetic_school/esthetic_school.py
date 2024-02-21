from rxconfig import config
import reflex as rx

from esthetic_school.views.wellcome import wellcome
from esthetic_school.views.courses import courses


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                wellcome()
            )
        )
    )

app = rx.App()
app.add_page(index)

