import reflex as rx
from portfolio_web.componentes.estilos import Size, MAX_WIDTH, Color, TextColor, Font


def cuarentas() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "Why change to I.T. at my 40's",
                    style={'font_family' : Font.TITULOS.value},
                    font_size=Size.BIG.value,
                    color=TextColor.PRIMARIO.value
                ),
                rx.box(
                    rx.spacer(padding=Size.SMALL.value),
                    rx.text(
                        "After working and growing for 10 years in the same company ",
                        "as an industrial engineer, I asked myself if this is what I ",
                        "wanted to do for the rest of my working life, Then I started ",
                        "to search and try options and I rediscovered my passion for programming."
                    ),
                    rx.spacer(padding=Size.SMALL.value),
                    rx.text(
                        "I know that my previous experience will help me as a basement ",
                        "in this new work stage. Because, now I want to be like a dolphin ",
                        "who learned to program.",
                    ),
                    color=TextColor.SECUNDARIO.value,
                    padding=Size.MEDIUM.value
                )
            ),
            rx.vstack(
                rx.image(
                    src="/otros/Turo.png",
                    width="200px",
                    height="auto"
                ),
                rx.text(
                    'Professor Turo from Pokémon',
                    color=TextColor.TERCIARIO.value,
                    font_size=Size.MEDIUM.value
                )
            )
        ),
        bg=Color.SECUNDARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )


def dolphin() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "A Dolphin (or Whale) Metaphor",
                style={'font_family' : Font.TITULOS.value},
                font_size=Size.BIG.value,
                color=TextColor.DESTACADO.value
            ),
            rx.box(
                rx.text(
                    "If you ask me: —Why after almost 20 years working in the industry, ",
                    "and in my 40's, make a big change and switch to IT?",
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "My short answer would be: —I'm in the middle of my working life, ",
                    "I have more time left to work than the time I have worked and I ",
                    "want to do it in something I like."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "My long answer is: —Think of a dolphin (or a whale), a marine mammal animal."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "All animals in their origins, were multicellular organisms, some decided ",
                    "stay in sea, but many others decided to leave the water and adapt to land, ",
                    "millions of years later, they became mammals, so, the dolphin (or whale) was ",
                    "an animal that adapted to land life, became a mammal and after that, it said: ",
                    "—No, it's not what I want. —And then it went back to the sea."
                ),
                rx.spacer(padding=Size.SMALL.value),
                rx.text(
                    "Despite its “late start” in adapting to the ocean, the dolphin is considered ",
                    "one of the most intelligent animals, and the whale is the largest animal in ",
                    "the world."
                ),
                rx.spacer(padding=Size.SMALL.value),
                color=TextColor.PRIMARIO.value
            ),
            rx.hstack(
                rx.image(
                    src="/otros/palafin.png",
                    width="auto",
                    height=rx.breakpoints(xs="50px", sm="100px")
                ),
                rx.text(
                    "So, I want to be like a dolphin, I want to make it in the world of programming, ",
                    "even though I didn't start at the same time as most of the other people."
                ),
                rx.image(
                    src="/otros/wailord.png",
                    width="auto",
                    height=rx.breakpoints(xs="50px", sm="100px")
                ),
                color=TextColor.PRIMARIO.value
            ),
            rx.hstack(
                rx.text(
                    'Palafin from Pokémon',
                    color=TextColor.SECUNDARIO.value,
                    font_size=Size.MEDIUM.value
                ),
                rx.spacer(),
                rx.text(
                    'Wailord from Pokémon',
                    color=TextColor.SECUNDARIO.value,
                    font_size=Size.MEDIUM.value
                ),
                width='100%'
            )
        ),
        bg=Color.TERCIARIO.value,
        padding=Size.BIG.value,
        border_radius='25px',
        style=MAX_WIDTH
    )
