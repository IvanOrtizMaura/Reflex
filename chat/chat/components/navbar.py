import reflex as rx

import chat.chat.state as State

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(
                    tag="hambuger",
                    mr=4,
                )
            )
        )
    )