import reflex as rx

from esthetic_school.components.navbar import navbar
from esthetic_school.components.red_button import red_button
from esthetic_school.components.green_button import green_button
from esthetic_school.components.heading import heading
from esthetic_school.styles.styles import Size
from esthetic_school.routes import Route


@rx.page(route="/pagos", title="Pagar")
def payment() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.vstack(
                heading("Pagar"),
                rx.divider(),
                rx.vstack(
                    rx.input(
                        placeholder="Numero de tarjeta",
                        name="credit_number",
                        size="3",
                        type="number",
                        required=True,
                        width="30.5em"
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Nombre del titular",
                            name="card_owner_name",
                            size="3",
                            required=True,
                            width="15em"
                        ),
                        rx.input(
                            placeholder="Apellido del titular",
                            name="card_owner_surname",
                            size="3",
                            required=True,
                            width="15em"
                        ),
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Codigo de seguridad",
                            name="security_code",
                            size="3",
                            type="password",
                            required=True,
                            width="15em",
                        ),
                        rx.input(
                            placeholder="Fecha de vencimiento",
                            name="due_date",
                            size="3",
                            type="date",
                            required=True,
                            width="15em",
                        ),
                    ),
                ),
                rx.hstack(
                    red_button("url","Cancelar"),
                    green_button("url", "Pagar"),
                ),
                align="center",
            ),
            spacing=Size.BIG.value,
            # bg="violet",
            width="100%",
            height="100vh",
            align="center",
            justify="center",
        ),
        # inferior_bar(),
        width="100%",
        height="100vh",
        # spacing=Size.MEDIUM.value
        # bg="green"
    )
