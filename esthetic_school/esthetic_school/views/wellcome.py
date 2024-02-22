import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route
#from esthetic_school.styles.styles import Size, BUTTON_STYLE
from esthetic_school.components.common_button import common_button
from esthetic_school.components.heading import heading

@rx.page(
    title="Esthetic School - Bienvenida",
    image="simple_icon.png"
)

def wellcome() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.card(
                heading(
                    "Bienvenidos a",
                    True
                ),
                rx.image(
                    src="logo_grande.png",
                    alt="Logo de la aplicación el cual incluye una flor y el nombre Esthetic School",
                    width="20em",
                    heigth="30em",
                    margin_left="25%"
                ),
                rx.text("Desarrolla tu destreza en estética con nuestra app de cursos especializados.",
                        size="5"
                        ),
                common_button(
                    Route.COURSES,
                    "Continuar",
                    True
                ),
                margin_top="25%",
            ),
            width="100%",
            direction="column",
            justify="between",
        ),
        bg="red",
    )