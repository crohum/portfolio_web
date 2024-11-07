import reflex as rx
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# WHO AM I, Resumen corto de porque me hago desarrollador.
def who_am_i() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Who am I ?",
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.spacer(),
                rx.button(
                    'Tell me more...',
                    #on_click=''
                ),
                padding_right=Size.BIG.value,
                width='100%'
            ),
            rx.text(
                "Soy un Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nunc nibh,"
                'tempus pretium leo feugiat, cursus luctus est. Vestibulum nec dignissim enim.'
                'Mauris vitae nulla tortor. Sed convallis, sem vel efficitur tempus,'
                'eros felis facilisis nulla, sit amet iaculis velit tortor eu tellus.'
                'Vestibulum cursus enim lorem, et sollicitudin ante dapibus vitae.'
                'Duis metus mauris, mollis sed sodales ac, faucibus sit amet ante.'
                'In commodo suscipit elit, eu aliquet ante varius nec.',
                color=TextColor.SECUNDARIO.value,
                padding_bottom=Size.MEDIUM.value
            ),
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
