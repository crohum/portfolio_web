import reflex as rx
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "I 'm",
                style={'font_family' : Font.NOTAS.value},
                padding_top=Size.TINY.value,
                font_size=Size.COLOSAL.value
            ),
            rx.heading(
                'ALEJANDRO Garcia Salazar',
                padding_top=Size.SMALL.value,
                font_size=Size.BIG.value,
                class_name='animate__animated animate__bounceInDown animate__slower --animate-delay: 1s'
                # Hacer que aparezca el nombre, usando Animate.css
            ),
            rx.text(
                '# I want to be: like a ',
                rx.link(
                    'Dolphin',
                    ''
                ),
                ' who learned to code.',
                font_size=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
                as_='p',
                color=TextColor.PRIMARIO.value
            ),
            rx.hstack(
                rx.text('Email:'),
                rx.box(
                    rx.text(' " crohum@hotmail.com " '),
                    border= f'solid, 3px, {Color.SECUNDARIO.value}'
                ),
                rx.link(
                    rx.icon(
                        'copy',
                        on_click=rx.set_clipboard("crohum@hotmail.com")
                        # Copia el correo al portapapeles al hacer click.
                    )
                ),
                color=TextColor.SECUNDARIO.value,
                padding_top=Size.DEFAULT.value
            ),
            rx.hstack(
                rx.text('Download traditional CV'),
                rx.link(
                    rx.icon(
                        'download',
                        #on_click=rx.download(href='')
                        # Descarga el archivo CV.pdf
                    )
                ),
                color=TextColor.SECUNDARIO.value,
                padding_top=Size.ZERO.value
            ),
            padding_left=Size.COLOSAL.value
        ),
        rx.image(
            src='perfil.png',
            width=['12em','14em','16em','18em','20em'],
            height='auto',
        ),
        bg=Color.PRIMARIO.value,
        padding=Size.BIG.value,
        style=MAX_WIDTH
    )
