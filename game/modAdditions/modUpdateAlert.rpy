screen modOutOfDate:
    modal True
    add "#23272a"

    vbox:
        align(0.5, 0.5)
        spacing 50

        text "{size=64}A new version of {b}Oscar's [config.name] Mod{/b} is now available.\nClick the Download Now button to download the new update."
        hbox:
            spacing 100
            xalign 0.5

            textbutton "Download Now":
                action OpenURL("https://www.patreon.com/OscarSix")
            textbutton "Ask Me Later":
                action Return()

label before_main_menu:

    if not upToDate():
        call screen modOutOfDate

    return
