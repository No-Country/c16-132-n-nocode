import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route
from esthetic_school.views import navbar

@rx.page(
    route=Route.COURSES,
    title="Esthetic School - Cursos",
    image="logo_mini.svg"
)


def courses() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.section(
                rx.heading("Curso 1"),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                rx.button("Ver más")
            ),
            rx.section(
                rx.heading("Curso 1"),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                rx.button("Ver más")
            ),
            rx.section(
                rx.heading("Curso 1"),
                rx.image(
                    src="/curso1.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text("Descripción breve del curso 1"),
                rx.button("Ver más")
            )
        )
    )