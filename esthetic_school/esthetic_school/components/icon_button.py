import reflex as rx

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "soft",
            margin_x="2em"
        ),
        href=url
    )