import reflex as rx

from esthetic_school.views.wellcome import wellcome 
from esthetic_school.views.login import login
from esthetic_school.views.courses import courses

def pruebas() -> rx.Component:
    return rx.center(
        login(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )