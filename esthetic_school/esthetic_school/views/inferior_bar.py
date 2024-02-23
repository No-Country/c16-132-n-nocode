import reflex as rx

def inferior_bar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.button(
                "boton1",
                margin_x="4em"
            ),
            rx.button(
                "boton1"
            ),
            rx.button(
                "boton1"
            ),
            rx.button(
                "boton1",
                margin_x="4em"
            ),
            bg="red",
            width="100%",
            height="4em",
            justify="between",
            align="center",
            bottom="0",
            spacing="8"
        ),
        width="100%"
    )