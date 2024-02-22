import reflex as rx

def common_button(url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            variant="solid" if solid else "soft"
        ),
        href=url
    )