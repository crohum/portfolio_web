import reflex as rx
import portfolio_web.componentes.estilos as styles
from portfolio_web.vistas.navbar import navbar
from portfolio_web.vistas.header import header
from portfolio_web.vistas.footer import footer
from portfolio_web.vistas.quien_soy import who_am_i
from portfolio_web.vistas.tecnologias import technologies
from portfolio_web.vistas.experiencia import experience
from portfolio_web.vistas.habilidades import skills
from portfolio_web.vistas.proyectos import proyect
from portfolio_web.paginas.proyects import proyect_page
from portfolio_web.paginas.about_me import cuarentas, dolphin


# MAIN PAGE
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                who_am_i(),
                technologies(),
                experience()
            ),
        ),
        rx.spacer(padding=styles.Size.VERY_BIG),
        skills(),
        rx.spacer(padding=styles.Size.VERY_BIG),
        rx.center(
            proyect()
        ),
        rx.spacer(padding=styles.Size.COLOSAL),
        rx.spacer(padding=styles.Size.VERY_BIG),
        footer(),
    )


# PAGE with all proyects
def proyects():
    return rx.box(
        navbar(),
        rx.center(
            proyect_page(),
        ),
        footer()
    )


# Contact's information
def resume():
    return rx.box(
        navbar(),
        rx.text("Curriculum Vitae - RESUME"),
        footer()
    )


# Why change to IT at my 40's
def about():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.spacer(padding=styles.Size.BIG),
                cuarentas(),
                rx.spacer(padding=styles.Size.BIG),
                dolphin()
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.HOJA_ESTILO,
    style=styles.ESTILO_BASE
)

app.add_page(
    index,
    title='Alejandro Garcia Salazar - PORTFOLIO',
    description="Alejandro Garcia Salazar (Crohum)'s Portfolio website",
)
app.add_page(proyects, route='/proyects')
app.add_page(resume, route="/resume")
app.add_page(about)
