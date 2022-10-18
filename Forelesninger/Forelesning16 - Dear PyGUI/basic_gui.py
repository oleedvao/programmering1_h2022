# Vi må importere dearpygui-pakken for å kunne opprette GUI-er.
# Dette krever at vi har innstallert denne pakken enten via pip eller Python Packages i PyCharm
import dearpygui.dearpygui as dpg

# Ethvert GUI opprettet med dearpygui starter med denne .
# Det er ikke viktig å forstå hva denne egentlig gjør.
dpg.create_context()

# Denne kodelinjen oppretter en viewport for programmet (et programmvindu) og konfigurer en tittel-text
# og vinduets vidde og høyde (i pixler).
# Funksjonen har også en rekke andre parametere, men de vist under er de mest essensielle.
dpg.create_viewport(title="Basic GUI!", width=700, height=500)

# Vi kan definere container-elementer ved bruk av with-nøkkelordet.
# Dette vil fungere som en kodeblokk hvor det vi definerer som tilhørende denne blokken vil være det
# container elementet inneholdter.
# Vi oppretter og konfigurerer i dette tilfellet et vindu, med en label, en width og en height.
# Labelen vil fungere som vinduets navn, width og height er fremedeles målt i pixler.
# Merk også at et "window" ikke er det samme som en viewport, men fungerer som et internt vindu.
with dpg.window(label="This is a window!", width=600, height=400):
    # Her kan vi definere UI-elementene som vinduet skal inneholde.
    # Slike UI-elementer må faktisk være inneholdt i et container-element for at vi skal kunne opprette det.
    # Linjen under oppretter en statisk tekst i vinduet.
    dpg.add_text("Something!")

# Disse fire kodelinjene er overordnet de som kjører og viser frem GUI-et.
# Disse må alltid være med på slutten av dearpygui-programmer, men det er ikke viktig å ytterligere vite
# nøyaktig hva de gjør.
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()