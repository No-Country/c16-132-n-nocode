import reflex as rx
from esthetic_school.styles.colors import Color


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.image(
                    src="favicon.ico",
                    alt="logo beauty school",
                    width="3em",
                    height="3em",
                    margin_x="2em",
                )
            ),
            # rx.spacer(),
            rx.text("Esthetic School", margin_x="2em"),
            top="0",
            bg="red",
            width="100%",
            height="4em",
            justify="between",
            align="center",
        ),
        width="100%",
    )
