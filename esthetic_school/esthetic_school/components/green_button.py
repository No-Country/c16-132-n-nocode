import reflex as rx

from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.styles import styles

class GreenButtonState(rx.State):
    def show(self) -> rx.Component:
        #print("Operación Confirmada")
        return rx.window_alert("Operación Confirmada")

def green_button(url: str, text="", solid=False ) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            text,
            variant="solid" if solid else "ghost",
            style=styles.GREEN_BUTTON,
            on_click=GreenButtonState.show
        ),
        href="#"
    )