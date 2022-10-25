import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    # Vi kan indentere de fleste elementer ved bruk av indent-parameteren. Vi vil da indentere elementet det
    # spesifiserte antallet pixler fra venstre i vinduet (ikke viewporten)
    dpg.add_button(label="Some element", indent=100)
    dpg.add_text("jkfdljsfkljsdlkfjaslkdfj", indent=80)

    # Vi kan også posisjonere elementer på et helt spesifikt sted (en absolutt posisjon) i vinduet ved bruk av
    # pos-parameteren. Denne parameteren tar en tuple med to verdier. Den første verdien definerer pixel-posisjonen
    # for x-aksen, og den andre verdien pixel-posisjonen for y-aksen. Det er viktig å bemerke at y aksen i Dear PyGUI
    # vinduer starter på 0 i toppen av vinduet og går nedover som pixel-verdien øker.
    # Merk også at absolutt posisjonering ikke tar hensyn til elementer som allerede eksisterer. Vi kan dermed plassere
    # elementer på toppen av andre elementer med absolutt posisjonering.
    dpg.add_button(label="Absolute position", pos=(70, 20))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
