import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route

# from esthetic_school.styles.styles import Size, BUTTON_STYLE
from esthetic_school.components.common_button import common_button
from esthetic_school.components.heading import heading
from esthetic_school.styles.styles import Separation_size, Size


@rx.page( route="wellcome", title="Esthetic School - Bienvenida", image="simple_icon.png")
def wellcome() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.vstack(
                heading("Bienvenidos a", True),
                rx.image(
                    src="/logo_fondo.jpeg",
                    alt="Logo de la aplicación el cual incluye una flor y el nombre Esthetic School",
                    width="15em",
                    heigth="25em",
                ),
                rx.text(
                    "Desarrolla tu destreza en estética con nuestra app de cursos especializados.",
                    size=Size.DEFAULT.value,
                ),
                common_button(Route.COURSES, "Continuar", True),
                margin_top="25%",
                align="center",
                spacing=Size.DEFAULT.value,
            ),
            direction="column",
        ),
        # bg="red",
        width="100%",
        align_items="center",
        justify="center",
        margin_y=Separation_size.SMALL.value,
    )
