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
                    rx.grid(
                        rx.image(
                            src='/techs/Python.png',
                            width='auto',
                            height='40px',
                        ),
                        rx.image(
                            src='/techs/reflex.png',
                            width='auto',
                            height='35px',
                            padding_x=Size.TINY.value,
                        ),
                        rx.image(
                            src='/visual code.png',
                            width='auto',
                            height='40px',
                        ),
                        columns=rx.breakpoints(xs='1', sm='2', md='3')
                    )
                )
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        'This website was built in Python with Reflex framework,',
                        ' and coded in Visual Studio Code by yours truly.',
                        padding=Size.ZERO.value
                    ),
                    rx.link(
                        rx.hstack(
                            rx.text('View the code. '),
                            rx.icon('external-link')
                        ),
                        href=Links.PORTFOLIO_URL,
                        is_external=True,
                        color=TextColor.SECUNDARIO.value
                    ),
                    padding=Size.ZERO.value
                ),
                padding_x=Size.BIG.value
            ),
            rx.spacer(),
            rx.card(
                rx.vstack(
                    rx.heading(
                        'Contact Me.! ',
                        style={'font_family' : Font.TITULOS.value},
                        font_size=Size.BIG.value,
                        color=TextColor.PRIMARIO.value
                    ),
                    rx.grid(
                        boton_footer(
                            'github',
                            Links.GITHUB_URL
                        ),
                        boton_footer(
                            'linkedin',
                            Links.LINKEDIN_URL
                        ),
                        columns=rx.breakpoints(xs='1', sm='2'),
                        align='center'
                    )
                ),
                variant='ghost'
            )
        ),
        bg=Color.DESTACADO.value,
        padding=Size.DEFAULT.value,
        width='100%',
        position='absolute',
        bottom='0'
    )
