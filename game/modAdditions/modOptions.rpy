init python:
    gr = "{color=#0f0}"
    BrookPath = "{color=#0f0}[Brook Path]"
    VanessaPath = "{color=#0f0}[Vanessa Path]"
    TiffanyPath = "{color=#0f0}[Tiffany Path]"
    OliviaPath = "{color=#0f0}[Olivia Path]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

        frame:
            grid 2 2:
                style_prefix "check"
                spacing 5

                textbutton "Brook Path" action ToggleVariable("BrookPath", true_value="{color=#0f0}[Brook Path]", false_value="")
                textbutton "Vanessa Path" action ToggleVariable("VanessaPath", true_value="{color=#0f0}[Vanessa Path]", false_value="")
                textbutton "Tiffany Path" action ToggleVariable("TiffanyPath", true_value="{color=#0f0}[Tiffany Path]", false_value="")
                textbutton "Olivia Path" action ToggleVariable("OliviaPath", true_value="{color=#0f0}[Olivia Path]", false_value="")

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)


label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    $ player_name = renpy.input("Please enter your {b}first{/b} name...", default="John")
    $ surname = renpy.input("Please enter your {b}last{/b} name...", default="Evans")
    scene tripb18 with fade
    $ olivia_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Olivia")
    scene tripb16 with sdissolve
    $ allison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Allison")
    scene tripb15 with sdissolve
    $ maddison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Maddison")
    scene lrali6 with xdissolve
    $ ali_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Allie")
    scene din10 with dissolve
    $ oli_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Liv")
    scene br9 with dissolve
    $ age = int(renpy.input("How old are the girls? (Numeric characters only. Leave this blank for their \"true age.\")", allow="0123456789", length=2, default=18))
    scene mbat6 with dissolve
    $ mad_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Maddie")

    mod "Names successful changed"
    return

label changeGalleryNames:
    $ persistent.player_name = renpy.input("Please enter your {b}first{/b} name...", default="John")
    $ persistent.surname = renpy.input("Please enter your {b}last{/b} name...", default="Evans")
    scene tripb18 with fade
    $ persistent.olivia_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Olivia")
    scene tripb16 with sdissolve
    $ persistent.allison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Allison")
    scene tripb15 with sdissolve
    $ persistent.maddison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Maddison")
    scene lrali6 with xdissolve
    $ persistent.ali_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Allie")
    scene din10 with dissolve
    $ persistent.oli_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Liv")
    scene br9 with dissolve
    $ persistent.age = int(renpy.input("How old are the girls? (Numeric characters only. Leave this blank for their \"true age.\")", allow="0123456789", length=2, default=18))
    scene mbat6 with dissolve
    $ persistent.mad_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Maddie")
    mod "Gallery names successful changed"
    return
