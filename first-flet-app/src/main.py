import flet as ft

def main(page: ft.Page):
    page.title = "El panadero con el pan 👀👀"
    page.window_width = 420
    page.window_height = 720
    page.bgcolor = "#FFF8E7"

    estado = {"actual": "inicio"}

    # Widgets o como se les llame
    titulo = ft.Text(
        "Preguntas bien pasadas de rosca", 
        size=24, 
        weight="bold", 
        color="#8B4513",  # Marrón (PUEBLO MARRÓN REFERENCIA)
        text_align="center"
    )

    texto = ft.Text("", size=18, text_align="center")
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si = ft.ElevatedButton("Sí", bgcolor="#D2691E", color="white", width=120)
    btn_no = ft.ElevatedButton("No", bgcolor="#8B0000", color="white", width=120)
    btn_reset = ft.TextButton("Reiniciar", icon=ft.Icons.REFRESH, style=ft.ButtonStyle(color="#8B4513"))

    botones = ft.Row(
        [btn_si, btn_no],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # --- Funciones de flujo ---
    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = "#FFF8E7"
        texto.value = "😏 ¿Te gusta el pan?"
        imagen.src = "pan1.png"
        imagen.visible = True
        btn_si.visible = True
        btn_no.visible = True
        page.update()

    # Flujooooo

    def p2_si():
        estado["actual"] = "p2_si"
        texto.value = "🥐 ¿Prefieres una concha que un bolillo?"
        imagen.src = "pan_dulce.png"
        page.update()

    def p2_no():
        estado["actual"] = "p2_no"
        texto.value = "¿Entonces me estás diciendo que no te gusta nada nadita? 🥺"
        page.update()

    def p3_dulce():
        estado["actual"] = "p3_dulce"
        texto.value = "¿Te gusta el... el bolillo? 👀"
        imagen.src = "bolilo.png"
        page.update()

    def p3_sin_dulce():
        estado["actual"] = "p3_sin_dulce"
        texto.value = "¿Te gusta el pan de queso? 🧀"
        imagen.src = "pan_queso.png"
        page.update()

    def p4_bolillo():
        estado["actual"] = "p4_bolillo"
        texto.value = "¿Te gusta la torta de ate? 🤑"
        imagen.src = "ate.png"
        page.update()

    def p4_no_bolillo():
        estado["actual"] = "p4_no_bolillo"
        texto.value = "🥛 ¿Te gusta tomarte tu pan con leche?"
        imagen.src = "leche.png"
        page.update()

    def p5_cuernillo():
        estado["actual"] = "p5_cuernillo"
        texto.value = "🥪 ¿Te gusta el cuernito relleno de jamón?"
        imagen.src = "cuernillo.png"
        page.update()

    def p5_leche():
        estado["actual"] = "p5_leche"
        texto.value = "🍯 ¿Te gusta el bolillo con mermelada?? (ya sé que la imágen no es un bolillo)"
        imagen.src = "mermelada.png"
        page.update()

    def p6_panaderia():
        estado["actual"] = "p6_panaderia"
        texto.value = "Esperanza: ¿Si o no?"
        imagen.src = "panaderia.png"
        page.update()

    def p6_mermelada():
        estado["actual"] = "p6_mermelada"
        texto.value = "¿Te lo comes entero?"
        imagen.src = "oomagad.png"
        page.update()

    # Finales
    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = "Eso es todo mi buen 🔥🔥🔥, te ganaste un pan."
        imagen.src = "pansupremo.png"
        page.bgcolor = "#C8E6C9"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "😑 Te la paso por esta vez..."
        imagen.src = "neutral.png"
        page.bgcolor = "#FFF3E0"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "😡 Tons pelate de aca carnal, no me hables"
        imagen.src = "angri.png"
        page.bgcolor = "#FFCDD2"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    # Decisiones
    def on_si(e):
        if estado["actual"] == "inicio": p2_si()
        elif estado["actual"] == "p2_si": p3_dulce()
        elif estado["actual"] == "p2_no": final_malo()
        elif estado["actual"] == "p3_dulce": p4_bolillo()
        elif estado["actual"] == "p3_sin_dulce": final_medio()
        elif estado["actual"] == "p4_bolillo": p5_cuernillo()
        elif estado["actual"] == "p4_no_bolillo": p5_leche()
        elif estado["actual"] == "p5_cuernillo": p6_panaderia()
        elif estado["actual"] == "p5_leche": p6_mermelada()
        elif estado["actual"] == "p6_panaderia": final_bueno()
        elif estado["actual"] == "p6_mermelada": final_bueno()

    def on_no(e):
        if estado["actual"] == "inicio": p2_no()
        elif estado["actual"] == "p2_si": p3_sin_dulce()
        elif estado["actual"] == "p2_no": final_malo()
        elif estado["actual"] == "p3_dulce": p4_no_bolillo()
        elif estado["actual"] == "p3_sin_dulce": final_medio()
        elif estado["actual"] == "p4_bolillo": final_medio()
        elif estado["actual"] == "p4_no_bolillo": final_medio()
        elif estado["actual"] == "p5_cuernillo": final_medio()
        elif estado["actual"] == "p5_leche": final_medio()
        elif estado["actual"] == "p6_panaderia": final_bueno()
        elif estado["actual"] == "p6_mermelada": final_medio()

    def on_reset(e): mostrar_inicio()

    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_reset.on_click = on_reset

    # Laiaut (layout)
    page.add(
        ft.Container(
            content=ft.Column(
                [titulo, texto, imagen, botones, btn_reset],
                alignment=ft.MainAxisAlignment.CENTER, #lo centré para que esté mas bonito
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

    mostrar_inicio()

ft.app(target=main)
