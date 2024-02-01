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
            _min_nav.visible = True
            _min_nav.update()
        else:
            _nav.controls[0].visible = True
            _nav.update()
            _min_nav.controls.visible = False
            _min_nav.update()

    # hover of nav items
    def _change_text_color(e):
        if e.control.content.color == 'white':
            e.control.content.color = '#FFC125'
            e.control.content.update()
        else:
            e.control.content.color = 'white'
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
                                color="white",
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'Contact',
                                weight="w600",
                                color="white"
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'Services',
                                weight="w600",
                                color="white"
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                'Privacy Policy',
                                weight="w600",
                                color="white"
                            ),
                        ),
                    ],
                ),
            ),
        ],
    )

    # Mini Navbar
    _min_nav = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='About Us'),
                    PopupMenuItem(text='Constact'),
                    PopupMenuItem(text='Services'),
                    PopupMenuItem(text='Privacy Policy'),
                ],
            ),
        ],
    )

    # title
    _title = ResponsiveRow(
        alignment = "center",
        controls=[
            Container(
                col={'xs': 12, 'sm': 10, 'md': 10, 'lg': 10, 'xl': 12},
                alignment=alignment.top_center,
                padding=20,
                content=Text(
                    'MetzkerTech\nPortfolio & Projects',
                    size=45,
                    width="w600",
                    text_align='center',
                ),
            ),
        ],
    )


    #  title heading
    _sub_title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={'xs': 12, 'sm': 10, 'md': 10, 'lg': 10, 'xl': 12},
                padding=20,
                alignment=alignment.top_center,
                content=Text(
                    'Welcome to our webpage/portifolio!\nHave a look around and contact us if you find something interesting.',
                    size=17,
                    text_align='center',
                    weight="w500",
                ),
            ),
        ],
    )


    # social media button
    _icon_list = [
        icons.FACEBOOK,
        icons.TIKTOK_SHARP,
        icons.SHARE_SHARP,
    ]

    _social_button = Container(
        padding=20,
        content=Row(
            alignment='center',
        ),
    )

    for icon in _icon_list:
        _icon = IconButton(
            icon=icon,
            icon_size=12,
            icon_color='white',
            offset=transform.Offset(0, -0.9),
            animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
            animate_opacity=200,
            opacity=0,
        )
        _social_button.content.controls.append(_icon)

    _test_icons = Container(
        content=Row(
            alignment=alignment.center,
            controls=[
                Icon(name=icons.FACEBOOK, color=colors.WHITE, size=30),
                Icon(name=icons.TIKTOK_OUTLINED, color=colors.WHITE, size=30),
                Icon(name=icons.SHARE_SHARP, color=colors.WHITE, size=30),
            ]
        )
    )

    _icon_container = Container(
        width=145, 
        height=50,
        bgcolor='blue800',
        border_radius=8,
        content=Column(
            spacing=0,
            controls=[
                _test_icons,
            ],
        ),
    )

    # main column
    _main_col = Column(horizontal_alignment="center")
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)
    _main_col.controls.append(_sub_title)
    _main_col.controls.append(_icon_container)

    # bg container
    _background = Container(
        expand=True,
        height=page.height,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#0f1720"],
        ),
        content=_main_col,
    )
    
    page.add(_background)
    page.on_resize = on_resize

if __name__ == "__main__":
    flet.app(target=main)