import reflex as rx
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH_SKILLS, Color, TextColor, Font


# Class to add each softskill's images n descriptions.
class ForeachState(rx.State):
    softskills : dict[str, str] = {
        # Todo este texto lo puedo poner en un txt, para no dejarlo en codigo.
        'teamwork' : 'uno, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'leadership' : 'dos, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'conflict_management' : 'tres, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'time_management' : 'cuatro, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo', #time normalization with three point estimation
        'adaptability' : 'cinco, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'communication' : 'seis, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'continuos_learning' : 'siete, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'creativity' : 'ocho, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        'problem_solving' : 'nueve, necesito un texto largo donde platico como ese softskill fue utilizado en una experiencia previa, como en un proyecto o en un trabajo y que si lo tengo/uso/poseo',
        # 'critical_thinking'
    }


# Crea los cuadros de la lista pasando el dict como lista.
def grid_dict(skill: List):
    return rx.box(
        rx.hstack(
            rx.image(
                src=f"/skills/{skill[0]}.png",
                width=rx.breakpoints(xs=Size.VERY_BIG.value, md=Size.GARGANTUAL.value, lg=Size.COLOSAL.value),
                height='auto'
            ),
            rx.text(skill[1])
        ),
        padding=Size.DEFAULT.value
    )


# Funcion que se manda al main para ejecutar, Contiene los logos y descripcion.
def skills():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    'Abilities & Softskills',
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.VERY_BIG.value,
                    padding_top=Size.DEFAULT.value
                ),
                rx.grid(
                    rx.foreach(
                        ForeachState.softskills,
                        grid_dict
                    ),
                    columns=rx.breakpoints(xs='1', md='2', lg='3')
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.text(
                        '*This section has been designed using resources from Flaticon.com',
                        color=TextColor.SECUNDARIO.value,
                        padding_y=Size.DEFAULT.value
                    ),
                    width='100%'
                ),
                style=MAX_WIDTH_SKILLS
            )
        ),
        bg=Color.TERCIARIO.value,
        padding=Size.DEFAULT.value,
        width='100%'
    )
