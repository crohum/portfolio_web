import reflex as rx
import portfolio_web.componentes.enlaces as Links
from portfolio_web.componentes.botones import boton_menu
from portfolio_web.componentes.estilos import Color, Size


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src='avatar.png',
                fallback='GSA',
                color_scheme='indigo',
                radius='full',
                border=f'solid, 2px, {Color.TERCIARIO.value}',
                size='3',
                spacing='3'
            ),
            rx.heading(
                "Alejandro G. S.'s portfolio"
            ),
            rx.spacer(),
            boton_menu(
                'home',
                'home',
                '',
                False
            ),
            boton_menu(
                'app-window-mac',
                'proyects',
                '',
                False
            ),
            boton_menu(
                'contact',
                'contact',
                '',
                False
            ),
            boton_menu(
                'braces',
                'about me',
                '',
                False
            ),
            boton_menu(
                'linkedin',
                'linkedin',
                Links.LINKEDIN_URL,
                True
            ),
            boton_menu(
                'github',
                'github',
                Links.GITHUB_URL,
                True
            ),
        ),
        bg=Color.PRIMARIO.value,
        position='sticky',
        padding_x=Size.MEDIUM.value,
        padding_y=Size.DEFAULT.value,
        z_index='999',
        border=f'3px solid {Color.SECUNDARIO.value}',
        top='0',
        width='100%'
    )
