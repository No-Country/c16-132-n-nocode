import reflex as rx

from esthetic_school.views.profile import profile

def pruebas() -> rx.Component:
    return rx.center(
        profile(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )