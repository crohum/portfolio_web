import reflex as rx
import portfolio_web.componentes.estilos as styles
from portfolio_web.vistas.navbar import navbar
from portfolio_web.vistas.header import header
from portfolio_web.vistas.footer import footer
from portfolio_web.vistas.quien_soy import who_am_i
from portfolio_web.vistas.tecnologias import technologies


def index() -> rx.Component:
    # Pagina principal.
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                who_am_i(),
                technologies(),
                who_am_i(),
            ),
        ),
        footer(),
    )


app = rx.App(
    stylesheets=styles.HOJA_ESTILO,
    style=styles.ESTILO_BASE
)

app.add_page(
    index,
    title='Alejandro Garcia Salazar - PORTFOLIO',
    description="Alejandro Garcia Salazar (Crohum)'s Portfolio website"
)
