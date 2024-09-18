from flet import *


book_name = 'Ivana emprende libro 4 sin animacion'
book_page = '51'

class State:
    x: float
    y: float

state = State()

def main(page: Page):

    def pan_start(e: DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: DragUpdateEvent):
        cp.shapes.append(
            canvas.Line(
                state.x, state.y, e.local_x, e.local_y, paint=Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    app_bar=AppBar(
        leading=Icon(icons.PALETTE),
        leading_width=40,
        title=Text("AppBar Example"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED),
            IconButton(icons.FILTER_3),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Item 1"),
                    PopupMenuItem(),  # divider
                    
                ]
            ),
        ],
    )
    rail=Container(
        col=1.5,
        bgcolor="teal",
        border_radius=10,
        content=Column(
            controls=[
                NavigationRail(
                    expand=True,
                    bgcolor="teal",
                    destinations=[
                        NavigationDestination(
                            icon=icons.SHORT_TEXT_SHARP,
                            label="TextField"
                        ),
                        NavigationDestination(
                            icon=icons.CHECK_BOX_SHARP,
                            label="CheckBox"

                        ),
                        NavigationDestination(
                            icon=icons.DRAW_SHARP,
                            label="Canvas"
                        ),
                        
                    ],
                    on_change=lambda e: add_item(e)
                )
            ]
        )
    )
    work_area=(
        Container(
            col=10,
            bgcolor="teal",
            content=Column(
                controls=[
                    Container(
                        image_src=f"../assets/{book_name}_{book_page}.png",
                        image_fit=ImageFit.CONTAIN,
                        expand=True
                    )
                ]
            )
        )
    )
    stack=Stack(
        [
            ResponsiveRow(
                controls=[
                    rail,
                    work_area
                ]
            )
        ],
        expand=True
    )

    cp=canvas.Canvas(
        [
            canvas.Fill(
                Paint(
                    gradient=PaintLinearGradient(
                        (0, 0), (600, 600), colors=[colors.GREY, colors.GREY]
                    )
                )
            ),
        ],
        content=GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )
    
    async def drag(e: DragEndEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    def add_item(e):
        input=""
        index= e.control.selected_index 
        if index==0:
            input=GestureDetector(
                    mouse_cursor=MouseCursor.MOVE,
                    on_vertical_drag_update=drag,
                    top=500,
                    left=500,
                    content=Container(TextField(label=""), bgcolor=colors.AMBER, border_radius=10, padding=5, width=100, height=50),
                )
        elif index==1:
            input=GestureDetector(
                    mouse_cursor=MouseCursor.MOVE,
                    on_vertical_drag_update=drag,
                    top=500,
                    left=500,
                    content=Container(Checkbox(value=False), bgcolor=colors.AMBER, border_radius=10, padding=5, width=100, height=50),
            )
        elif index==2:
            input=GestureDetector(
                mouse_cursor=MouseCursor.MOVE,
                on_vertical_drag_update=drag,
                top=500,
                left=500,
                content=Container(cp,border_radius=25,width=100,height=100,expand=True)
            )

        stack.controls.append(input)
        page.update()
    
    page.window_min_height=720
    page.window_min_width=530
    page.theme_mode=ThemeMode.SYSTEM
    
    page.add(app_bar,stack)
    page.update()

    
app(main)