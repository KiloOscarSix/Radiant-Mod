screen main_menu():
    tag menu

    add "gui/main_menu.png"

    imagebutton auto "gui/button/patreon_%s.png" xalign 0.05 yalign 0.95 action OpenURL("https://www.patreon.com/radiantgame")



    imagebutton auto "gui/button/start_%s.png" xpos 100 ypos 220 focus_mask True action Start()
    imagebutton auto "gui/button/load_%s.png" xpos 100 ypos 280 focus_mask True action ShowMenu('load')
    imagebutton auto "gui/button/pref_%s.png" xpos 100 ypos 335 focus_mask True action ShowMenu('preferences')
    textbutton _("Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneCharacterMenu")]
    imagebutton auto "gui/button/about_%s.png" xpos 100 ypos 390 focus_mask True action ShowMenu('about')
    imagebutton auto "gui/button/quit_%s.png" xpos 100 ypos 450 focus_mask True action Quit(confirm=True)

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

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            if title == "Save":
                text "{color=#fff}Save Name:{/color}":
                    xalign 0
                    yalign -0.005
                input:
                    xalign 0
                    yalign 0.05
                    value VariableInputValue("save_name")

            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
