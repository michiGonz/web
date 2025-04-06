import reflex as rx
from web.styles.styles import Size as Size
from web.styles.colors import TextColor as TextColor
from web.components.link_icon import link_icon
from web.styles.colors import Color as Color
import web.styles.styles as styles

def header() -> rx.Component:
    return rx.section(
        rx.hstack(
            rx.hstack(
                rx.link("Home", href="/", style=styles.navbar_link_style),
                rx.link("About", href="#about-section", style=styles.navbar_link_style),
                rx.link("Skills", href="#skills-section", style=styles.navbar_link_style),
                rx.link("Projects", href="#project-section", style=styles.navbar_link_style),
                style=styles.navbar_links_container_style
            ),
            justify="between", 
            align="center",  
            style=styles.navbar_style  
        ),
        # Contenido del banner
        rx.box(
            rx.text("Hi 👋",  style=styles.banner_description_style, margin_top="20px"),
            rx.text("I'm a",  style=styles.banner_description_style, margin_top="0px"),
            rx.text("Web Developer", style=styles.banner_description_style, margin_top="0px"),
            rx.text("I build things for web", style=styles.banner_description_style, margin_top="0px"),
            rx.hstack(
                link_icon(
                    "https://github.com/michiGonz",
                    "/icons/squar.svg"      
                ),
                link_icon(
                    "https://linkedin.com/in/stephanie-gonzález-87303a1b6",
                    "/icons/linkedin.svg"
                ),
                link_icon(
                    "https://x.com/stephdev",
                    "/icons/twitter.svg"
                ),
                style={"gap": "10px","margin-left": "20px", "margin_left": "50px"}  # Añade espacio entre los iconos
            ), 
        ),
        style=styles.banner_container_style,
    )