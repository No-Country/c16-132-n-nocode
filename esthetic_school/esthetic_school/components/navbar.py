import reflex as rx
from esthetic_school.styles.colors import Color
from esthetic_school.routes import Route
from esthetic_school.components.icon_button import icon_button

def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.avatar(src="/logo_icon.png", size="4", margin_x="2em", radius="full"),
                href="/",
            ),
            rx.hstack(
                icon_button(
                    # Profile
                    "circle-user",
                    "/profile",
                    "Perfil",
                ),
                icon_button(
                    # Courses
                    "graduation-cap",
                    "/courses",
                    "Cursos",
                ),
                icon_button(
                    # Info
                    "info",
                    "/tyc",
                    "Información",
                ),
                icon_button(
                    # Back
                    "arrow-left",
                    "url",
                    "Volver",
                ),
            ),
            # rx.spacer(),
            # rx.text("Esthetic School", margin_x="2em"),
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
        z_index="99999",
    )
