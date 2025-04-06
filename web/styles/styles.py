import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

STYLESHEETS = []

#constants
MAX_WIDTH="600px"

#sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    LARGE = "4"
    BIG = "5"

 
STYLESHEETS =[
    "https://fonts.googleapis.com/css?family=Roboto:wght@300&display=swap"
]

#styles

BASE_STYLE ={
    "font_family": Font.DEFAULT.value, #fuente general
    "background_color": Color.BACKGROUND.value, #color de fondo general
    "scroll_behavior": "smooth",  # Habilita el desplazamiento suave
}

#estilo del navbar
navbar_style = {
    "display": "flex",  # Usa flexbox
    "align-items": "center",  # Alinea verticalmente
    "justify-content": "space-between",  # Distribuye los elementos a los extremos
    "width": "100%",  # Ocupa todo el ancho
    "padding": "10px 20px",  # Espaciado interno
    "position": "absolute",  # Posición absoluta dentro del header
    "top": "0",  # Posición superior
    "margin-bottom": "50px",  # Espacio debajo del navbar
}

# Estilo de los enlaces del navbar
navbar_link_style = {
    "color": "white",  # Color del texto
    "text-decoration": "none",  # Sin subrayado
    "font-size": "15px",  # Tamaño de fuente
    "font-weight": "bold",  # Negrita
    "padding": "5px 10px",  # Espaciado interno
    "border-radius": "5px",  # Bordes redondeados
    "transition": "background-color 0.3s",  # Transición suave
    "_hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",  # Fondo al pasar el mouse
    },
}

# Estilo del contenedor de los enlaces
navbar_links_container_style = {
    "display": "flex",  # Usa flexbox
    "gap": "20px",  # Espaciado entre los enlaces
}

# Estilo de los enlaces del navbar
navbar_link_style = {
    "color": "white",  # Color del texto
    "text-decoration": "none",  # Sin subrayado
    "font-size": "15px",  # Tamaño de fuente
    "font-weight": "bold",  # Negrita
    "padding": "5px 10px",  # Espaciado interno
    "border-radius": "5px",  # Bordes redondeados
    "transition": "background-color 0.3s",  # Transición suave
    "_hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",  # Fondo al pasar el mouse
    },
}

#estilo del texto de la descripcion del banner
banner_description_style = dict(
    font_size = "40px",
    font_weight = "bold",
    font_family= "'Helvetica Neue', Arial, sans-serif",
    color="#eeeef3",
    margin_left = "60px",
    
)
# estilo del banner
banner_container_style = dict (
    background_image = "url('/banner.png')",
    background_size = "cover",
    background_position = "center",
    height = "auto",
    width = "100%",
)