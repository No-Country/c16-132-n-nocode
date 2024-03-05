import reflex as rx
import json

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route
from esthetic_school.states.states import course_information

ruta_img = "/home/franco/Desktop/c16-132-n-nocode/esthetic_school/assets/courses_img/laminado_cejas1.jpg"

@rx.page(route="/course", title="Curso")

def course() -> rx.Component:
    #course_id = CourseState.show_curse
    #course_data = get_course_data(course_id)
    #print(course_id)    
    return rx.center(
        navbar(),
        rx.vstack(
            rx.avatar(
                rx.image(
                    src="/courses_img/laminado_cejas1.jpg"
                ),
                size="9"
            ),
            heading("Nombre del curso", True),
            rx.center(
                rx.vstack(
                    rx.text(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum vehicula sapien, vel malesuada quam tristique ac. Nullam consequat nibh nec libero varius, quis bibendum sem fermentum. Phasellus lobortis nisi nec nulla venenatis, ut posuere risus accumsan. Curabitur rutrum elit vel risus convallis, sed malesuada justo posuere.",
                        size="4"
                    ),
                    rx.text.strong(
                        "Precio: $15.000",
                        size="4"
                    ),
                ),
                align="center",
                justify="center",
                width="50%"
            ),
            common_button("/pagos", "Obtener el curso"),
            align="center",
            justify="center",
            margin_y="8em",
            #course_id = int(request.params["course_id"])
        )
    )

# ruta = '/home/franco/Desktop/c16-132-n-nocode/esthetic_school/esthetic_school/states/courses.json'
# def load_courses_file():
#     with open(ruta) as file:
#         return json.load(file)
    
# def get_course_data(course_id: int):
#     courses = load_courses_file()
#     return next((course for course in courses if f"{CourseState.show_curse == course["id"]}"), None)
