import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Elements", width=600, height=400)

with dpg.window(label="Content", width=600, height=400):
    dpg.add_text("This is a text!") # Legger til et statisk tekstelement med verdien "This is a text!"

    dpg.add_input_text(label="Input text here", width=150) # Legger til et inputfelt for text
    dpg.add_input_int(label="Input int here", width=150) # Legger til et inputfelt for int
    dpg.add_input_float(label="Input float here", width=150) # Legger til et inputfelt for float
    # Merk at inputfeltene over har automatisk kontroll for verdiene vi setter inn når programmet kjører.
    # Vi kan dermed stole på at en int-input aldri vil ta/gi noe annet enn en int-verdi. Det samme gjelder for
    # de andre input-typene.

    dpg.add_button(label="Click me!") # Legger til en knapp (uten klikkfunksjonalitet)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()