# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rachel")
define mo = Character("Monique")
define c = Character("Cliff")
define ce = Character("Celine")
define m = Character("Mia")

transform character_down:
    xalign 0.5
    yalign -0.3


# The game starts here.
label start:
    "Your game starts he- ...Wait, what is this?"

label rachel_bedroom_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

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

    m "Play My Game."

    hide mia temp with fade

    "WHAT THE HEEEEEEELLLLLLLLL GOOKIIILLLLLEEEE"

    # This ends the game.

    return
