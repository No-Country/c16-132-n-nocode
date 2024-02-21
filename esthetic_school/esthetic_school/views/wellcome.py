import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route
from esthetic_school.styles.styles import Size, BUTTON_STYLE

@rx.page(
    title="Esthetic School - Bienvenida",
    image="simple_icon.png"
)

def wellcome() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.card(
                rx.heading(
                    "Bienvenidos a", 
                    size="8",
                    padding_bottom=Size.SMALL.value,
                    align="center"
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
                rx.link(
                    rx.button(
                        "Continuar",
                        style=BUTTON_STYLE,
                    ),
                    href=Route.COURSES,
                    margin_left="45%"
                ),
                margin_top="25%",
            ),
            width="100%",
            direction="column",
            justify="between",
        ),
        bg="red",
    )