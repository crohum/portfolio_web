import reflex as rx
from typing import List
from portfolio_web.componentes.estilos import Size, MAX_WIDTH_SKILLS, Color, TextColor, Font


# Class to add each softskill's images n descriptions.
class ForeachState(rx.State):
    softskills : dict[str, str] = {
        # Todo este texto lo puedo poner en un txt, para no dejarlo en codigo.
        'teamwork' : 'Working well with others, having been in different parts of a process, has given me insight into understanding the needs of others and being able to work together.',
        'leadership' : 'I have been a supervisor for 5 years, leading up to 40 people, achieving objectives and improving processes, all this thanks to the good disposition of the people in my charge.',
        'conflict_management' : 'As a supervisor, during that time, I have had to mediate problems and conflicts among the workers, arriving at good resolutions.',
        'time_management' : 'Both as supervisor and coordinator, I needed to calculate the time of the tasks we had pending, using time normalization with three point estimation.',
        'adaptability' : 'In the perishable food industry, we rely on short-notice orders, so we have to adapt to the orders that come in on a daily basis and act accordingly.',
        'communication' : 'The implementation of Kanban boards in one of my jobs was precisely to create a model for effective communication between departments.',
        'continuos_learning' : 'I like to learn and apply my knowledge, I am constantly taking courses to develop my skills and knowledges.',
        'creativity' : "I like hobbies and activities that make me think in new ways and create unexpected solutions, I love LEGO, Board games, and that's why I like programming to.",
        'problem_solving' : 'During life, we all face different problems, from everyday life to work, in the world of board games, we define them as problems that we impose on ourselves to achieve a goal, and that is my philosophy of life.',
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
