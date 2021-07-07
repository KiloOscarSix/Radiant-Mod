init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = len(filter(lambda s: s.char == char, galleryItems))//8 + 1
            self.label = label

            if scope is None: self.scope = {}
            else: self.scope = scope

            self.thumbnail = os.path.join("/images/", thumbnail)
            galleryItems.append(self)

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    ## GALLERY ITEMS HERE
define Gracie = GalleryItem("All", "gracieforeplay", "Chapter 1/grsx_a12.webp")
define All = GalleryItem("All", "galleryScene2", "Chapter 1/sw21.webp")
define Vanessa = GalleryItem("All", "vanessasex", "Chapter 2/c2g21.webp")
define All = GalleryItem("All", "galleryScene1", "Chapter 2/c2o13.webp")
define Maddie = GalleryItem("All", "mad_punished", "Chapter 2/c2u1.webp")
define Gracie = GalleryItem("All", "gracie_sex_scene", "Chapter 3/c3a1.webp")
define Allie = GalleryItem("All", "takingadvantage", "Chapter 3/c3k11.webp")
define Allie = GalleryItem("All", "allieposescene", "Chapter 3/c3l12.webp")
define Brooke = GalleryItem("All", "afterkiss_romance", "Chapter 3/c3q55.webp")

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
    ["All", ""],
]

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
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

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
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action [Hide("sceneGalleryMenu"), ShowMenu("main_menu")]
            else:
                action SetVariable("galleryPageNumber", galleryPageNumber - 1)
            idle "/modAdditions/images/backButton.png"
            hover im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action SetVariable("galleryPageNumber", galleryPageNumber + 1)
                idle "modAdditions/images/nextButton.png"
                hover im.MatrixColor("modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)