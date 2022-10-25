import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=430, height=340)

with dpg.window(no_title_bar=True, width=400, height=300):
    # Vi kan opprette det som kalles for child windows. Disse fungerer i praksis som vinduer i "hovedvinduet" og
    # benyttes ofte til å visuelt samle og strukturere elementer.
    # Disse child window-elementene kan ha sine individuelle størrelser og innhold.
    # I child window-elementet under setter vi vidde og høyde statisk.
    with dpg.child_window(width=300, height=150):
        # Fyller child window-elementet med 20 text elementer
        # Dette overstrider dets definerte høyde og vil automatisk aktivere scrolling for dette child window-et.
        for number in range(20):
            dpg.add_text(f"Item {number}")

    dpg.add_text("Outside child window") # Text på utsiden av child windows

    # I child window-elementet under settes vidde og høyde dynamisk ved å sette verdiene for disse til å være -1.
    # Child window-elementet vil da fylle plassen som er tilgjengelig i henhold til dets "foreldreelement". I dette
    # tilfellet, hovedvinduet i programmet.
    with dpg.child_window(width=-1, height=-1):
        dpg.add_text("Other content")

    # Å legge til disse elementene demonstrerer at scrolling også fungerer for hovedvinduet hvis innholdet overstrider
    # høyden.
    dpg.add_text("Other content")
    dpg.add_text("Other content")
    dpg.add_text("Other content")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()