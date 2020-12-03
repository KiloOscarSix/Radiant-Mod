screen main_menu():
    tag menu

    add "gui/main_menu.png"

    imagebutton auto "gui/button/patreon_%s.png" xalign 0.05 yalign 0.95 action OpenURL("https://www.patreon.com/radiantgame")



    imagebutton auto "gui/button/start_%s.png" xpos 100 ypos 220 focus_mask True action Start()
    imagebutton auto "gui/button/load_%s.png" xpos 100 ypos 280 focus_mask True action ShowMenu('load')
    imagebutton auto "gui/button/pref_%s.png" xpos 100 ypos 335 focus_mask True action ShowMenu('preferences')
    imagebutton auto "modAdditions/images/gallery_%s.png" action [ui.callsinnewcontext("galleryNameChange"), Show("sceneCharacterMenu")] xpos 100 ypos 390
    imagebutton auto "gui/button/about_%s.png" xpos 100 ypos 440 focus_mask True action ShowMenu('about')
    imagebutton auto "gui/button/quit_%s.png" xpos 100 ypos 490 focus_mask True action Quit(confirm=True)

    style_prefix "main_menu"

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:
            textbutton _("Mod Options") action Show("modOptions")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):



            textbutton _("Quit") action Quit(confirm=not main_menu)
