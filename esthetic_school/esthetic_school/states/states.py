import reflex as rx
import json
import os

from esthetic_school.components.course_card import course_card

ruta = '/home/franco/Desktop/c16-132-n-nocode/esthetic_school/esthetic_school/states/courses.json'
def load_courses_file():
    with open(ruta) as file:
        return json.load(file)


def course_information(course):
    return  course_card(
        os.path.join('esthetic_school', 'assets', 'courses_img', f'{course["image"]}'),
        f'{course["name"]}',
        f'{course["description"]}',
        'url'
    )

def show_information() -> rx.Component:
    courses = load_courses_file()
    return rx.center(
        rx.grid(
            *[course_information(course) for course in courses],
            columns="6",
            rows="4",
            spacing="4",
            position="absolute",
            top="6em",
            
        ),
        
        align="center",
        justify="center",
        width="100%"
    )

"""
def course_component(course):
    return rx.component(
        rx.box(
            rx.img(src=f"images/{course['image']}", width=100),
            rx.p(course["name"]),
            rx.p(course["description"]),
        )
    )
"""



