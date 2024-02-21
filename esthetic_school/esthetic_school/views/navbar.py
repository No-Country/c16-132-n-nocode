import reflex as rx
from esthetic_school.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(src="logo_mini.svg")
        ),
        position="sticky",
        bottom="0",
        z_index="999",
        bg=Color.PRIMARY.value
    )
