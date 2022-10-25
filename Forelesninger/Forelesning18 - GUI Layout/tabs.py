import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    # Tabs fungerer essensielt som forskjellige sider med forskjellige elementer, som vi kan navigere/bytte mellom.
    # For å opprette tabs, må vi først opprette en tab bar, som kan holde på disse tabene.
    # Denne har egne parametere, men det er inget krav om å benytte dem.
    with dpg.tab_bar():
        # Vi kan legge til individuelle tabs på innsiden av en slik tab bar.
        # Innholdet av disse kan være hva som helst og vil bare vises hvis den gitte taben er selektert.
        with dpg.tab(label="Tab 1"):
            dpg.add_text("Some text")
            dpg.add_button(label="Button!")
        with dpg.tab(label="Tab 2"):
            with dpg.group(horizontal=True):
                dpg.add_text("Input: ")
                dpg.add_input_text()
        with dpg.tab(label="Tab 3"):
            dpg.add_button(label="I DONT KNOW")
    # Merk at bare innholdet i tabene byttes mellom ved navigasjon.
    dpg.add_text("this text is here regardless of selected tab")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()