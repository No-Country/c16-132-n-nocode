import reflex as rx

from esthetic_school.views.register import register

def pruebas() -> rx.Component:
    return rx.center(
        register(),
        width="100%",
        height="100vh",
        align="center",
        justify="center"
    )