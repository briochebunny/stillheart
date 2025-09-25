# The script of the game goes in this file.

define fadeLong = Fade(0.5, 1, 0.5)

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
    "Ah. There you are. I can see you clearly now."

    "Welcome, welcome. Please, get comfortable."

    "Before you begin your revisit of high school through another's point of view, there is something you must know."

    "You must know that you are not being told the full story."

    "Our protagonist knows something important, and she refuses to tell anyone."

    "You can spend your time seeking the truth, or you can choose to let it be. The choice is yours."

    "But be warned, your pursuit of knowledge may cost you. If you decide to live a life of blissful ignorance, is that really so bad?"

    "I suppose you won't know until you do."

    "Well, I've spoken long enough. It's time for your journey to commence. But please, do keep in mind what I told you."

    "After all, some secrets are better kept in the dark."

    scene black with fade
    jump rachels_bedroom_start


label rachels_bedroom_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg rachelsbedroom
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Inside a small bedroom, in a small town, are two girls, listening to some music together on a small record player."

    "The two girls lay side by side in comfortable silence, not wishing to disturb the gentle crackle of the vinyl against its needle."

    "One of them, a redhead, seems to be comfortable in the silence, her eyes closed and her hands clasped against her stomach."

    "Having just submitted her college applications earlier that day, she felt the stress of meeting the deadlines wash away with the music."

    "College is a fresh start, afterall."

    "She seems oblivious to her friend–the brunette–and how she seems to be stewing over something, shifting against the sheets in mild concern."

    "All this movement seems to be getting on the redhead's nerves, as she furrows her brow in discomfort. Her eyes remain shut."

    show ra default:
        xpos -0.4
        ypos 0.1

    ra "Moni, your sweater keeps tickling my arm hair."

    "Monique, the brunette, shifts a bit to the right to give her friend some much needed space."

    show mo default:
        xpos 0.4
        ypos 0.0

    mo "Whoops, sorry, Rach."

    "The redhead, Rachel, sits up in the bed now, her eyes open as she regards Monique with a quizzical expression."

    ra "Is something bothering you? Do...you not like the song?"
    ra "Is it not exciting enough for you?"

    mo "No, it's not the song! I feel like that'd be a silly reason for me to be upset."

    ra "Well, that's because you're a silly person."

    "Rachel throws Monique a soft, lighthearted smirk, which seems to lighten the mood."

    mo "..."

    ra "Come on, Moni, you can tell me anything."

    mo "Sigh."
    mo "You're not gonna like it though."

    ra "Please, when has that ever stopped you from running your mouth with me?"
    ra "In the time I've known you, I've only ever known you to be loud and unapologetic."
    ra "So please, just tell me what's bothering you."

    "Rachel's voice softens near the end, and Monique sighs in resolution."

    mo "Alright, I'll tell you."
    mo "But I'm telling you now, you'll wish I kept my mouth shut."

    ra "Whatever you say."
    ra "Come on, spill."

    mo "Okay okay."
    mo "So...you remember the guy from Advanced Art last year?"

    ra "The one who..."

    menu:
        "...tried asking you out?":
            ra "And in the middle of his confession to you, got so nervous he threw up?"

            mo "YES, and then started crying from his embarrassment over throwing up!"

        "...spilled paint thinner on you?":
            ra "And in the middle of his apologies and offering to find you a change of clothes, his cup of paint water slipped from his sweaty hands?"

            mo "YES, and all the water got all over my already paint-thinner-soaked leggings!"

    mo "Well, he has a friend who I ran into a few times last year."
    mo "And, you remember how I told you this super cute guy joined the track team?"

    ra "Is that this same guy??"

    mo "YES! I honestly had NO idea he even remembered me since we barely ever spoke."
    mo "Well anyway, we were talking a bit and he was totally flirting with me."

    "It's at this point that Monique starts to look reluctant to speak, as though her nerves came flooding back."

    mo "But, um, he asked if I was busy today and I said no, so..."
    mo "He invited me to this Halloween party he's going to."
    mo "And I just said yes without thinking since it's open to the upper classmen, but now that I think about it, I'm getting second thoughts."

    ra "What? No, you have to go! You told me you thought he was cute at the start of the year, it's been months."
    ra "You're still into him, right?"

    "Monique nods her head, glancing off to the side."

    ra "Then you should go!"

    "And, before she could stop herself–"

    ra "I'll even go to back you up too, okay?"

    "Whoops."

    "Looks like Rachel has a hard time holding her tongue."

    mo "Wha–? Are you serious? I thought you hated parties."

    "Rachel withholds a grimace at the mention. She's never been particularly fond of parties, and the feeling only worsened in high school."

    ra "I mean, I can just hang out in a corner so no one talks to me, it's fine."
    ra "And it's a Halloween party, right? I can just put on a mask or something so no one realizes it's me."

    mo "Wow Rachel, in the time I've known you, you've never been one for large crowds."
    mo "Just the mention of being around lots of people has you ducking for cover."

    ra "And for good reason, too."
    ra "You make it seem like I'm just some antisocial loser."

    mo "Well..."

    ra "Oh, screw you!"

    "Rachel tosses one of her pillows at Monique, eliciting a laugh from the girl as it smacks her in the face, before plopping into her lap."

    "Monique's smile falters for a moment, and Rachel realizes the very important question she has yet to ask."

    ra "Did you ask whose house the party was being held at?"

    mo "Um, yeah...I did."

    "Rachel stares at her expectantly."

    mo "..."

    ra "Well?"

    mo "It's uh, being held at..."
    mo "...Celine's."

    ra "..."

    mo "Y-yeah…"
    mo "Listen, I can just tell him I wasn't feeling well on Monday, I don't have to."
    mo "I accepted without thinking anyway..."

    "Despite her words, Monique looks dejected, as though she were already predicting the outcome to be not in her favor."

    "It seems like she was really looking forward to this."

    "But...is going to this party really such a good idea?"

    "Rachel can't help but feel like this is a mistake."

    menu:
        "Insist that she goes.":
            call rachbedroom_insist_mo_goes
        "Attempt to dissuade her.":
            call rachbedroom_disuade_mo
        "Rachel will be fine":
            call rachbedroom_ra_fine

    "There's a heavy silence for a moment, before Monique breaks out into a smile."

    mo "Damn, you got guts, girl! Going to the home of your biggest enemy is pretty ballsy."

    ra "Yeah, yeah. I'm only going for you. And maybe the dog."

    mo "Definitely the dog!"
    mo "Anyway, it starts in a couple hours so we should start getting ready, I think!"
    mo "We can't pull up to a Halloween party without any costumes on, that's like...Mac without Cheese."

    "With the air cleared, Monique seems to be in a much better mood."

    "Maybe it'll be okay for Rachel to go after all."

    jump halloween_party

    
