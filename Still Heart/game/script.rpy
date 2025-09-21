# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ra = Character("Rachel")
define mo = Character("Monique")
define cl = Character("Cliff")
define ce = Character("Celine")
define mi = Character("Mia")

transform character_down:
    xalign 0.5
    yalign -0.3


# The game starts here.
label start:
    "Your game starts he- ...Wait, what is this?"

label rachels_bedroom_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg rachelsbedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Celine Dion,,,"

    show celine temp at character_down with fade

    # These display lines of dialogue.

    ce "W-Who's there?!"

    ce "Wait... Where AM I?!?!?!?!?"

    hide celine temp with fade

    "In the Dark... Someone appears..."

    show mia temp at character_down with dissolve

    mi "Play My Game."

    hide mia temp with fade

    "WHAT THE HEEEEEEELLLLLLLLL GOOKIIILLLLLEEEE"

    show cl default1 at right 

    cl "hey guys im cliff"

    show ra default at left 

    ra "AW HELL NAW YO ASS TWEAKIN JIGSAW"

    show celine temp at center

    ce "actually mia kill these guys"

    hide celine temp

    show mia temp 

    mi "yes vegeta"

    scene bg rachelsbedroom

    "and they all died yay the end thnaks for playing :333"

    # This ends the game.

    return
