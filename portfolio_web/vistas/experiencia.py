import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


# EXPERIENCE, un bloque con un resumen de mi experiencia laboral y un boton para el cv.
def experience() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Work Experience",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.PRIMARIO.value
            ),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nunc nibh, "
                'tempus pretium leo feugiat, cursus luctus est. Vestibulum nec dignissim enim. '
                'Mauris vitae nulla tortor. Sed convallis, sem vel efficitur tempus, '
                'eros felis facilisis nulla, sit amet iaculis velit tortor eu tellus. '
                'Vestibulum cursus enim lorem, et sollicitudin ante dapibus vitae. '
                'Duis metus mauris, mollis sed sodales ac, faucibus sit amet ante. '
                'In commodo suscipit elit, eu aliquet ante varius nec.',
                color=TextColor.SECUNDARIO.value,
                padding=Size.MEDIUM.value
            ),
            rx.hstack(
                rx.button(
                    'Download CV',
                    on_click=rx.download(url='/downloads/alejandro_garcia_salazar_cv.pdf'),
                    size='3'
                ),
                rx.button(
                    'View on ',
                    rx.box(
                        class_name=f"fa fa-linkedin"
                    ),
                    href=Links.LINKEDIN_URL,
                    is_external=True,
                    size='3'
                )
            )
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
