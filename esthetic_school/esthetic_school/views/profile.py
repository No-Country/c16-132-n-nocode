import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route

@rx.page(
        route=Route.PROFILE,
        title="Perfil"
)

def profile() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            rx.vstack(
                rx.chakra.avatar(color_scheme="pink", size="8"),
                heading("Nombre", True),
                heading("mail@mail.com"),
            ),
            rx.divider(width="25%"),
            rx.hstack(
                common_button(
                    Route.LOGIN,
                    "Iniciar Sesion",
                ),
                common_button(Route.REGISTER, "Registrarse"),
            ),
            # bg='pink',
            width="50%",
            height="50vh",
            align="center",
            justify="center",
        ),
        align="center",
        width="100%",
        height="100vh",
    )