label halloween_party:
    scene bg partyexterior
    with fadeLong

    "wiggly wobbly wiggly wobbly wiggly wobbly ouguguhhhhh OWAHHHHHHH"
    return

    


label rachbedroom_insist_mo_goes:
    ra "No, you should go."
    ra "Forget about me for a second. Do what feels good to you."

    mo "What feels good to me is making sure you're okay, and it doesn't seem like you are!"
    mo "And besides, I don't even know if I'd want to go anyway."
    mo "Rachel...Celine is like, your biggest hater."
    mo "Sure, you have a reputation of sorts, but she's like, the CEO of the Anti Rachel Regime."

    ra "Yeah, well, she can suck it up for once."

    mo "Suck it up?"
    mo "How can you expect her to suck it up when she thinks you're the reason her sister is missing?"
    mo "With a grudge THAT big you'd think she would crush half the cheer squad with all that weight."

    ra "Moni, be serious."

    mo "I am serious! I don't get how you're so comfortable with this."

    ra "Well, I am, so just drop it okay?"
    return

label rachbedroom_disuade_mo:
    ra "Hey...I'm sure it'll be super boring anyway."
    ra "It's not like they've got anything that you don't already have."
    ra "And… it's like you said, right? You can see him again on Monday?"

    "Monique averts her eyes."

    mo "...They got a Pac-Man machine."

    "Damn. They really do got everything."

    "Now it's Rachel's turn to look away, though this time it's out of guilt."

    "She thought back to their years together in this small town, where word travels fast, and furious."

    "Reference aside, Rachel mentally acknowledges how these years of ridicule were not only difficult on her, but her friend as well."

    "Monique no doubt faces similar scrutiny from peers due to association."

    "Her social life seemed to be mostly fine, but was Rachel really going to deny her something she seemed to want so badly, for her own selfish reasons?"

    "And with Monique looking down like that, she knew she couldn't say no."

    ra "..."
    ra "God, I feel like a jerk."
    ra "You shouldn't not go because of me, Moni."
    ra "It'll be fun, I think!"

    "Monique slowly looked back at Rachel, a quizzical expression formed."

    mo "...Are you serious?"

    "A small smile formed on Rachel's face."

    ra "Yeah, forget about me for a second. Do what feels good to you."
    ra "I'll be fine."
    return

label rachbedroom_ra_fine:
    ra "You know what? I'll be fine."
    ra "Why don't you tell me what it's like after?"

    mo "Rach, are you serious? I can't do this by myself!"
    mo "Sure I'm...more social than you are, but we're a team!"
    mo "You know, the whole Dastardly Duo or whatever."
    mo "Besides, I don't want to go there just KNOWING it's a place that might not accept you...No offense."

    "Rachel smiles at Monique, but it doesn't quite reach her eyes."

    ra "I honestly don't mind."
    ra "You can get some sweet info on what people think about me!"

    mo "This isn't the time to joke! Celine literally hates your guts."
    mo "She thinks what happened is your fault!"
    mo "How can I just leave you for that?"

    ra "Look, that doesn't matter when you're not even going for her!"
    ra "She won't even know you're going until you're there."

    mo "That's my point! So either we both go or I just lie and hang out with you eating chips and dip all night!"

    "That did sound good."

    "But she couldn't get in the way of Monique's life, she'd supported her all throughout high school when everyone was against her..."

    "For Moni, she'd push her issues aside."

    ra "Alright, you got my hands tied."
    ra "Do what feels good to you, I'll be right beside you."
    return