import dearpygui.dearpygui as dpg

# Funksjon som skal kjøre når GUI-knappen klikkes.
def calculate_and_display_moon_weight():
    # Henter ut verdien for input-feltet for text basert på item tag (verdien send med som parameter).
    # Item tagen må matche med det som er definert for input-feltet lenger ned. Se Vindu-definisjonen under.
    user_weight = dpg.get_value("input_weight")

    # Beregner månevekten basert på verdien hentet fra input-feltet.
    moon_weight = user_weight / 9.807 * 1.622

    # Setter verdien for text-elementet i GUI, basert på item tag, til resultatet av utregningen.
    dpg.set_value("text_output", f"Result: {moon_weight}")


dpg.create_context()
dpg.create_viewport(title="Simple Button Click", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True, width=600, height=400):
    # Legger til et input-felt for float. Vi ønsker senere, ved knappetrykk, at verdien inneholdt i denne skal kunne
    # bli hentet ut. For å kunne gjøre dette, må vi ha en måte å referere til elementet. Dette kan vi gjøre ved bruk
    # av item tags. For å definere et element sin item-tag, kan vi sette en selvvalgt tekstverdi for paramteren tag.
    # De fleste GUI-elementer har denne tag-parameteren. Angående navngivning, er det ofte lurt å lage et navn
    # som både inneholder informasjon om typen element og hva elementet skal benyttes til. Vi kan senere benytte
    # denne taggen til å hente ut eller sette inn verdier for dette elementet. Se dpg.get_value() og dpg.set_value()
    # funksjonene, som er benyttet i calculate_and_display_moon_weight()-funksjonen over.
    dpg.add_input_float(label="Your weight on earth", width=200, tag="input_weight")

    # Oppretter en knapp og binder knappens callback til calculate_and_display_moon_weight()-funksjonen.
    dpg.add_button(label="Calculate moon weight", callback=calculate_and_display_moon_weight)

    # Oppretter et text-element og setter en item tag, for denne, slik at vi senere kan oppdatere dens verdi.
    # (Se calculate_and_display_moon_weight()-funksjonen)
    dpg.add_text("Result: ", tag="text_output")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()