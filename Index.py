from flet import *
import random

book_name = 'Ivana emprende libro 4 sin animacion'
book_page = '0'

class Input(GestureDetector):
    def __init__(self,top,left):
        print("gesture created", top,left)
        super().__init__()
        self.mouse_cursor=MouseCursor.MOVE
        self.on_vertical_drag_update=self.drag()
        self.top=0
        self.left=0
        self.content=Container(bgcolor=colors.BLUE, width=100, height=100)


    # async def drag(e: DragEndEvent):
    #     print("aqui anda")
    #     # top=0
    #     # left=0
    #     # if e.control.top != Number and e.control.left != Number:
    #     #     top=e.control.top
    #     #     left=e.control.left

    #     e.control.top = max(0, e.control.top + e.delta_y)
    #     e.control.left = max(0, e.control.left  + e.delta_x)
    #     await e.control.update_async()

def main(page: Page):
    async def drag(e: DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd = []
    stack=(Stack(gd))

    def ran():
        ran= random.uniform(0,500)
        print(ran)
        return ran
    
    def add_input(top,left,color):
   
        stack.controls.append(
            GestureDetector(
                mouse_cursor=MouseCursor.MOVE,
                on_vertical_drag_update=drag,
                top=0,
                left=0,
                content=Container(bgcolor=color, width=top, height=50),
                )
        )
        # input = Input(top,left)
        # page.add(Stack([input]))
        page.update()
    
    def clear(page:Page):
        page.clean()
        page.update()
    
    page.theme_mode = 'dark'
    page.add(

            ElevatedButton("input",on_click=lambda _:add_input(200,200, colors.AMBER)),
            ElevatedButton("input",on_click=lambda _:add_input(100,100, colors.BROWN)),
            stack
        

            # Row([
            #     FloatingActionButton(icon=icons.ARROW_BACK_SHARP, bgcolor='grey', data=False, on_click=change_page),
            #     TextField(value=book_page, text_align="center", color="#FFFFFF", width=100,text_size=40),
            #     FloatingActionButton(icon=icons.ARROW_FORWARD_SHARP, bgcolor='grey', data=True, on_click=change_page)

            # ])
    )
    page.update()

app(main)