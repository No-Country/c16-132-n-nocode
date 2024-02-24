import reflex as rx

from esthetic_school.components.common_button import common_button
from esthetic_school.routes import Route
from esthetic_school.styles.styles import Size
from esthetic_school.views.navbar import navbar
from esthetic_school.views.inferior_bar import inferior_bar


@rx.page(route=Route.REGISTER, title="Registro")
def register() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.vstack(
                rx.input(
                    placeholder="Nombre/s",
                    name="nombre",
                    size="3"
                ),
                rx.input(
                    placeholder="Apellido/s",
                    name="apellido",
                    size="3"
                ),
                rx.input(
                    placeholder="email@email.com",
                    name="email",
                    size="3"
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="contrasña",
                    size="3"
                ),
                rx.input(
                    placeholder="Confirmar contraseña",
                    name="confirmar_contraseña",
                    size="3"
                ),
                common_button(
                    "ulr",
                    "Enviar",
                    True
                ),
                align="center"
            ),
            spacing=Size.BIG.value,
            #bg="violet",
            width="100%",
            height="100vh",
            align="center",
            justify="center"
        ),
        inferior_bar(),
        width="100%",
        height="100vh",
        #spacing=Size.MEDIUM.value
        #bg="green"
    )