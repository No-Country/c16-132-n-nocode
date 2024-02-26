import reflex as rx

from esthetic_school.views.course import course 

def pruebas() -> rx.Component:
    return rx.center(
        course(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )