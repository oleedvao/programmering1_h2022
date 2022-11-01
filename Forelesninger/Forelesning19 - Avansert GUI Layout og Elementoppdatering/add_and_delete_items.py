import dearpygui.dearpygui as dpg


# Callback-funksjon for å legge til et nytt tekst-element i child windowet "cw_list"
def add_item():
    item_name = dpg.get_value("input_item_name") # Henter tekst-verdien fra input-felt.
    dpg.add_text(item_name, parent="cw_list") # Legger til tekst-verdien som et eget tekst-element


# Callback-funksjon for å slette alle elementer i child window-et "cw_list"
def delete_items():
    dpg.delete_item("cw_list", children_only=True) # Sletter *de inneholdte* elementene i "cw_list", men ikke "cw_list"
    # i og seg selv.


dpg.create_context()
dpg.create_viewport(title="Add and delete items", width=600, height=400)

with dpg.window(no_title_bar=True, tag="window"):
    # GUI-oppsett for input og knapper.
    with dpg.group(horizontal=True):
        dpg.add_text("Item name: ")
        dpg.add_input_text(width=150, tag="input_item_name")
        dpg.add_button(label="Add item", callback=add_item)
        dpg.add_button(label="Delete items", callback=delete_items)
    # Benytter et child-window som en "liste" med tekst-elementer
    with dpg.child_window(height=-1, width=-1, tag="cw_list"):
        "content" # Denne tekstverdien gjør ingenting. Den er der for å forsørge at child-windowet har et "innhold" og
        # er syntax-messig gyldig.

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()