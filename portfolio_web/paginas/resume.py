import reflex as rx


def curriculum() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src='/graphs/coord.png',
                width='250px'
            ),
            rx.image(
                src='/graphs/supv.png',
                width='250px'
            ),
            rx.image(
                src='/graphs/ctrqa.png',
                width='250px'
            ),
            rx.image(
                src='/graphs/facilt.png',
                width='250px'
            ),
        )
    )
