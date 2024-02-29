import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route
from esthetic_school.states.states import load_courses_file

"""def course_component(course_id: int):
    courses = load_courses_file() 
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return rx.center(
            navbar(),
            rx.vstack(
                rx.avatar(size="9"),
                heading(course['name'], True),
                rx.text(course['description']),
                common_button(Route.PAYMENT.value, "Ir a pagar"),
                align="center",
                justify="center",
                margin_y="8em"
            )
        )
    else:
        return rx.text("Curso no encontrado")"""



def course() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            rx.avatar(size="9"),
            heading("Curso 1", True),
            rx.text("Descripción del curso"),
            common_button(Route.PAYMENT.value, "Ir a pagar"),
            align="center",
            justify="center",
            margin_y="8em"
        )
    )
