import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

state = State()

def main(page: ft.Page):
    page.title = "Flet Brush"
    canvas="" 

    def clicked(e):
        canvas = e.control.content
        print(canvas.shapes.append(
            cv.Line(
                0, 0, 100, 100, paint=ft.Paint(stroke_width=1)
            )
        ))
        canvas.update()

    def pan_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        #print(e.control)
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=1)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    # def pan_start2(e: ft.DragStartEvent):
    #     print("asñldkasñdk")
    #     state.x = e.local_x
    #     state.y = e.local_y

    # def pan_update2(e: ft.DragUpdateEvent):
    #     print("aslñdjañsldmañslmdsñalm")
    #     cp2.shapes.append(
    #         cv.Line(
    #             state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
    #         )
    #     )
    #     cp2.update()
    #     state.x = e.local_x
    #     state.y = e.local_y

    cp=cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.colors.GREY, ft.colors.GREY]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    cp2 = cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.colors.GREY, ft.colors.GREY]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    # async def drag(e: ft.DragEndEvent):
    #     e.control.top = max(0, e.control.top + e.delta_y)
    #     e.control.left = max(0, e.control.left + e.delta_x)
    #     e.control.update()

    page.window.width=1000
    page.window.height=1000
    page.theme_mode=ft.ThemeMode.LIGHT
    page.add(
            ft.Container(
                cp,
                border_radius=5,
                width=100,
                height=100,
                expand=True,
                on_click=clicked
                
            ),
            ft.Container(
                cp2,
                border_radius=5,
                width=100,
                height=100,
                expand=True,
                on_click=clicked
                
            )
    )


ft.app(main)