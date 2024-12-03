import reflex as rx
from portfolio_web.componentes.estilos import Size, TextColor


# Crea los botones con nombre del navbar de forma responsiva.
def boton_menu(icon: str, name: str, url: str, ext: bool) -> rx.Component:
    return rx.link(
                rx.hstack(
                    rx.icon(
                        icon,
                        display=["flex", "flex", "flex", "flex", "flex"] if ext
                        else ["flex", "flex", "none", "flex", "flex"]
                    ),
                    rx.text(
                        name.upper(),
                        display=["none", "none", "none", "flex", "flex"] if ext
                        else ["none", "none", "flex", "flex", "flex"]
                    )
                ),
                href=url,
                is_external=ext,
                class_name='shake',
                color=TextColor.SECUNDARIO.value
                # Hace que tiemble al poner el cursor, usando CSShake v1.7.0
            ),


# Crea los botones del footer
def boton_footer(icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.box(
            class_name=f"fa fa-{icon}"
        ),
        href=url,
        is_external=True,
        size='8',
        class_name='shake',
        color=TextColor.PRIMARIO.value,
        padding_right=Size.SMALL.value
    )
