# flet responsive website

# modules 
import flet
from flet import *

def main(page: Page):
    # Page title
    page.title = "MetzkerTech Portfolio"
    
    def on_resize(e):
        if page.width <= 730:
            _nav.controls[0].visible = False
            _nav.update()
        else:
            _nav.controls[0].visible = True
            _nav.update()

    # hover of nav items
    def _change_text_color(e):
        if e.control.content.color == 'black':
            e.control.content.color = 'white70'
            e.control.content.update()
        else:
            e.control.content.color = 'black'
            e.control.content.update()
    # navbar
    _nav = Row(
        alignment='end',
        controls=[
            Container(
                padding=padding.only(right=25),
                height=60,
                content=Row(
                    controls=[
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'About Us', 
                                weight="w600", 
                                color="black",
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'Contact',
                                weight="w600",
                                color="black"
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'Services',
                                weight="w600",
                                color="black"
                            ),
                        ),
                    ],
                ),
            ),
        ],
    )

    # title
    _title = ResponsiveRow(
        alignment = "center",
        controls=[
            Container(
                alignment=alignment.top_center,
                content=Text('MetzkerTech Portfolio'),
            ),
        ],
    )

    # main column
    _main_col = Column()
    _main_col.controls.append(_nav)
    _main_col.controls.append(_title)


    # bg container
    _background = Container(
        expand=True,
        height=page.height,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#B80d0c7"],
        ),
        content=_main_col,
    )
    
    page.add(_background)
    page.on_resize = on_resize

if __name__ == "__main__":
    flet.app(target=main)