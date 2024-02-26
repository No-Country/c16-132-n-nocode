import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route


@rx.page(route=Route.COURSE)
def course() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            rx.avatar(size="9"),
            heading("Curso 1", True),
            rx.text("Descripción del curso"),
            common_button(Route.PAYMENT, "Ir a pagar"),
            align="center",
            justify="center"
        )
    )
