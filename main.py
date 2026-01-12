import flet as ft

def main(page: ft.Page):
    page.title = "Kalkulyator"
    page.window_width = 350
    page.window_height = 550
    page.bgcolor = "#1a1a1a"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    result = ft.Text(value="0", color="white", size=40, text_align="right", weight="bold")

    def button_click(e):
        data = e.control.data
        if data == "C":
            result.value = "0"
        elif data == "=":
            try:
                expression = result.value.replace("x", "*").replace("÷", "/")
                # Avoid eval for safety in production, but okay for simple demo
                result.value = str(eval(expression))
            except Exception:
                result.value = "Error"
        elif data == "⌫":
            if len(result.value) > 1:
                result.value = result.value[:-1]
            else:
                result.value = "0"
        elif data == "+/-":
            if result.value.startswith("-"):
                result.value = result.value[1:]
            elif result.value != "0":
                result.value = "-" + result.value
        else:
            if result.value == "0" or result.value == "Error":
                result.value = data
            else:
                result.value += data
        
        page.update()

    def create_button(text, color="white", bg="#333333", data=None):
        if data is None:
            data = text
        
        return ft.Container(
            content=ft.Text(value=text, size=24, color=color),
            alignment=ft.alignment.center,
            width=70,
            height=70,
            bgcolor=bg,
            border_radius=ft.border_radius.all(35),
            on_click=button_click,
            data=data,
            ink=True,
        )

    # Use try-except to handle potential API differences smoothly or just use a simpler approach
    # Checking for border_radius helper availability
    try:
        br = ft.border_radius.all(35)
    except AttributeError:
        br = 35 # Some versions might accept int, others might need ft.BorderRadius(35,35,35,35)
        # To be safe, let's redefine create_button to use generic if needed or just patch it here
    
    # Redefine create_button to be safer
    def create_button_safe(text, color="white", bg="#333333", data=None):
        if data is None:
            data = text
        
        # Safe alignment
        align = ft.Alignment(0, 0)
        
        # Safe border radius
        try:
           radius = ft.border_radius.all(35)
        except:
           radius = ft.BorderRadius(35, 35, 35, 35)

        return ft.Container(
            content=ft.Text(value=text, size=24, color=color),
            alignment=align,
            width=70,
            height=70,
            bgcolor=bg,
            border_radius=radius,
            on_click=button_click,
            data=data,
            ink=True,
        )

    # Tugmalar qatori
    row1 = ft.Row(
        controls=[
            create_button_safe("C", color="red", bg="#3a1111"),
            create_button_safe("+/-"),
            create_button_safe("%"),
            create_button_safe("÷", color="orange", data="/"),
        ],
        alignment="center",
    )
    
    row2 = ft.Row(
        controls=[
            create_button_safe("7"),
            create_button_safe("8"),
            create_button_safe("9"),
            create_button_safe("x", color="orange", data="*"),
        ],
        alignment="center",
    )

    row3 = ft.Row(
        controls=[
            create_button_safe("4"),
            create_button_safe("5"),
            create_button_safe("6"),
            create_button_safe("-", color="orange"),
        ],
        alignment="center",
    )

    row4 = ft.Row(
        controls=[
            create_button_safe("1"),
            create_button_safe("2"),
            create_button_safe("3"),
            create_button_safe("+", color="orange"),
        ],
        alignment="center",
    )

    row5 = ft.Row(
        controls=[
            create_button_safe("0"), 
            create_button_safe("."),
            create_button_safe("=", bg="orange", color="white"),
            create_button_safe("⌫"),
        ],
        alignment="center",
    )

    # Safe page alignment
    try:
        page_align = ft.alignment.center_right
    except:
        page_align = ft.Alignment(1, 0)

    page.add(
        ft.Container(
            content=result,
            padding=20,
            alignment=page_align
        ),
        row1, row2, row3, row4, row5
    )

ft.app(main)

