import reflex as rx
from esthetic_school.views.inferior_bar import inferior_bar
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route
from esthetic_school.views.navbar import navbar
from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button



@rx.page(
    route=Route.COURSES,
    title="Esthetic School - Cursos",
    image="logo_mini.svg"
)


def courses() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            inferior_bar(),
            rx.section(
                heading(
                    "Curso1"
                ),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                common_button(
                    "url",
                    "ver mas",
                )
            ),
            rx.section(
                heading(
                    "Curso1"
                ),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                common_button(
                    "url",
                    "ver mas",
                )
            ),
            rx.section(
                heading(
                    "Curso1"
                ),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                common_button(
                    "url",
                    "ver mas",
                )
            ),
            bg="violet",
            width="100%",
            align="center",
            justify="center"
        ),
        bg="green"
    )