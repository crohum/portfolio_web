import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.botones import boton_footer
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.heading(
                        'Crohum. 2024',
                        style={'font_family' : Font.TITULOS.value},
                        font_size='1.5em',
                        color=TextColor.PRIMARIO.value,
                        align_items='center'
                    ),
                    rx.hstack(
                        rx.image(
                            src='python.png',
                            width='40px',
                            height='auto'
                        ),
                        rx.image(
                            src='reflex.png',
                            width='35px',
                            height='auto'
                        ),
                        rx.image(
                            src='visual code.png',
                            width='40px',
                            height='auto'
                        )
                    )
                )
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        'This website was built in Python with Reflex framework,',
                        as_='span',
                        padding=Size.ZERO.value
                    ),
                    rx.text(
                        'and coded in Visual Studio Code by yours truly.',
                        as_='span',
                        padding=Size.ZERO.value
                    ),
                    rx.link(
                        rx.hstack(
                            rx.text('view the code. '),
                            rx.icon('arrow-up-right'),
                            href=Links.ENLACE,
                            is_external=True
                        )
                    ),
                    padding_bottom=Size.ZERO.value
                ),
                padding_x=Size.BIG.value
            ),
            rx.spacer(),
            rx.card(
                rx.vstack(
                    rx.heading(
                        'Contact Me ! ',
                        style={'font_family' : Font.TITULOS.value},
                        font_size=Size.BIG.value,
                        color=TextColor.PRIMARIO.value
                    ),
                    rx.hstack(
                        boton_footer(
                            'github',
                            Links.LINKEDIN_URL
                        ),
                        boton_footer(
                            'linkedin',
                            Links.LINKEDIN_URL
                        )
                    )
                ),
                variant='ghost'
            )
        ),
        bg=Color.DESTACADO.value,
        padding=Size.DEFAULT.value,
        width='100%',
    )
