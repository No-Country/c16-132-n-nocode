import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route

@rx.page(
    title="Esthetic School - Bienvenida",
    image="simple_icon.png"
)

def wellcome() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Bienvenidos a", as_="h1", justify_content="center"),
                rx.image(
                    src="logo_grande.png",
                    alt="Logo de la aplicación el cual incluye una flor y el nombre Esthetic School",
                    width="16em",
                    heigth="16em"
                ),
                rx.text("Desarrolla tu destreza en estética con nuestra app de cursos especializados."),
                #seguramente el btn va a ser un link, ya que me debe llevar a los listados de los cursos
                rx.link(
                    rx.button(
                        "Continuar",
                    ),
                    href=Route.COURSES
                )
            ),
            width="100%",
            height="80vh"   
        )
    )