from flet import *

class Item(GestureDetector):
    def __init__(self):
        super().__init__()
        self.content=Container(TextField(label="hola"),bgcolor="white",padding=10,width=100,height=50)
        self.mouse_cursor=MouseCursor.MOVE
        self.on_vertical_drag_update=self.drag()
        self.top=0
        self.left=0


class UI(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)
        self.gd=[]
        self.stacks=Stack(self.gd)
        self.items=(
            Container(
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
                                )
                            ],
                            on_change=lambda e: self.add_item()
                        )
                    ]
                )
            )
        )
        self.work_area=(
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
        self.container=Stack([
            ResponsiveRow(
                controls=[
                    self.items,
                    self.work_area
                ]
            ),
            self.stacks
        ])
    async def drag(e: DragEndEvent):
        print("asñldañsjd")
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    def add_item(self):
        print("asñldañsjd")
        self.stacks.controls.append(GestureDetector(
                mouse_cursor=MouseCursor.MOVE,
                on_vertical_drag_update=self.drag,
                top=0,
                left=0,
                content=Container(bgcolor=colors.AMBER, width=100, height=50),
                )
        )
        self.page.update()

    def build(self):
        return self.container
    




book_name = 'Ivana emprende libro 4 sin animacion'
book_page = '36'

book = [Image(src=f'../assets/{book_name}_{book_page}.png', width=100, height=100)]

def main(page: Page):
    page.window_min_height=720
    page.window_min_width=530
    page.theme_mode=ThemeMode.SYSTEM
    page.add(UI(page))

app(main)