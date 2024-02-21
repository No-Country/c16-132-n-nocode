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
        rx.center(
            rx.vstack(
                rx.heading(
                    "Bienvenidos a", 
                    font_size=Size.MEDIUM.value,
                    padding_bottom=Size.SMALL.value
                ),
                rx.image(
                    src="logo_grande.png",
                    alt="Logo de la aplicación el cual incluye una flor y el nombre Esthetic School",
                    width="20em",
                    heigth="30em"
                ),
                rx.text("Desarrolla tu destreza en estética con nuestra app de cursos especializados."),
                #seguramente el btn va a ser un link, ya que me debe llevar a los listados de los cursos
                rx.link(
                    rx.button(
                        "Continuar",
                        style=BUTTON_STYLE
                    ),
                    href=Route.COURSES
                )
            ),
            padding_top="50%",
            width="100%",
            height="80%"   
        )
    )