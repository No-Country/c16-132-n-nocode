import reflex as rx
from esthetic_school.routes import Route
from esthetic_school.components.navbar import navbar
from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.states.states import show_information


@rx.page(
    route=Route.COURSES.value, title="Esthetic School - Cursos", image="logo_mini.svg"
)
def courses() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            show_information()
        ),
        bg="red",
        width="100%",
        margin_y="10em",
    )
