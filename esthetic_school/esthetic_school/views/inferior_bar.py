import reflex as rx
from esthetic_school.components.icon_button import icon_button

from esthetic_school.routes import Route

def inferior_bar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            icon_button(
                #Profile
                "circle-user",
                Route.REGISTER,
                "",
                True,
            ),
            icon_button(
                #Courses
                "graduation-cap",
                "url",
                "",
                True
            ),
            icon_button(
                #Info
                "info",
                "url",
                "",
                True
            ),
            icon_button(
                #Back
                "arrow-left",
                "url",
                "",
                True,
            ),
            bg="red",
            width="100%",
            height="4em",
            justify="between",
            align="center",
            bottom="0",
            spacing="8",
            position="sticky"
        ),
        width="100%"
    )