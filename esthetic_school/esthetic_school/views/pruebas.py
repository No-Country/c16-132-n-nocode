import reflex as rx

from esthetic_school.views.wellcome import wellcome 
from esthetic_school.views.course import course
from esthetic_school.views.register import register
from esthetic_school.views.payment import payment 
from esthetic_school.states.states import show_information
from esthetic_school.views.terms_conditions import terms_conditions

def pruebas() -> rx.Component:
    return rx.center(
        terms_conditions(),
        width="100%",
        height="100vh",
        align="center",
        justify="center",
        #bg="blue"
    )