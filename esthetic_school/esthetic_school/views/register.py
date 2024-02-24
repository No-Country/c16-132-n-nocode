import reflex as rx

from esthetic_school.components.common_button import common_button
from esthetic_school.routes import Route
from esthetic_school.styles.styles import Size

@rx.page(route=Route.REGISTER, title="Registro")
def register() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.input(placeholder="Nombre/s", name="name", size="3"),
            rx.input(placeholder="Apellido/s", name="last_name",size="3"),
            rx.input(placeholder="Email@email.com", name="email", size="3"),
            common_button("url", "Enviar", True),
            align="center",
            spacing=Size.MEDIUM.value
        ),
    )
