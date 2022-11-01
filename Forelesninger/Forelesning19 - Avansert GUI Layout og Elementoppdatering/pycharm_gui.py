import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="PyCharm", width=600, height=400)

with dpg.window(no_title_bar=True, tag="window"):
    # For dette GUI-et benytter vi child windows for å lage forskjellige segmenter av GUI-et.
    # Det spesifikke oppsettet er her basert på PyCharm sitt GUI.

    with dpg.child_window(height=50, width=-1):
        # Dette child window-et representerer menyen på toppen av GUI-et. Merk at vi setter vidden til å være
        # dynamisk basert på det helhetlige vinduet.
        dpg.add_text("Menu")

    with dpg.child_window(height=200, width=-1):
        # Dette child windowet benytter vi til å samle Filvisning- og Editor-segmentene.
        # Fordelen med å gjøre dette er at vi kan samlet redigere slik som høyde og vidde for de inneholde segmentene.

        with dpg.group(horizontal=True): # Vi benytter group for å legge segmentene ved siden av hverandre.
            with dpg.child_window(height=-1, width=150):
                # Dette segmentet representerer Filvisningen i PyCharm-GUI-et. Merk at vi setter vidden statisk, mens
                # høyden er basert på child windowet som er definert på linje 15.
                #dpg.add_text("Files")

                # Vi kan her begynne å lage innhold som reflekterer en filvisning.
                with dpg.tree_node(label="Forelesning_19"):
                    dpg.add_text("pycharm_gui.py")
                    dpg.add_text("template.py")

            with dpg.child_window(height=-1, width=-1):
                # Dette segmentet representerer Editoren i PyCharm-GUI-et. Merk at både vidde og høyde er her satt
                # dynamisk. Høyden vil være basert på child window-et definert på linje 15, mens vidden er
                # underforstått påvirket av sementet til venstre for dette (linje 20).
                #dpg.add_text("Editor")
                dpg.add_input_text(multiline=True, height=-1, width=-1) # Multiline text-input.

    with dpg.child_window(height=-1, width=-1):
        # Dette segmentet representerer terminalen i PyCharm-GUI-et og tar opp den resterende vidden og høyden
        # på bunnen av GUI-et.
        dpg.add_text("Terminal")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True) # Setter "window" til å være GUI-ets primærvindu. Vinduet vil da dekke hele
                                       # viewporten.
dpg.start_dearpygui()
dpg.destroy_context()