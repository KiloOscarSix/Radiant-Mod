default gr = "{color=#0f0}"
default red = "{color=#f00}"
default blue = "{color=#00f}"

default lustPath = "{color=#0f0}[Lust Path]"
default lust1 = "{color=#0f0}[Lust +1]"
default lust2 = "{color=#0f0}[Lust +2]"
default lust3 = "{color=#0f0}[Lust +3]"
default lust4 = "{color=#0f0}[Lust +4]"
default lust6 = "{color=#0f0}[Lust +6]"

default pure1 = "{color=#0f0}[Pure +1]"
default pure2 = "{color=#0f0}[Pure +2]"
default pure3 = "{color=#0f0}[Pure +3]"
default pure4 = "{color=#0f0}[Pure +4]"
default pure6 = "{color=#0f0}[Pure +6]"

default dark1 = "{color=#0f0}[Dark +1]"
default dark2 = "{color=#0f0}[Dark +2]"
default dark3 = "{color=#0f0}[Dark +3]"
default dark5 = "{color=#0f0}[Dark +5]"
default dark6 = "{color=#0f0}[Dark +6]"

default TiffanyPath = "{color=#0f0}[Tiffany Path]"
default OliviaPath = "{color=#0f0}[Olivia Path]"

default mcCareless = "{color=#0f0}[Careless]"
default mcDisciplinarian = "{color=#0f0}[Disciplinarian]"
default mcSadist = "{color=#0f0}[Sadist]"

default MadDark = "{color=#0f0}[Maddie Dark]"
default madScared1 = "{color=#0f0}[Maddie Scared1]"

default livLove1 = "{color=#0f0}[Liv Love +1]"
default livHorny1 = "{color=#0f0}[Liv Horny +1]"
default livProtect = "{color=#0f0}[Liv Protect]"
default livUncertain = "{color=#0f0}[Liv Uncertain]"
default livApologize = "{color=#0f0}[Liv Apologize]"
default livBlame = "{color=#0f0}[Liv Blame]"
default livFeelings = "{color=#0f0}[Liv Feelings]"
default livDeception = "{color=#0f0}[Liv Deception]"
default livTruthful = "{color=#0f0}[Liv Truthful]"
default livKissed = "{color=#0f0}[Liv Kissed]"

default aliLove1 = "{color=#0f0}[Ali Love +1]"
default aliHorny1 = "{color=#0f0}[Ali Horny +1]"
default aliScared2 = "{color=#0f0}[Ali Scared +2]"
default aliIncelgram = "{color=#0f0}[Ali Incelgram]"

default BrookPath = "{color=#0f0}[Brook Path]"
default brkCorrupted1 = "{color=#0f0}[Brook Corrupted +1]"

default VanessaPath = "{color=#0f0}[Vanessa Path]"
default vanJudgement = "{color=#0f0}[Vanessa Judgement]"

default creampie = "{color=#0f0}[Creampie]"
default endRelationship = "{color=#f00}[End Relationship]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xalign 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

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

    $ scopeDict = {"player_name":persistent.player_name, "surname":persistent.surname, "olivia_name":persistent.olivia_name, "allison_name":persistent.allison_name, "maddison_name":persistent.maddison_name, "ali_nick":persistent.ali_nick, "oli_nick":persistent.oli_nick, "age":persistent.age, "mad_nick":persistent.mad_nick}
    return

label changeIngameNames:

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
    return
