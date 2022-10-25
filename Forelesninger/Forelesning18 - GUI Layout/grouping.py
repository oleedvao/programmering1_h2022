import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    dpg.add_text("This text is outside a group")
    # Vi kan gruppere GUI-elementer ved bruk av container elementet group, og benytte det til forskjellige formål.
    # Hvis vi ønsker å legge til elementer som skal legges til horisontalt i stedet for vertikalt, kan vi sette
    # horizontal-prameteren til True.
    with dpg.group(horizontal=True):
        dpg.add_button(label="Button 1")
        dpg.add_text("Some text.")
        dpg.add_text("Another text.")
    # Vi kan også benytte groups til å redigere vidden av alle elementer inneholdt i gruppen.
    # Men selv om det hadde gitt mening, kan vi av en eller annen grunn ikke redigere høyden av elementene
    # på denne måten.
    with dpg.group(width=250):
        dpg.add_button(label="Button 2")
        dpg.add_button(label="Button 3")
    # Vi kan i tillegg gjøre begge deler på en gang ved å definere verdier for begge parameterene.
    # Vi kan interessant nok også benytte posisjoneringsparametere på gruppen for å endre posisjonen av alle elementene
    # samlet. Det vil si at vi posisjonerer gruppen som en helhet.
    with dpg.group(horizontal=True, width=150, pos=(50, 150)):
        dpg.add_button(label="Button 4")
        dpg.add_text("TEEEEXT")
        dpg.add_button(label="Button 5")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()