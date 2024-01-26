# flet responsive website

# modules 
import flet
from flet import *

def main(page: Page):
    # Page title
    page.title = "MetzkerTech Portfolio"
    
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

    # main column
    _main_col = Column()
    _main_col.controls.append(_nav)


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


if __name__ == "__main__":
    flet.app(target=main)