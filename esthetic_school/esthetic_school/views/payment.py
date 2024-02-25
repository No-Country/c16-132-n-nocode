import reflex as rx

from esthetic_school.components.navbar import navbar
from esthetic_school.components.common_button import common_button
from esthetic_school.components.heading import heading

def payment() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            heading("Pagar")
        )
    )