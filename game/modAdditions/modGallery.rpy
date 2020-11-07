init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

define galleryMenu = [
["All", ""],
]

define grace = GalleryItem("All", 1, "gracieforeplay", "Chapter 1/grsx_a12.webp")
define all = GalleryItem("All", 1, "galleryScene2", "Chapter 1/sw21.webp")
define vanessa = GalleryItem("All", 1, "vanessasex", "Chapter 2/c2g21.webp")
define all = GalleryItem("All", 1, "galleryScene1", "Chapter 2/c2o13.webp")

default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.player_name = ""
    default persistent.surname = ""
    default persistent.olivia_name = ""
    default persistent.allison_name = ""
    default persistent.maddison_name = ""
    default persistent.ali_nick = ""
    default persistent.oli_nick = ""
    default persistent.age = ""
    default persistent.mad_nick = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("Please enter your {b}first{/b} name...", default="John")
    if persistent.surname == "":
        $ persistent.surname = renpy.input("Please enter your {b}last{/b} name...", default="Evans")
    if persistent.olivia_name == "":
        scene tripb18 with fade
        $ persistent.olivia_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Olivia")
    if persistent.allison_name == "":
        scene tripb16 with sdissolve
        $ persistent.allison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Allison")
    if persistent.maddison_name == "":
        scene tripb15 with sdissolve
        $ persistent.maddison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")", default="Maddison")
    if persistent.ali_nick == "":
        scene lrali6 with xdissolve
        $ persistent.ali_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Allie")
    if persistent.oli_nick == "":
        scene din10 with dissolve
        $ persistent.oli_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Liv")
    if persistent.age == "":
        scene br9 with dissolve
        $ persistent.age = int(renpy.input("How old are the girls? (Numeric characters only. Leave this blank for their \"true age.\")", allow="0123456789", length=2, default=18))
    if persistent.mad_nick == "":
        scene mbat6 with dissolve
        $ persistent.mad_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")", default="Maddie")

    $ scopeDict = {"player_name":persistent.player_name, "surname":persistent.surname, "olivia_name":persistent.olivia_name, "allison_name":persistent.allison_name, "maddison_name":persistent.maddison_name, "ali_nick":persistent.ali_nick, "oli_nick":persistent.oli_nick, "age":persistent.age, "mad_nick":persistent.mad_nick}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action ShowMenu("main_menu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
