import dearpygui.dearpygui as dpg


# Dette er en vanlig funksjon, men den skal kjøres når gui-knappen klikkes.
# Funksjonen blir bundet til knappen lenger ned, hvor knappen blir opprettet.
def print_something():
    print("Programming is fun.")


dpg.create_context()
dpg.create_viewport(title="Simple Button Click", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True, width=600, height=400):
    # Legger til en knapp vi ønsker skal gjøre noe når vi klikker den.
    # Får å utføre funksjonalitet når knappen klikkes må definere knappens "callback".
    # En callback er i praksis en referanse til en funksjon som skal kjøres når det utføres en handling.
    # Handlingen er avhengig av hvilket element callbacken defineres for. Knapp -> knappeklikk.
    # For å definere selve callbacken kan vi sette en verdi for en egen parameter som heter callback.
    # Verdien for callback-parameteren setter vi til å være NAVNET på funksjonen vi ønsker å binde knappeklikket til.
    # Det vil si at vi skriver funksjonsnavnet, men ikke (). På denne måten sier vi at callback-parameteren skal holde
    # på en referanse til funksjonen. Hadde vi benyttet (), hadde funksjonen bare blitt kalt en gang når vi oppretter
    # knappen.
    dpg.add_button(label="Click me!", callback=print_something)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()