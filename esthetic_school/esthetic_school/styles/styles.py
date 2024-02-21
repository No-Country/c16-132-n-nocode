import reflex as rx
from enum import Enum
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"

BASE_STYLE = {
    "color": TextColor.ACCENT.value,
    "background": Color.PRIMARY.value,
}

HEADING_STYLE = {
    "color": TextColor.ACCENT.value,
    "font_size": "3em"
}

LINK_STYLE =  {
    "text_decoration": "none",
    "_hover": {
        "color": TextColor.ACCENT.value,
        "text_decoration": "none"
    }
}

BUTTON_STYLE = {
    "background": Color.PRIMARY.value,
    "margin_bottom": Size.DEFAULT.value,
    "height": Size.BUTTON.value,
    "color": f"{TextColor.BLACK.value} !important",
    "cursor":"pointer",
    "_hover": {
        "color": f"{TextColor.BLACK.value} !important",
        "background": f"{Color.TERTIARY.value} !important" 
    }
}


max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)