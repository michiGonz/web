import reflex as rx
import web.styles.styles as styles
from web.styles.styles import Size as Size
from web.views.header.header import header

class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                header(),
                width="100%", 
                max_width="100%",
                margin_y=Size.BIG.value
            ),
        ),
)


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="FefiDev | Mis Proyectos",
    description="Hola mi nombre es stef, soy ingeniero de software y aqui encontraras mi portafolio de proyectos",
    image="logo.png"
    ),


