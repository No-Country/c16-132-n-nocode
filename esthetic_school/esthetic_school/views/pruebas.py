import reflex as rx

from esthetic_school.views.login import login

def pruebas() -> rx.Component:
    return rx.center(
        login(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )