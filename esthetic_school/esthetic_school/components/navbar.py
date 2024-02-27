import reflex as rx
from esthetic_school.styles.colors import Color
from esthetic_school.routes import Route
from esthetic_school.components.icon_button import icon_button


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.image(
                    src="/logo_icon.png",
                    alt="logo beauty school",
                    width="3em",
                    height="3em",
                    margin_x="2em",
                ),
                href=Route.WELLCOME.value,
            ),
            rx.hstack(
                icon_button(
                    # Profile
                    "circle-user",
                    Route.PROFILE.value,
                    "",
                ),
                icon_button(
                    # Courses
                    "graduation-cap",
                    "/courses",
                    "",
                ),
                icon_button(
                    # Info
                    "info",
                    "url",
                    "",
                ),
                icon_button(
                    # Back
                    "arrow-left",
                    "url",
                    "",
                ),
            ),
            # rx.spacer(),
            #rx.text("Esthetic School", margin_x="2em"),
            bg=Color.PRIMARY.value,
            width="100%",
            height="4em",
            justify="between",
            align="center",
        ),
        position="fixed",
        top="0px",
        align="start",
        justify="start",
        width="100%",
    )
