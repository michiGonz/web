import reflex as rx
import web.styles.styles as styles

def link_icon(url: str, image: str)-> rx.Component:
    return rx.link(
        rx.image (
            src=image,
            width="20px"
        ),
    href=url,
    is_external=True
    )