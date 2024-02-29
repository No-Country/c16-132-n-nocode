import reflex as rx

from esthetic_school.views.wellcome import wellcome 
from esthetic_school.states.states import show_information
from esthetic_school.views.courses import courses

def pruebas() -> rx.Component:
    return rx.center(
        courses(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )