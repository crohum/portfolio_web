import reflex as rx
from enum import Enum


class Size(Enum):
    # Utilizando en lugar de px, para que se ajuste al tamaño de texto.
    ZERO = '0px !important'
    TINY = '0.3em'
    SMALL = '0.5em'
    MEDIUM = '0.7em'
    DEFAULT = '1em'
    BIG = '2em'
    VERY_BIG = '2.5em'
    GARGANTUAL = '3em'
    COLOSAL = '4em'


class Color(Enum):
    DESTACADO = '#0033CC'
    PRIMARIO = '#000000'
    SECUNDARIO = '#202020'
    TERCIARIO = '#4682B4'


class TextColor(Enum):
    DESTACADO = '#0033CC'
    PRIMARIO = '#ffffff'
    SECUNDARIO = '#B0C4DE'
    TERCIARIO = '#4682B4'


class Font(Enum):
    TITULOS = 'Dancing Script'
    TEXTO = ''
    NOTAS = 'Qwitcher Grypen'


MAX_WIDTH = dict(
    align_items='start',
    padding_x=Size.BIG.value,
    width='100%',
    max_width='1000px'
)


MAX_WIDTH_SKILLS = dict(
    align_items='start',
    padding_x=Size.BIG.value,
    width='100%',
    max_width='1200px'
)


ESTILO_BASE = {
    'font_family': Font.TEXTO.value,
    'color': TextColor.PRIMARIO.value,
    'background': Color.PRIMARIO.value,
    rx.heading: {
        'color': TextColor.DESTACADO.value
    },
    rx.link: {
        'text_decoration': 'none',
        '_hover': {
            'color': TextColor.DESTACADO.value,
            'text_decoration': 'none'
        },
    },
    rx.button: {
        'background-color' : Color.DESTACADO.value,
        'variant' : 'solid',
        'margin_bottom': Size.DEFAULT.value,
        'height': Size.BIG.value,
        'color': TextColor.SECUNDARIO.value,
        '_hover': {
            'color': TextColor.TERCIARIO.value
        }
    }
}


# Fuentes y CSS's animations
HOJA_ESTILO = [
    # FONTS
    'https://fonts.googleapis.com/css?family=Qwitcher+Grypen&display=swap',
    'https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap'

    # CSS
    "https://csshake.surge.sh/csshake.min.css", # por alguna razon no esta funcionando el shake, necesito revisar si hubo cambios en la fuente.
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
]
