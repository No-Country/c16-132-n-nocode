import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.icon_button import icon_button
from esthetic_school.styles.styles import Separation_size


def course_card(
    img: str, heading_text: str, description: str, url: str
) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(src=img, width="4em", heigth="4em"),
            rx.heading(heading_text, as_="h4", size="4", align="center"),
            rx.text(description),
            icon_button("eye", url, "Ver más"),
            align="center",
            justify="center",
            spacing="2"
        ),
    )
