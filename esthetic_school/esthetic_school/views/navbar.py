import reflex as rx
from esthetic_school.styles.colors import Color
from esthetic_school.routes import Route


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.image(
                    src="/logo_icon.png",
                    alt="logo beauty school",
                    width="3em",
                    height="3em",
                    margin_x="2em",
                ),
                href="/wellcome"
            ),
            # rx.spacer(),
            rx.text("Esthetic School", margin_x="2em"),
            bg="red",
            width="100%",
            height="4em",
            justify="between",
            align="center",
        ),
        top="0",
        align="start",
        justify="start",
        width="100%",
    )
