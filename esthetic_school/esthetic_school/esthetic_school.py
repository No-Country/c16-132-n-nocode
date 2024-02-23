from rxconfig import config
import reflex as rx

from esthetic_school.views.wellcome import wellcome
from esthetic_school.views.courses import courses


def index() -> rx.Component:
    return rx.center(
        wellcome()
    )

app = rx.App()
app.add_page(index)

