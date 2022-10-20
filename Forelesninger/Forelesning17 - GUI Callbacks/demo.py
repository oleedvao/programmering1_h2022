# Denne koden kjører en demo som viser mange forskjellige elementer man kan opprette med Dear PyGUI.
# Kildekoden for denne demoen kan bli funnet her: https://github.com/hoffstadt/DearPyGui/blob/master/dearpygui/demo.py
# Denne er fin å benytte som en referanse på hva man kan gjøre, og kildekoden kan benyttes for å finne ut hvordan
# det er gjort. Merk likevel at en god del av koden kan være overkomplifisert for hva man egentlig trenger.

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title="Elements", width=600, height=400)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()