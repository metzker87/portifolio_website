# flet responsive website

# modules 
import flet
from flet import *

def main(page: Page):
    # Page title
    page.title = "MetzkerTech Portfolio"
    

    # navbar
    _nav = Row()

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