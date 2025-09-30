$ quick_menu = True
# The script of the game goes in this file.

define celineFirst = False
define cliffFirst = False
define sendText = False

define fadeLong = Fade(0.5, 1, 0.5)
define af = renpy.audio.filter
define customMove = MoveTransition(1.5)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ra = Character("Rachel")
define mo = Character("Monique")
define cl = Character("Cliff")
define ce = Character("Celine")
define mi = Character("Mia")

# commenting out the loop image predictions since the game is relatively short and its just for the demo :)
init python:
#     #image predictions -Arthur
#     # in the full game it's advised to predict only the used assets with each labels to prevent lag
#     def preload_images(img_list):
#         for img in img_list:
#             renpy.start_predict(img)

#     def stop_preloading(img_list):
#         for img in img_list:
#             renpy.stop_predict(img)

    images_to_preload = [
        # USED sprites
        "ra default", "ra defaultcos", "ra frown", "ra frowncos", "ra sad", "ra sadcos", "ra shocked", "ra shockedcos", "ra smile", "ra smilecos", "ra timid", "ra timidcos",
        "mo angry", "mo angrycos", "mo concern", "mo concerncos", "mo default", "mo defaultcos", "mo gentle", "mo gentlecos", "mo smile", "mo smilecos",
        "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
        # BGs
        "bg partyexterior", "bg partyinterior", "bg partyporch", "bg rachelsbedroom",
        # covers/splashes
        "itchMainCover", "spooktober logo", "thanks for playing"
    ]


image splash = "images/spooktober logo.png"
image endcreds = "images/thanks for playing.png"

#disables click for whatever screen its called on
screen noclick(): #maybe add this too 
    zorder 1000
    $ preferences.afm_enable = True

# adding a splash screen
label splashscreen:
    $ renpy.music.set_volume(0.5)

    show screen noclick
    scene black
    with Pause(1.0)

    show splash with dissolve
    with Pause(4.0)

    scene black with dissolve
    with Pause(1.0)

    hide screen noclick
    $ preferences.afm_enable = False
    return

# Sprite Positions -Arthur
# transform posLeft:
#     xpos -5           
#     ypos 100   

# transform posRight:
#     xpos 800           
#     ypos 100  

transform posLeft:
    xpos -0.05
    ypos 0.2

transform posRight:
    xpos 0.65
    ypos 0.15

transform cliffsFuckassSpecialFunction:
    xpos 0.60
    ypos 0.15


# The game starts here.
label start:
    $ renpy.start_predict(images_to_preload)
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

    stop music fadeout 1.0

    scene black with fade
    jump rachels_bedroom_start


label rachels_bedroom_start:
    # predictions babey
    # $ preload_images(["ra default", "ra frown", "ra sad", "ra shocked", "ra smile", "ra timid",
    # "mo angry", "mo concern", "mo default", "mo gentle", "mo smile", "bg rachelsbedroom"])

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Hushed.wav"

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

    "She seems oblivious to her friend-the brunette-and how she seems to be stewing over something, shifting against the sheets in mild concern."

    "All this movement seems to be getting on the redhead's nerves, as she furrows her brow in discomfort. Her eyes remain shut."

    show ra default at posLeft with moveinleft

    ra "Moni, your sweater keeps tickling my arm hair."

    "Monique, the brunette, shifts a bit to the right to give her friend some much needed space."

    show mo concern at posRight with moveinright


    mo "Whoops, sorry, Rach."

    "The redhead, Rachel, sits up in the bed now, her eyes open as she regards Monique with a quizzical expression."

    ra "Is something bothering you? Do...you not like the song?"
    ra "Is it not exciting enough for you?"

    mo "No, it's not the song! I feel like that'd be a silly reason for me to be upset."

    ra "Well, that's because you're a silly person."

    show ra smile
    "Rachel throws Monique a soft, lighthearted smirk, which seems to lighten the mood."

    show mo gentle
    mo "..."

    show ra smile
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

    show ra default
    ra "The one who..."

    menu:
        "...tried asking you out?":
            ra "And in the middle of his confession to you, got so nervous he threw up?"

            show mo smile
            mo "YES, and then started crying from his embarrassment over throwing up!"

        "...spilled paint thinner on you?":
            ra "And in the middle of his apologies and offering to find you a change of clothes, his cup of paint water slipped from his sweaty hands?"

            show mo smile
            mo "YES, and all the water got all over my already paint-thinner-soaked leggings!"

    mo "Well, he has a friend who I ran into a few times last year."
    mo "And, you remember how I told you this super cute guy joined the track team?"

    show ra shocked
    ra "Is that this same guy??"

    show mo default
    mo "YES! I honestly had NO idea he even remembered me since we barely ever spoke."
    mo "Well anyway, we were talking a bit and he was totally flirting with me."

    show mo gentle
    show ra default
    "It's at this point that Monique starts to look reluctant to speak, as though her nerves came flooding back."

    mo "But, um, he asked if I was busy today and I said no, so..."
    mo "He invited me to this Halloween party he's going to."
    mo "And I just said yes without thinking since it's open to the upper classmen, but now that I think about it, I'm getting second thoughts."

    show ra shocked
    ra "What? No, you have to go! You told me you thought he was cute at the start of the year, it's been months."
    ra "You're still into him, right?"

    "Monique nods her head, glancing off to the side."

    ra "Then you should go!"

    "And, before she could stop herself-"

    show ra timid
    ra "I'll even go to back you up too, okay?"

    "Whoops."

    "Looks like Rachel has a hard time holding her tongue."

    show mo concern
    mo "Wha-? Are you serious? I thought you hated parties."

    "Rachel withholds a grimace at the mention. She's never been particularly fond of parties, and the feeling only worsened in high school."

    ra "I mean, I can just hang out in a corner so no one talks to me, it's fine."
    ra "And it's a Halloween party, right? I can just put on a mask or something so no one realizes it's me."

    show mo gentle
    mo "Wow Rachel, in the time I've known you, you've never been one for large crowds."
    mo "Just the mention of being around lots of people has you ducking for cover."

    ra "And for good reason, too."
    ra "You make it seem like I'm just some antisocial loser."

    mo "Well..."

    show ra smile
    ra "Oh, screw you!"

    show mo default
    "Rachel tosses one of her pillows at Monique, eliciting a laugh from the girl as it smacks her in the face, before plopping into her lap."

    show mo gentle
    "Monique's smile falters for a moment, and Rachel realizes the very important question she has yet to ask."

    ra "Did you ask whose house the party was being held at?"

    mo "Um, yeah...I did."

    show ra default
    "Rachel stares at her expectantly."

    mo "..."

    ra "Well?"

    show mo concern
    mo "It's uh, being held at..."

    show ra shocked
    mo "...Celine's."

    ra "..."

    mo "Y-yeah…"
    show mo gentle
    mo "Listen, I can just tell him I wasn't feeling well on Monday, I don't have to."
    mo "I accepted without thinking anyway..."

    show ra frown
    "Despite her words, Monique looks dejected, as though she were already predicting the outcome to be not in her favor."

    "It seems like she was really looking forward to this."

    "But...is going to this party really such a good idea?"

    "Rachel can't help but feel like this is a mistake."

    menu:
        "Insist that she goes.":
            call rachbedroom_insist_mo_goes from _call_rachbedroom_insist_mo_goes
        "Attempt to dissuade her.":
            call rachbedroom_disuade_mo from _call_rachbedroom_disuade_mo
        "Rachel will be fine":
            call rachbedroom_ra_fine from _call_rachbedroom_ra_fine

    "There's a heavy silence for a moment, before Monique breaks out into a smile."

    show mo default
    mo "Damn, you got guts, girl! Going to the home of your biggest enemy is pretty ballsy."

    show ra smile
    ra "Yeah, yeah. I'm only going for you. And maybe the dog."

    mo "Definitely the dog!"
    mo "Anyway, it starts in a couple hours so we should start getting ready, I think!"
    
    show mo smile
    mo "We can't pull up to a Halloween party without any costumes on, that's like...Mac without Cheese."

    "With the air cleared, Monique seems to be in a much better mood."

    "Maybe it'll be okay for Rachel to go after all."

    stop music fadeout 1.0

    jump halloween_party

    
label halloween_party:
    
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    scene bg black
    with fadeLong

    "At first, the prospect of a simple high school Halloween party doesn't seem like that big a deal."

    "An assumption like that is simply foolish."

    "At a party, teenagers are all grouped and condensed together under one roof."

    "They all engage in and participate in absurd levels of underage drinking."

    "They dance obscenely to foul music not appropriate for their age."

    "And worse of all, they go snooping around in rooms not designated for partygoers, rummaging through sensitive belongings they have no business seeing."

    "High school Halloween house parties are repugnant, and so are its attendees."

    "Not to mention, teenagers can be ruthless and cold."

    "They are not particularly welcoming of outsiders."

    "All of these things together create the most abhorrent environment."

    "They are not places for fun."

    $ renpy.music.set_audio_filter("music", walkie_talkie_af, replace=True)
    play music "Rattled.wav" volume 1.0 fadein 1.0
    scene bg partyexterior
    with fadeLong

    "Standing now at the base of the porch, with party lights flashing through the windows, Rachel finds that she has never felt more like an outsider than she does right now."

    "The blaring, festive music does not do much to quell her everlasting nerves."

    "Rachel's anxiety is made noticeable by Monique, who offers a small smile of sympathy."

    show mo concerncos at posRight with moveinright

    mo "Hey, you don't look too hot."
    mo "It's not too late for us to turn back."

    show ra timidcos at posLeft with moveinleft
    ra "No, we're already here."
    ra "And, it's fine, really."
    ra "My costume hides most of my defining features, so I doubt anyone will notice me."

    show ra smilecos
    "Clad in a dark, grim reaper cloak with fraying edges, Rachel pulls the hood further over her head with the hopes of obscuring her identity further."

    "Not the most creative costume, but if it does the job of keeping her out of the host's line of sight, then it's good enough for her."

    show mo gentlecos
    mo "Speaking of costumes, I didn't overdo it, did I?"

    "Monique gives Rachel a little twirl of her costume; a sparkly green fairy outfit."

    show ra shockedcos
    ra "No no, you look great, Moni!"
    show ra defaultcos
    ra "You're supposed to be that one green fairy from those animated movies, right?"

    show mo defaultcos
    mo "Oh my God, NO!"
    mo "I'm Ashia, from Blinx Club!"

    show ra smilecos
    ra "Hm, doesn't ring a bell."
    ra "Green animated fairy it is."

    show ra timidcos
    mo "raCHEL!!"

    "With a playful smack from Monique, a chuckle from Rachel, and her spirits lightly eased, Rachel's gaze fell back on that house."

    show ra smilecos
    "When she's with Monique, it feels like all her troubles wash away into nothing."

    "She almost forgot about the house she had yet to step foot into."

    show ra defaultcos
    show mo smilecos
    "But, you can only put things off for so long."

    "Her gaze falls back onto Monique, who has already taken a step up the porch stairs, waving for Rachel to follow."

    "If someone were reading Rachel's mind, they would hear, \"Do it for Moni.\""

    "But thankfully, nobody is reading her mind at the moment."

    "Reluctantly, she follows her friend inside..."

    $ renpy.music.set_audio_filter("music", None, replace=True)
    scene bg partyinterior
    with fade

    "The first thing Rachel notices is the noise."

    "The music is exceptionally loud, and yet she's still able to hear the chatter of some people nearby."

    "She pulls the hood further down her face and keeps her gaze cast down, in case she accidentally makes eye contact with someone."

    "The second thing she notices is the sheer amount of people."

    "When Monique mentioned that the upperclassmen were invited, she assumed the lack of specification was due to the inconvenience of having to clarify which classes and which students were attending."

    "But, after her first glance around the living room, it really does feel like the entirety of the junior and senior classes are at this house."

    "She has no doubt that more are upstairs and in the backyard."

    "A wave of nausea grips at her, but she fights back the anxiety as best she can."

    "The third thing she notices are the decorations."

    "The only light sources available are from the little halloween decorations scattered through the house, as well as the little disco lamps set up on some tables."

    "Rachel appreciated the dark lighting."

    "And, fourth..."

    "Dog" "Woof!"

    "...little party puppy...how adorable."

    "The family dog is a lot larger now, fully grown and excitedly running between party goers and jumping on people."

    "This party just went from a 0 to a 3."

    show mo defaultcos at posRight with moveinright

    
    mo "Oh my God, Rach!! They have glowsticks!"

    show ra defaultcos at posLeft with moveinleft


    "Pulling her attention back to Monique, Rachel peers up from under her hood, and notices that people had different colored glowstick wristbands."

    "She spots a small table next to the snacks containing different piles of different glowstick colors along with labels, though she can't make out the words from this distance."

    "She gestures to the table."

    ra "Wanna grab some?"

    show mo smilecos
    "Monique beams and grabs Rachel's wrist, pulling them both to the glowsticks."

    "Now upon closer inspection, Rachel could make out the labels and their assigned colors."

    "Pink - Taken. Blue - Single. Green - Complicated."

    "Monique grabs a green glowstick for herself and a blue one for Rachel."

    show mo defaultcos
    mo "Hey, mine goes with my costume!"

    show ra smilecos
    ra "Oh yeah, it does."
    show ra defaultcos
    ra "I don't know if a glowstick would be good for me to have, though."
    ra "Wouldn't it...draw unwanted attention?"

    mo "Oh PLEASE, look around! Everyone has one!"
    show mo gentlecos
    mo "I think you'd get more attention if you didn't."

    ra "I guess so."

    "Rachel takes the glowstick from Monique and clasps it around her wrist."

    "Her grim reaper sleeve is long enough to cover it, but the glow still shines faintly through the fabric."

    mo "Actually, maybe it would be better if you had a pink one, so no one tries to approach you?"

    show ra frowncos
    ra "I don't think that'd be a problem, I mean I'm covered from head to toe in a black cloak."
    ra "No one would even know what I look like to even want to approach me."

    "Despite her words, it appears that she doubts the validity of them."

    show mo defaultcos
    mo "You never know, some people are into the whole mysterious thing."

    "Monique hands Rachel a pink glowstick, just in case."

    "The redhead slips the blue glowstick off her wrist and sets it down back in the pile, with the pink one now in its place."

    show ra defaultcos
    ra "So like, what now?"
    ra "You know parties better than me, so..."
    ra "What do y'all do for fun?"

    show mo smilecos
    mo "Well, normally I find where the games are and go from there, but since we're laying low, I think we can pass on those for now."

    "Rachel's expression twists slightly."

    show ra frowncos
    ra "No, wait, I don't wanna be the reason you miss out on your games."

    show mo gentlecos
    mo "You aren't the reason for anything!"
    show mo defaultcos
    mo "It's your first party in like, forever, I wanna help you make it fun!"
    mo "Actually, elementary school dances don't count, so this is officially your first party in my own humble opinion."
    mo "And because of that, we're gonna figure out what you like at parties, not what I do already."
    show mo gentlecos
    mo "Okay?"

    show ra sadcos
    ra "..."
    show ra smilecos
    ra "...Mkay."

    "Rachel has a seemingly difficult time telling her \"no.\""

    "It appears to have become a pattern over the years."

    show mo smilecos
    "Monique smiles and begins scanning the room."

    mo "I think we should start in here. What do you think?"

    ra "We should..."

    show mo defaultcos
    show ra shockedcos
    "Before she can make a decision, a small, wrangled noise pulls itself from Monique's throat."

    show ra defaultcos
    "It was probably a sound of excitement, to be honest..."

    mo "Rachel, look!! There he is!"

    "Rachel looks to where her friend is pointing, and through the dark lighting of the room was able to make out someone."
    
    "They looked to be dressed up as a fictional character of some sort, with a styled wig and what looked to be a professional made outfit to match."

    "The character doesn't ring any bells for Rachel, but the craftsmanship is admirable."

    "Rachel pulls her hood down further as though she were ashamed of her own store-bought costume."

    mo "Oh oh oh, look! He's looking around for me, I think!"

    show ra frowncos
    ra "Hm."
    ra "Sounds about right."

    show mo gentlecos
    "Monique's toothy grin settles on her friend, and she falters for a moment."

    "It's no surprise that Rachel isn't the most enthused at the prospect of her friend's eye candy showing up to the party."


    "After all, it meant that her friend would leave her alone to go socialize with him, and while she was okay with it at home, she couldn't help but regret her decision just a smidge."

    show ra sadcos
    "Anxiety wells in her stomach."

    show mo concerncos
    "As though she could sense it, Monique gently rests a hand on Rachel's forearm."

    mo "Hey...you sure you'll be okay?"
    show mo gentlecos
    mo "It's not too late to back out and go home."
    mo "We can chill at your place and watch scary movies while the neighborhood kids come by for trick-or-treating!"
    mo "It's no issue at all, seriously."
    mo "You can back out at any time."

    show ra frowncos
    ra "No."
    show ra timidcos
    ra "I mean, n-no thanks, I want to do this."

    "She does not."

    ra "I gotta face these fears eventually, right?"
    show ra smilecos
    ra "Go talk to him, I'll...be here."

    show mo concerncos
    mo "And that's what you genuinely want?"

    show ra sadcos
    "No."

    show ra smilecos
    ra "Yeah."

    "The two of them knew fully well that Rachel wasn't being honest, but Monique knows how stubborn her friend can be and chooses not to press further."

    mo "Alright Rach, I believe you."
    show mo gentlecos
    mo "And my phone will be on me, like, the whole time, so if you wanna leave just shoot me a text and I'll head over!"

    hide mo with moveoutright
    "Rachel nods, and with that she watches her friend gravitate towards the object of her attraction, her sparkly costume twinkling under the lights."

    show ra defaultcos
    "Rachel, now alone, stands awkwardly in the living room, watching other people socialize with the distinct feeling of not belonging."

    "All these people, talking and having fun without any cares in the world...their nights would sour immediately if they knew she was hiding in the crowd."

    "After all, the only reason she's even here is so her friend can hang out with someone else."

    show ra sadcos
    "What was even the point of being here besides inconveniencing other people?"

    "Her eyes almost well up with self-inflicted guilt."

    show ra defaultcos
    "Swallowing the lump in her throat, she decides that if she's here, she may as well take a look around the house."

    "It has been a while, after all."

    "Where will Rachel go first?"

    menu:
        "Migrate back to the snack table.":
            $ celineFirst = True
            call celine_party from _call_celine_party
        "DOG DOG DOG DOG DOG DOG":
            $ cliffFirst = True
            call cliff_party from _call_cliff_party

    scene bg partyinterior
    with wipeleft

    "Well, that went about as expected."

    "After that lively encounter, Rachel decides she's had enough and contemplates sending Monique a text so they could leave."

    "It may take a while for her friend to come get her, so Rachel would still have time to finish up whatever it is she needs to do before then."

    "Send Monique a text?"

    menu:
        "Yes.":
            $ sendText = True
            "Rachel quickly shoots Monique a text asking to wrap things up so they could leave."

            "Pocketting her phone, Rachel glances around the area again." 

            "She should keep herself busy while she waits."

            "Ideally without another harrowing encounter."
        "No.":
            "Upon further contemplation, Rachel shoves down her insecurities and discomfort."

            "She would rather die than impose herself on Monique's time with her crush."

            "She will wait for her friend to come to her, instead."

            "Until then, she should do something to busy herself."

            "Ideally without another harrowing encounter."

    if celineFirst == True:
        menu:
            "DOG DOG DOG DOG DOG DOG":
                call cliff_party from _call_cliff_party_1
    else:
        menu:
            "Migrate back to the snack table.":
                call celine_party from _call_celine_party_1

    stop music fadeout 2.0
    scene bg partyinterior
    with wipeleft

    "--?!"

    "There's a sudden rush of people, and an increase in the chatter."

    "It looks like they're all heading for the exit."

    play music "Breath.wav" #fadein 2.0

    "Did something happen?"

    if sendText == False:
        "As people rush by her in a blur, Rachel is able to make out a sparkly green costume heading towards her, squeezing past the traffic."

    show mo concerncos at posRight with moveinright


    mo "What's with the commotion?"

    show ra defaultcos at posLeft with moveinleft

    ra "Maybe the party is over?"

    show ra frowncos
    "She wishes that were the case, but a sense of dread and impending doom give her the feeling that it's something else entirely."

    show mo gentlecos
    mo "C'mon, let's go check it out!"
    show mo defaultcos
    mo "We were just leaving, anyway, so might as well see what the fuss is about before we go."

    "The two of them follow the small crowd, luckily not needing to shove past too many people since not everyone has caught wind of whatever was going on outside."

    "Rachel can't help but shudder, feeling that impending dread crawl back up her neck, the hairs standing on end."

    scene bg partyporch
    with fadeLong
    $ preferences.afm_enable = False #forcibly disabling autoplay bc i am ANNOYED!!

    "It's no surprise that people are crowding around the door, both indoors and out, making it difficult for Rachel and Monique to get a good view of whatever everyone's doing."

    "In all the chaos, Rachel's cloak hood has slipped down to rest on the nape of her neck, her anonymity long gone."

    "But, no one seems to care about her."

    "At this time, their eyes are all locked on a figure, standing at the end of the pathway leading up to Celine's house, shroud in shadow."

    "Biscuit, who had trailed after the crowd, now stands near the front of the porch, hackles raised as a growl rumbles in her throat."

    "It's hunching over, and slowly making its way towards the house."

    "Rachel's heart sinks further."

    "She tugs on her friend's arm, desperation clouding her voice."

    ra "Moni, we need to go, NOW."

    "But, the figure has gotten too close now."

    "It is blocking the steps to the porch, leaving no room to exit."

    "It is now, illuminated by the decorations and the moon's light in the sky, that Rachel is able to make out what-or rather who- the figure is."

    "Clothes tattered and frayed, showing signs of weathering, but not use."

    "Hair unkempt and tangled, with debris entwined but still somehow flawlessly draping across shoulders."

    "Eyes glazed over, peering between overgrown bangs and seemingly unfocused."

    "Skin ghostly white, mirroring that of a corpse but with just enough life left in the complexion to be considered breathing."

    ra "Is that-?"

    transform miaCenter:
        xpos 0.30
        ypos 0.15

    show mi partydark at miaCenter with dissolve
    "There stands Mia before the crowd."

    "She is as beautiful as ever, even in this decrepit state she finds herself in."

    "And, at the sound of Rachel's voice, her head shoots up to leer directly at her."

    "With her palm outstretched, breath labored, and stiff, creaking movements, nobody could possibly prepare for her sudden dash up the porch..."

    "...her nails aimed directly for Rachel's heart."
    jump endcredits

label endcredits:
    # $ preload_images(["thanks for playing"])
    $ quick_menu = False
    $ renpy.music.set_volume(0.5)

    show screen noclick
    scene black
    with Pause(3.0)

    show endcreds with dissolve
    with Pause(8.0)

    stop music fadeout 2.0
    scene black with dissolve
    with Pause(3.0)

    hide screen noclick
    $ preferences.afm_enable = False 
    return




label rachbedroom_insist_mo_goes:
    # $ preload_images(["ra default", "ra frown", "ra sad", "ra shocked", "ra smile", "ra timid",
    # "mo angry", "mo concern", "mo default", "mo gentle", "mo smile", "bg rachelsbedroom"])
    show ra smile
    ra "No, you should go."
    ra "Forget about me for a second. Do what feels good to you."

    show mo concern
    mo "What feels good to me is making sure you're okay, and it doesn't seem like you are!"
    mo "And besides, I don't even know if I'd want to go anyway."
    mo "Rachel...Celine is like, your biggest hater."
    mo "Sure, you have a reputation of sorts, but she's like, the CEO of the Anti Rachel Regime."

    show ra frown
    ra "Yeah, well, she can suck it up for once."

    mo "Suck it up?"
    mo "How can you expect her to suck it up when she thinks you're the reason her sister is missing?"
    mo "With a grudge THAT big you'd think she would crush half the cheer squad with all that weight."

    show mo gentle
    ra "Moni, be serious."

    mo "I am serious! I don't get how you're so comfortable with this."

    ra "Well, I am, so just drop it okay?"
    return

label rachbedroom_disuade_mo:
    # $ preload_images(["ra default", "ra frown", "ra sad", "ra shocked", "ra smile", "ra timid",
    # "mo angry", "mo concern", "mo default", "mo gentle", "mo smile", "bg rachelsbedroom"])
    show ra sad
    ra "Hey...I'm sure it'll be super boring anyway."
    ra "It's not like they've got anything that you don't already have."
    ra "And… it's like you said, right? You can see him again on Monday?"

    show mo concern
    "Monique averts her eyes."

    show mo gentle
    mo "...They got a Pac-Man machine."

    "Damn. They really do got everything."

    "Now it's Rachel's turn to look away, though this time it's out of guilt."

    "She thought back to their years together in this small town, where word travels fast, and furious."

    "Reference aside, Rachel mentally acknowledges how these years of ridicule were not only difficult on her, but her friend as well."

    "Monique no doubt faces similar scrutiny from peers due to association."

    "Her social life seems to be mostly fine, but was Rachel really going to deny her something she appears to want so badly, for her own selfish reasons?"

    "And with Monique looking down like that, she knew she couldn't say no."

    show ra default
    ra "..."
    ra "God, I feel like a jerk."
    show ra smile
    ra "You shouldn't not go because of me, Moni."
    ra "It'll be fun, I think!"

    show mo concern
    "Monique slowly looks back at Rachel, a quizzical expression forming."

    mo "...Are you serious?"

    show ra smile
    "A small smile forms on Rachel's face."

    ra "Yeah, forget about me for a second. Do what feels good to you."
    ra "I'll be fine."
    return

label rachbedroom_ra_fine:
    # $ preload_images(["ra default", "ra frown", "ra sad", "ra shocked", "ra smile", "ra timid",
    # "mo angry", "mo concern", "mo default", "mo gentle", "mo smile", "bg rachelsbedroom"])
    show ra timid
    ra "You know what? I'll be fine."
    ra "Why don't you tell me what it's like after?"

    show mo concern
    mo "Rach, are you serious? I can't do this by myself!"
    mo "Sure I'm...more social than you are, but we're a team!"
    show mo gentle
    mo "You know, the whole Dastardly Duo or whatever."
    mo "Besides, I don't want to go there just KNOWING it's a place that might not accept you...No offense."

    show ra smile
    "Rachel smiles at Monique, but it doesn't quite reach her eyes."

    ra "I honestly don't mind."
    ra "You can get some sweet info on what people think about me!"

    show mo angry
    mo "This isn't the time to joke! Celine literally hates your guts."
    show mo concern
    mo "She thinks what happened is your fault!"
    mo "How can I just leave you for that?"

    show ra default
    ra "Look, that doesn't matter when you're not even going for her!"
    ra "She won't even know you're going until you're there."

    mo "That's my point! So either we both go or I just lie and hang out with you eating chips and dip all night!"

    "That did sound good."

    "But she couldn't get in the way of Monique's life, she'd supported her all throughout high school when everyone was against her..."

    "For Moni, she'd push her issues aside."

    show ra timid
    ra "Alright, you got my hands tied."
    show ra smile
    ra "Do what feels good to you, I'll be right beside you."
    return



label celine_party:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    scene bg partyinterior
    with wipeleft

    show ra defaultcos at posLeft with moveinleft

    "Making her way back to the snack table, Rachel makes sure to keep her head down."

    show ra shockedcos
    "A little too down, however, as she ends up running into somebody on her way there."

    show ra frowncos
    "The cup of punch the person was holding ends up splashing onto Rachel's cloak, drenching the front in a sticky red substance."

    "Rachel looks up to apologize for not watching where she was going, but freezes the moment she catches a glimpse of who it is."

    show ra shockedcos
    "Oh."

    "Oh no."

    show ce worrycos at posRight with moveinright
    
    ce "Oh my gosh, I'm so sorry!!"

    "It's Celine."

    "Luckily, if her friendly and apologetic tone is something to go off of, it seems she hasn't noticed who exactly bumped into her."

    "Looks like the lighting of the room helped obstruct her identity."

    "Also, Celine is a bit taller than her, and the hood of her cloak is still pulled up over her head, so maybe her face is still a bit hidden?"

    show ra timidcos
    ra "Oh, um, it's alright."

    ce "Here, I'll help you clean this up."

    "Before Rachel can refuse, Celine grabs her wrist and drags her to the snack table, snatching a couple napkins before furiously scrubbing at the wet patch."

    "Well, that's one way to get to the snack table."

    ce "Ah-it's a bit hard to see if I'm helping at all since the fabric is black..."

    show ra smilecos
    ra "It's okay, really."
    ra "You really don't have to do that.."

    show ce smilecos
    ce "Pshh, nonsense."
    ce "I spilled my drink on you so it makes sense that I help you get it out!"
    ce "I hope I didn't ruin your night!"
    ce "Are you enjoying the party so far?"

    menu:
        "Lie.":
            pass
        "Lie.":
            pass
    #there are two bc i think its funny heh

    show ra timidcos
    ra "Yeah, it's fun."
    ra "I uh, like what you did with the place."
    show ra smilecos
    ra "Decorations are real...lively?"

    show ce sneercos
    ce "HA, that was awful!"
    show ce smilecos
    ce "I'll need to kick you out if you make another shitty pun like that."

    "Oh, that wasn't even intentional."

    show ra timidcos
    ra "Hahaha yeahhh..that'd suck."

    show ra smilecos
    "So far Celine doesn't appear to recognize Rachel, but alarm bells can't stop going off for her."

    "She looks visibly jittery."

    show ce worrycos
    ce "Hey, you okay?"
    ce "You look like you're boutta jump outta your skin."
    show ce sneercos
    ce "I know, my costume is terrifying."

    show ra timidcos
    "Rachel forces out a chuckle."

    "She needs to find a way out of this conversation, FAST."

    show ce smilecos
    ce "So...you were heading to the snack table when I bumped into you, right?"
    ce "I'll fix you a plate!"

    show ra shockedcos
    "Before Rachel can protest, Celine already begins grabbing different foods from the table, piling it with an absurd amount of snacks."

    show ra defaultcos
    ce "I'm not sure what you like, so I just grabbed you a bunch of everything."
    ce "Help yourself to the punch, too!"
    ce "It's my own blend of juice and sodas, REAL good if I say so myself."

    "Celine continues to speak, always the chatterbox."

    "She's so energetic and lively, it's jarring when compared to how she normally treats Rachel."

    "Despite how desperate Rachel is to leave this conversation, she can't help but partly wish it could go on further."

    show ra sadcos
    "She misses talking with her peers."

    "But, she knows it's fleeting, and that the longer it goes on, the more likely she is to be caught."

    "Maybe now's the time to leave."

    menu: 
        "Distract Celine.":
            show ra timidcos
            ra "Haha...um, I might be sick if I drink anymore punch."
            ra "...It's almost too good!"
            show ra smilecos
            ra "I was...uhh..."
            ra "Planning on getting something to eat..."
            show ra timidcos
            ra "to see if that...helped...?"

            show ce worrycos
            ce "Wow, you really don't sound good, are you okay?"
            ce "Need to sit down for a bit?"

            show ra shockedcos
            "Before Rachel can protest, Celine takes her hand in her own and raises the other as if to check her temperature."

            "And, a little too late, Rachel realizes that she's staring directly into Celine's face, her cloak no longer obscuring her vision."

            "And, by extension, her face."

            show ce angrycos
            "Celine retracts her hand as though she were burned, anger brewing in her expression."
        "Slowly back away.":
            show ra frowncos
            "Rachel tries using Celine's turned back as an opportunity to disappear back into the crowd." 

            "Slowly backing up, her eyes stay glued onto the other girl."

            "She prepares to make a dash into a dark corner somewhere for the rest of the night, if all goes well."

            show ra shockedcos
            "But, unfortunately she's too distracted with Celine, and fails to notice that she accidentally walked into another guest who pulls on her hood in annoyance."

            show ra frowncos
            "Shoot."

            "And, just her luck..."

            "Celine turns back around to see the distance that has been created, just as her cloak hood is yanked from her head."

            ce "Anyway, I don't bite, y'know-" 

            show ce neutralcos
            "They both freeze as they enter an unspoken staring context, though Celine is the first to lose."

    show ce angrycos
    ce "raCHEL?!"

    if celineFirst == False:
        jump celine_party_2
    
    show ra frowncos
    "Well, shit."

    "If only someone were here to swoop in and save Rachel from this absolutely atrocious position she finds herself in."

    "This conversation barely started and it's already going to shit."

    "Well, it's less of a conversation and more like an enforced confrontation."

    "Regardless of what it is, Rachel wants out."

    ce "You have a lot of nerve showing your face around here."
    ce "Since when do you even like parties anyway?"

    ra "Never."

    show ce sneercos
    ce "HA!"
    ce "So you're just here to cause a scene then, huh?"
    ce "Sounds about right."
    ce "You always hated being pushed to the side, always wanting to be the center of attention."

    ra "?!"
    ra "No??"
    ra "I freaking hate attention, where the hell did you get that info??"


    ce "I don't need to hear it from anywhere, it's so obvious."
    show ce eyerollcos
    ce "You love when things revolve around you, you're always trying to play the victim card so people fawn over you."
    ce "And you hate when people call you out on your bullshit."
    show ce angrycos
    ce "Well, too bad Rachel."
    ce "I can see right through you."
    show ra sadcos
    ce "You're a two-faced bitch."

    "Celine is probably the only person in the world who manages to be so scary in a deer costume."

    "She was right about what she said earlier."

    "She's terrifying."

    ra "..."
    show ra frowncos
    ra "I wish I had your confidence."
    ra "You're dead wrong."

    "Her voice still wavers, despite her attempted bravado."

    show ce sneercos
    ce "Oh, real funny word choice, Rachel."
    show ce angrycos
    ce "What even is your costume anyway?"
    ce "The grim reaper? Hilarious."
    show ce eyerollcos
    ce "You're honestly not even trying to hide it anymore."

    show ra shockedcos
    ra "!!"
    show ra frowncos
    ra "T-That was entirely unintentional!"
    ra "I just needed something simple and subtle, that's all."
    ra "You're reading into it."

    show ce sneercos
    ce "Oh, gaslighting now too?"
    ce "Looks like you CAN go lower."
    ce "Wish I could say I'm surprised."

    show ra sadcos
    "Rachel's eyes frantically dart across the room, trying to find a way out of this conversation."

    "No matter how hard she tries, her words come out all wrong."

    "But, Celine is relentless."

    show ce angrycos
    ce "You're disgusting."
    ce "Showing up to MY house, of all places, for MY party-"
    show ce eyerollcos
    ce "-knowing how I feel about you."
    ce "How EVERYBODY feels about you..."
    show ce angrycos
    ce "It's like you don't even care about how others feel."
    ce "You'd rather make everyone else uncomfortable as long as you get what you want."
    ce "I'd tell you to get the hell out of my house, but I don't wanna be a bad host-"

    show ra frowncos
    "-NOW she thinks about being a bad host??-"

    ce "-So instead I'll tell you to leave me the hell alone for the rest of your time here."
    ce "You won't touch anything, you won't leave the living room, and you won't talk to anyone."
    ce "As a matter of fact, if you so much as LOOK at anyone, I'll smack the shit out of you for disturbing my guests."

    show ra sadcos
    ra "Celine..."
    show ra frowncos
    ra "I'm sorry I'm hurting you, but you have to understand I-"

    show ce sneercos
    ce "Disrespectfully I don't give a shit about what you have to say to me."
    ce "I don't think I've ever hated anyone more than I hate you."
    ce "The only reason I'm tolerating you being here is because I know Mia liked you."

    "Rachel's throat tightens."

    ra "Celine, what happened with Mia..."
    ra "It hurts me as much as it hurts you."

    show ce angrycos
    "Celine's face contorts furiously."

    "Way to go, Rachel."

    ce "Are you..."
    show ra sadcos
    ce "Are you kidding me?"

    "Celine scoffs in disbelief."

    ce "You've gotta be joking."
    ce "There's no way you just said that to me."
    ce "It hurts YOU as much as it hurts me?!"
    show ce sneercos
    ce "I'd laugh if I could."
    ce "Do I need to remind you that you're not the one whose sister vanished into thin air?"
    show ce angrycos
    ce "You're not the one who has to deal with the fact that everyone else has moved on but you."
    ce "My friends moved on, the police moved on..."
    show ce eyerollcos
    ce "Hell, even my own parents have moved on."
    show ce angrycos
    ce "Nobody even cares about her anymore, Rachel."
    ce "How could you possibly understand, when it's your own fault she's gone?!"
    ce "You refused to tell the police anything, even though you KNOW what happened because you were there!!"
    ce "And because of you, they have nothing to work with."
    show ce defaultcos
    ce "You did something, I know you did."
    ce "I don't have proof, but I can tell when someone's guilty, and it's written all over your ugly face."
    ce "It's all your fault."
    show ce angrycos
    ce "And I have to watch you get away, scot-free, while Mia's still out there."
    ce "If it weren't for you, she'd still be here."
    ce "She'd be here, and she'd be happy."
    show ce defaultcos
    ce "I'd be happy."

    ra "..."

    show ce angrycos
    ce "...Stay the hell away from me."
    return

transform celinepartyleft:
    xpos -0.05
    ypos 0.15

transform celinepartyright:
    xpos 0.65
    ypos 0.15

label celine_party_text:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    "Before Celine can respond, a familiar voice breaks through all the noise."

    show mo concerncos at celinepartyright with moveinright
    show ra shockedcos
    show ce defaultcos with moveinright:
        xpos 0.5
    mo "There you are!"
    mo "I got your text, is every-"

    "Monique freezes mid-sentence the moment she sees who it is Rachel is speaking to."

    mo "Oh."
    mo "Oh no."
    hide mo with moveoutright
    show ce at celinepartyright with moveoutright
    show mo gentlecos at Transform(xzoom=-1.0) with moveinleft:
        xpos -0.05
        ypos 0.15
    show ra with moveinleft:
        xpos 0.15
    mo "Hey...Celine..!"
    mo "What brings you here?"

    show ce eyerollcos
    ce "Oh, you know, just hosting MY party."
    ce "MY party, which Rachel apparently thought was a good idea to come to."

    show ra sadcos
    ra "Wasn't my idea, for the record."

    show ce angrycos
    ce "How about you worry about your criminal record instead?"

    show mo angrycos
    mo "Hey, lay off Rachel!"
    mo "She's not all that, okay?"

    ce "She's \"all that\" and then more, I can promise you that much."
    ce "Tell me, what exactly do you know about her?"

    mo "I know that you guys all blame her for something that wasn't her fault!"
    mo "Everyone else, I understand."
    mo "But YOU?"
    mo "Celine, you can't be this dense as to think that Rachel of all people could be behind a missing person's case."

    ce "Are you saying I'm stupid?!"

    mo "Well, if the shoe fits!"

    show ra frowncos
    ra "Guys-"

    ce "What the hell are you two even doing at my house anyway?!"
    ce "Did you just come here to insult me? Because you're playing a dangerous game."

    mo "No, insulting you is just the bonus!"
    mo "I'm here for someone better than you, Rachel just agreed to tag along out of the goodness of her heart."

    show ce sneercos
    ce "Oh yeah?"
    ce "I didn't think there could be any \"goodness\" left in that cold, still heart of hers."

    show ra defaultcos
    ra "Can we calm down-?"

    mo "Yeah, well, you'd notice if you took two seconds to pull your head out of your own ass."
    mo "Rachel is a good person, my intuition is never wrong!"

    ce "Well, first time for everything, right?"

    mo "Not for you, since you clearly have a lotta experience in being a huge bitch."

    show ce angrycos
    ce "You call me a bitch again and I'll be mopping the floor with you."

    mo "Fine then!"
    mo "You couldn't win even if you wanted to!"
    mo "You're just mad because you know you're in the wrong and you hate it!"
    mo "You hate knowing I'm a better person than you, and you hate that Rachel is even better too!"
    mo "Just because it's your party doesn't mean you get to get all pissy if someone stands against you for being a bully."
    mo "Leave Rachel alone, and I leave you alone."
    mo "It's that easy!"

    show ce angrycos
    "Celine's eyes narrow into a harsh glare."

    ce "Bully?!"
    ce "Oh, so I'm the bad guy for calling out the person who caused my sister's disappearance?"

    mo "YES, because you don't have actual proof!!"
    mo "You know it's not actually her fault, you just want someone to blame!"

    ce "I don't need proof, I know she was involved and that she refuses to take accountability for anything!"
    ce "That screams \"guilty\" to me."
    ce "If you're that willing to defend a horrible person, be my guest, but do it where I can't see."
    ce "Finish whatever business you came here for and get the hell out of my house."
    ce "I don't wanna see either of you anywhere near me or my guests, you hear me?"

    mo "Or what?"
    mo "You'll call the police on us?"

    show ce neutralcos
    ce "Yes."

    show mo concerncos
    show ra frowncos
    mo "..."

    "Monique turns to Rachel for the first time in this entire encounter with a whisper."

    mo "I lowkey didn't think she would say yes to that."

    "They both look at Celine's rigid stand and realize she means business."

    "That's their cue to leave."

    show mo angrycos
    mo "Fine, we'll get out of your dead, damaged, dry hair."

    show ra timidcos
    ra "Uh, we'll leave, is what she's trying to say."

    mo "I said what I said and I meant it."

    "The two of them turn their backs to Celine, already excusing themselves from that dreadful conversation."
    return

label celine_party_2:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    show ra frowncos
    "Damnit."

    "Just her luck."

    "First Cliff recognizes her, now Celine..."

    "Who's next?!"

    ra "Oh, great."
    ra "I can't seem to catch a break, can I?"

    show ce eyerollcos
    ce "Oh, YOU can't catch a break?"
    ce "I should be the one saying that, actually."
    show ce angrycos
    ce "What the hell are you doing here?!"

    "Rachel sighs exasperatedly."

    ra "I'm just here for my friend, I'm not actually here for the party."

    ce "Yeah, right. I know you're just here to get on my nerves."
    show ce sneercos
    ce "\"I'm just here for a friend!!!\""
    show ce eyerollcos
    ce "PLEASE, save it for someone who's stupid enough to care."

    "Normally, Rachel would be much softer spoken and passive in a situation like this."

    "Basically, a total pushover."

    "But after the dumpster-fire encounter with Cliff, her reservations have gone down from 95\% to maybe 30\%."

    show ra defaultcos
    ra "Okay fine, don't believe me."
    ra "Not like that's anything new, anyway."
    show ra frowncos
    ra "I'm used to people thinking I'm a liar."

    show ce smilecos
    ce "Aww, poor you, playing the victim card already?"
    show ce neutralcos
    ce "You're so pathetic."

    ra "If I'm so pathetic, then what are you?"
    ra "You're stooping to my level by having this conversation with me."
    show ra sadcos
    ra "Just kick me out and save yourself the trouble."

    show ce eyerollcos
    "Celine scoffs, looking down her nose at Rachel."

    "They aren't too far off in height, but it feels like Celine is towering over her."

    ce "No, you deserve to stand here and listen to everything I have to say about you."

    show ra frowncos
    ra "Ughh, I'd rather not."
    ra "I already had to deal with Cliff being stupid and bothering me, I don't really feel like having the same conversation twice."

    show ce angrycos
    ce "You just got here and you're already harassing my guests?!"

    ra "NO???"
    show ra shockedcos
    ra "Did you not hear what I just said?"
    show ra frowncos
    ra "He harassed ME, not the other way around!"

    show ce sneercos
    ce "Yeah, and I'm running for president."
    ce "You know, I may have believed your lies when we were kids, but I know better now."
    show ce angrycos
    ce "I'm not the stupid little kid you still think I am."

    ra "Celine, I never thought you were stupid...who even told you that?"

    if sendText:
        jump celine_party_text

    ce "I don't need anyone to tell me to know it's true."
    show ce neutralcos
    ce "You and Mia...you two were so close it makes me sick."
    show ce angrycos
    show ra sadcos
    ce "How could you just...tear her away from me like that?"
    ce "Even before she disappeared you were stealing her from me."
    ce "You started shutting me out in my own house."
    ce "You never gave me the time of day."
    show ce neutralcos
    ce "Even when I looked up to you."

    show ra defaultcos
    ra "Celine..."

    show ce angrycos
    ce "Shut the hell up."
    ce "I hate you so damn much."
    ce "You stole everything from me, you ruined my life."
    ce "I don't wanna hear any useless apologies from you unless your apology is bringing back my sister."
    show ce neutralcos
    ce "Everyone thinks she's dead but I know she's out there somewhere."
    ce "And I know she's crawling her way back here, little by little, just to exact karma upon you."
    ce "Because God knows you deserve everything that's coming to you."

    "They stare at each other in silence, despite the ongoing music."

    show ce angrycos
    "Celine's face twists into one of disgust."

    ce "Really?"
    ce "Nothing to say for yourself?"

    show ra sadcos
    ra "I feel like no matter what I say, you'll get mad at me again."

    ce "!!"

    show ra defaultcos
    ra "Celine, listen..."
    ra "I'm...sorry you felt singled out when we were kids."
    ra "I never meant for you to feel that way."

    "Celine crosses her arms."

    show ce eyerollcos

    ce "Yeah, well, you did so you can't take it back."

    ra "I know, and you're right about one thing."

    show ce defaultcos
    ce "?"

    ra "I do deserve everything that's coming to me."
    show ra sadcos
    ra "I've been feeling so guilty for so many years, I just..."
    ra "I couldn't bring myself to say anything."
    ra "What happened with me and Mia..."
    ra "It changed me."
    show ra defaultcos
    ra "I've hardly been able to come to terms with it myself, after all these years."
    ra "Freshman year feels so long ago, but also so recent."
    ra "It's weird, it feels fresh in my mind but buried so deep that I can hardly bring myself to resurface it all."
    ra "I wanted to tell the police, when they brought me in for questioning."

    show ce neutralcos
    ce "...but you couldn't, huh?"

    show ra sadcos
    "Rachel nods shamefully."

    show ce eyerollcos
    ce "Well, I'm not the police, so you could have at least started by telling me."
    ce "I think I deserve it after all this time."

    show ra defaultcos
    ra "..."

    show ce defaultcos
    ce "Rachel, I need to know."
    ce "Tell me what happened to my sister."

    menu:
        "Tell Celine the truth.":
            pass

    ra "I..."
    ra "..."
    ra "Okay."
    ra "It was four years ago, as you know."
    ra "Mia was dealing with..."
    show ra sadcos
    ra "...problems."
    show ra defaultcos
    ra "Problems she only told me about."

    "Rachel swallows thickly, her pulse quickening beyond the beat of the music."

    ra "She, um..."
    ra "...decided she wanted to get away from them, I guess."
    show ra sadcos
    ra "A-and, asked me to run away with her."
    ra "I said yes, and-"

    show ra frowncos
    "Her mind screeches to a stop, all of a sudden."

    "It appears she can't bring herself to vocalize what happened just yet."

    ra "Actually, never mind."
    ra "I don't think I feel comfortable sharing this with you right now."

    ce "..."
    show ce angrycos
    ce "You seriously expect me to believe that?"
    show ce sneercos
    ce "Mia? Running away?"
    ce "I'd laugh if I didn't wanna actively strangle you."
    ce "You just can't stop with the lies, can you?"

    show ra shockedcos
    ra "No, Celine, I wasn't lying-!"

    show ce angrycos
    show ra defaultcos
    ce "I don't wanna hear it."
    ce "You make me sick."
    ce "I never should've said anything to you."
    ce "Next time, if I want to know about Mia, I'll just figure it out myself."
    ce "I want you out of my house."
    ce "If I see you lurking anywhere around here within the next 15 minutes, I swear I'll call the police."
    ce "Do not test me."

    hide ce with moveoutright
    "Celine stomps off to another part of the house, probably so she wasn't tempted with the urge to strangle Rachel."

    "Left alone at the snack table, Rachel lets out a sigh of pure exhaustion."
    return


label cliff_party:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    scene bg partyinterior
    with wipeleft

    "Barely containing her excitement at the mental reminder of the dog, Rachel makes a beeline toward it."

    "This is quite literally the only redeeming quality of this party; the cute little golden retriever making rounds around the living room."

    "She catches a glimpse of the dog currently jumping on somebody's lap."

    "Or, at least trying to."

    "It's got both its front paws resting on the person's lap."

    "They look to be in a homemade knight in shining armor costume, the armor sheets being made of cardboard and spray painted in metallic silver."

    "The visor of their helmet is down, obstructing their face."

    "She can't help but feel a little stupid for not thinking to buy a mask for her costume as well."

    "The dog, now sensing Rachel's presence, tears away from the knight, eagerly bounding towards her."

    "She doesn't even have time to react before it pounces, sending her to the ground as it licks her face, tail creating an afterimage from the sheer speed of its wagging."

    show ra timidcos at posLeft
        # xpos -0.05
        # ypos 0.2
    ra "Aww, hey buddy!"

    "The dog let out a 'Borf!' and continued its relentless onslaught of slobber."

    ra "C'mon Biscuit, that's so gross!!"

    "Stranger" "Dang, that's the friendliest she's been with people all night!"

    "Rachel glances slightly towards the voice, coming from the person in the handmade knight costume."

    show ra smilecos
    ra "Yeah?"

    "The stranger nods."

    "Stranger" "Uh-huh."
    "Stranger" "She's been hyper and jumping on people, but I haven't seen her topple anyone to the ground like that."
    "Stranger" "I guess she really likes you."

    ra "Yeah, I guess so."

    "As if to confirm the stranger's words, Biscuit tries to reach Rachel's face with even more loving kisses, her head digging under her hood to lick her ear."

    "She tries to push Biscuit back, but her efforts go unnoticed by the golden retriever."

    "Her bright hair spills forward, and the nudging of Biscuit's snout causes the hood to be pushed back ever so slightly."

    "The stranger stiffens before carefully raising their visor to reveal a familiar face."

    show ra shockedcos
    "Stranger" "I don't believe it!"

    menu:
        "Try lowering the hood.":
            pass
        "Go, Biscuit! Attack!!":
            pass

    "It was too late."

    "She REALLY should have invested in a mask or something."

    if celineFirst == True:
        "Twice in one night is just embarrassing."

    "The stranger's face is now in view, and..."

    if cliffFirst == False:
        jump cliff_party_2

    "There's no way."

    show cl sneercos at cliffsFuckassSpecialFunction with moveinright


    cl "Well well well well well well well."
    cl "Well."

    "Oh God."

    show ra defaultcos
    ra "Sigh."
    ra "Hey, Cliff."

    cl "Look what the cat dragged in."
    cl "Or rather, should I say..."

    show cl eyerollcos
    "He goes silent."

    cl "Uh, what even are you?"
    cl "Are you some homeless witch or something?"

    show ra frowncos
    ra "...NO???"
    ra "I'm the grim reaper? I guess?"

    show cl defaultcos
    cl "PFFFT WOWWW."
    cl "That's a bit on the nose, don't you think??"
    cl "That's gotta be intentional."

    ra "It really wasn't..."

    cl "Uh, yeah, sure."
    show cl cockycos
    cl "What prompted you to even show your face here?"
    cl "No one even likes you."

    ra "Geez, what a charmer..."

    show cl defaultcos
    cl "HAHA!"
    cl "No, really."
    cl "What gives?"
    cl "Dude, Celine's gonna flip if she sees you here."
    cl "You better hope she doesn't find you for your sake."

    "The vibes of this guy are so rancid, Biscuit has already scampered away to find some better party goers to jump on."

    "Already, Rachel's main solace has slipped away."

    ra "Yeah yeah, whatever."
    ra "So what're YOU doing at this party?"
    ra "Don't you have those tabletop game meetings on Fridays??"
    ra "Why aren't you there with your loser friends?"

    show cl eyerollcos
    cl "First of all, they aren't losers."
    cl "Real rich coming from the likes of you."
    cl "And SECOND, our meeting got cancelled."
    cl "One of our party members got busy, so we gotta wait til next week."

    ra "Uh-huh..."

    "In the middle of his scrutinization of Rachel, Cliff's eyes zero in on the pink glowstick shining through her costume sleeve."

    show cl sneercos
    cl "Woah, no way."
    cl "Seriously, no WAY!"

    show ra defaultcos
    ra "...?"

    cl "Let me guess, they go to another school?"
    cl "You two met online?"

    show ra frowncos
    ra "Who???"
    ra "Dude I can't ever hold a conversation with you, ever."
    ra "You make zero sense half the time."

    show cl eyerollcos
    cl "Your glowstick, stupid."
    cl "It's pink, you're seeing someone."
    show cl defaultcos
    cl "I mean, pfft, allegedly."

    "Internally, Rachel screams at Monique for ever thinking that the pink glowstick would be a better option than the blue."

    "If Monique knew it would warrant a conversational hostage encounter with Cliff of all people, she may have gotten rid of the entire glowstick pile altogether."

    "However..."

    "Rachel can't possibly pass up an opportunity to mess with this douchebag."

    "If it goes well, then it might be the one good thing to come out of coming to this party."

    ra "...And what's it to you?"

    show cl eyerollcos
    cl "Hm?"

    ra "What's it to you that I'm seeing someone?"

    cl "What's it to me?"
    show cl sneercos
    show ra defaultcos
    cl "HA!!"
    cl "You make it sound like I care about that stuff."
    cl "Heh, no."
    cl "I'm just wondering who in their right mind would ever wanna go out with you."
    cl "Maybe someone with a death wish."

    show ra frowncos
    ra "Yeah?"
    ra "Only someone with a death wish would date me?"
    ra "WOuldn't that make you suicidal?"

    show cl eyerollcos
    cl "HEY, I was doing charity work."
    cl "I mean, no one else was gonna do it."

    ra "YOU? Charity work?"
    ra "Please, it was the other way around."
    ra "You were all alone and I took pity on you."
    ra "Hell, I thought you were endearing, how stupid was I?"
    ra "Pretty sure I was your only girlfriend ever."
    ra "Am I wrong?"

    "Cliff lets out a huff, though it's hard to tell if it's one of irritation or arrogance."

    "Maybe both, honestly."

    cl "Uh, you're dead wrong."
    show cl cockycos
    cl "You may have held the girlfriend title, but I have many suitors just lining up to bask in my radiance."
    cl "Actually, I should be thanking you."
    cl "Breaking up with you after your big fumble with Mia's case was probably the best thing to ever happen to me."
    cl "Everyone took pity on the poor guy who got manipulated into dating the walking Death Curse."
    cl "Thankfully I escaped in time, I'd hate to imagine what might've happened to me if I didn't leave you when I did."

    show ra shockedcos
    ra "...You cannot be serious."
    show ra defaultcos
    ra "You have no idea what that was like for me."
    ra "You weren't even there..."
    ra "You transferred here AFTER everything happened."
    ra "Did you seriously date me for clout?"
    ra "Dude, it wasn't even good clout, everyone hates me."

    cl "All clout is good clout, my dear."

    show ra frowncos
    ra "You talk a lot of smack for a dude whose real name is Cliffington the Second."

    show cl eyerollcos
    cl "SHSHHHHHH!!!"

    show ra shockedcos
    "Cliff smacks a gloved hand over her mouth haphazardly."

    cl "Could you be any louder?!"

    "Rachel tears his hand off her face."

    show ra frowncos
    ra "There's??? Music playing????"
    ra "Literally NO ONE heard me besides you."
    ra "There was no reason to put your gross glove hand on me."

    cl "Oh yeah, sure."
    show cl cockycos
    cl "I'll have you know I come from an honorable family, put some respect on my name."
    show cl eyerollcos
    cl "I won't have a nasty criminal such as yourself slander it."

    show ra defaultcos
    ra "Look, I really didn't do anything."

    show cl cockycos
    cl "Yeah? Then how come you were at the scene of the crime?"
    cl "How come you refuse to say anything about what happened to Mia?"

    show ra sadcos
    "Rachel looks to the side in discomfort."

    ra "I..."
    ra "I can't."
    ra "You don't get it, I can't just talk about something like that."

    show cl defaultcos
    cl "Can't or won't?"
    cl "You're the main suspect here."
    cl "Just because the police excused you from the case, doesn't mean jack to me."
    cl "You know something we all don't, it's obvious."

    show ra frowncos
    ra "That's-"

    show cl sneercos
    cl "You may have fooled the law with your fancy shmancy attorney, but I've got an ace up my sleeve."
    cl "I've got my own source of intel, and I'll make sure the town, no, the whole world knows about your crimes against humanity."
    cl "Watch your back, Rachel."
    show cl eyerollcos
    cl "And for the love of everything Halloween, just get a mask next time."
    cl "It's like you didn't even try."
    return

label cliff_party_text:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    "Before Cliff can finish that train of thought, they're both intercepted by a voice cutting through the noise."

    show cl eyerollcos with moveinright:
        xpos 0.4
    show mo concerncos at celinepartyright with moveinright
    
    show ra shockedcos
    
    mo "There you are!"
    mo "I got your text, is every-"

    "Monique freezes mid-sentence the moment she sees who it is Rachel is speaking to."

    mo "Oh, great."
    mo "It's this guy again."
    hide mo with moveoutright
    show cl at cliffsFuckassSpecialFunction with moveoutright
    show mo gentlecos at Transform(xzoom=-1.0) with moveinleft:
        xpos -0.05
        ypos 0.15
    show ra with moveinleft:
        xpos 0.15
    mo "Don't you have something better to do than to bother Rachel?"
    mo "She doesn't want you bro, move on."

    cl "I beg your pardon?"
    cl "SHE was bothering ME."
    cl "I was minding my business with that cute dog when she stomped up from nowhere, and scared the poor thing off."

    show ra frowncos
    ra "That's not?? How it happened????"
    ra "Biscuit loves me, she left because you were ruining the vibes."

    show mo defaultcos
    mo "Yeah, and probably the air, too!"
    mo "I just know you're stinking up that sweater under all that cardboard."

    cl "Um, I wear deodorant??"

    mo "Could've fooled me!"
    mo "Anyway, that's beside the point!"
    mo "Leave Rachel alone, she doesn't want you around."

    show cl cockycos
    cl "Yeah? You think anyone here wants HER around?"
    cl "You people can be so selfish sometimes."
    cl "You expect everyone to be cool with a potential murderer just hanging out with them, like nothing's wrong?"
    show cl sneercos
    cl "\"Carry on guys, pay no mind to the psychopath 5 feet from you!\""
    cl "That's how dumb you guys sound."

    show mo angrycos
    mo "Oh, we're the dumb ones??"
    mo "You just accused someone of murder with no evidence, and you're acting like it's concrete info!"
    mo "And I heard you wanna be a journalist; not the best look if you're making biased accusations before you've even gotten your name professionally printed."

    cl "I'm not biased, I'm trusting my gut!"

    mo "Yeah, your biased gut!"

    show cl cockycos
    cl "It's not biased for me to say she's the prime suspect, because it's true!"
    cl "There are only so many things that could've happened to Mia, and they all involve one common denominator."

    "He points a finger at Rachel."

    cl "You."
    cl "Something happened and you were the only one there to see it."
    cl "I have no idea as to why you'd stay silent, unless you were guilty."
    show ra sadcos
    cl "You're probably trying to protect yourself, huh?"
    cl "You don't care who suffers so long as you stay out of bars."

    mo "How can you even say that?!"
    mo "You have no idea what losing Mia did to Rachel!"
    mo "You weren't even there, dumbass!"

    show cl eyerollcos
    cl "No, but I don't need to have been there."
    cl "I've learned that word travels quick in this town."
    cl "So I couldn't help but pick up on the fact that Rachel got held back a year."

    show ra shockedcos
    "Rachel stiffens, but Monique holds strong."

    mo "So? What's that got to do with anything?"

    show ra sadcos
    show cl defaultcos
    cl "Well, there had to have been a reason, right?"
    cl "Someone as supposedly smart as Rachel doesn't get held back a year for failing classes, no."
    cl "It had to have been for something much more sinister."
    cl "And, people do say that she vanished for the rest of her freshman year, after Mia disappeared."
    show cl sneercos
    cl "My guess, and this seems to be the common theory, is that Rachel spent some time in a mental hospital-"
    cl "-being treated for whatever illness caused her to murder her closest friend."

    show mo concerncos
    "Silence."

    mo "Orrrrr, she switched to home schooling, but failed and had to come back to public school?"
    mo "The best thing you've been saying so far has been baseless assumptions that can so easily be explained by something else."

    "Cliff throws his hands up in defense."

    show cl defaultcos
    cl "Hey, it's your choice if you wanna die on this hill."
    cl "You might end up like Mia, but hey, just another baseless assumption."

    show mo angrycos
    mo "I can't believe you said that!"
    mo "You're so gross, maybe you should spend some time in a mental hospital yourself!"

    show cl sneercos
    cl "You aren't denying it."

    mo "I didn't think I had to, you're being stupid right now!"

    "Rachel finally speaks up."

    show ra defaultcos
    ra "Moni, it's fine."
    ra "It's not like he's known for being the most logical, anyway."

    show mo gentlecos
    mo "Ugh, you're right."

    show cl cockycos
    cl "Ladies, ladies."
    cl "Please, don't argue over me."
    cl "I'm sure I can help you come to a reasonable conclusion."
    cl "One that is preferably in my best interest."

    show ra smilecos
    ra "Oh, we weren't arguing."

    show cl eyerollcos
    cl "Y-you weren't?"

    show mo concerncos
    mo "Um, no."
    mo "And especially not over you."

    cl "..."
    show cl defaultcos
    cl "Well!"
    cl "I better be off, then."
    cl "Duty calls, you know."
    cl "I can't be the greatest journalist of all time if I sit chit-chatting with my suspects."
    cl "That's not how it works at all."

    "Neither of them have the energy to correct him."

    cl "Toodles!"

    hide cl with moveoutright
    "They both watch as he skips away, his cardboard costume jostling other party-goers from how clunky it was."

    "Once he disappears into the crowd, they turn to face one another."

    hide mo with moveoutleft
    show ra smilecos at posLeft with moveinleft
    show mo gentlecos at Transform(xzoom=1.0) with moveinright:
        xpos 0.65
        ypos 0.15

    mo "So...at least that's over, right?"
    show mo angrycos
    mo "Ugh, the nerve of that guy!"
    mo "Claiming you were in a mental hospital, of all places."

    show ra smilecos
    ra "It's alright, he wasn't entirely off anyway."
    ra "Um, he was mostly wrong, though."
    show ra defaultcos
    ra "I'm just...tired, I think."
    ra "Of being here, I mean."
    ra "Everyone keeps jumping to conclusions, pointing fingers at me."
    show ra sadcos
    ra "It feels fresh all over again."

    show mo gentlecos
    mo "Hey, it's okay, you don't have to talk about it."
    mo "I understand."
    mo "Let's head out, okay?"
    return


label cliff_party_2:
    # $ preload_images([
    # "ra defaultcos", "ra frowncos", "ra sadcos", "ra shockedcos", "ra smilecos", "ra timidcos",
    # "mo angrycos", "mo concerncos", "mo defaultcos", "mo gentlecos", "mo smilecos",
    # "mi partydark", "mi partylight", "cl defaultcos", "cl cockycos", "cl eyerollcos", "cl sneercos", "ce angrycos", "ce defaultcos", "ce eyerollcos", "ce neutralcos", "ce smilecos", "ce sneercos", "ce worrycos",
    # # BGs
    # "bg partyexterior", "bg partyinterior"])
    "Say it ain't so."

    show cl defaultcos at cliffsFuckassSpecialFunction with moveinright

    cl "So, you decided to show your face around here."

    "This...cannot be."

    show ra frowncos
    "First Celine sees her here, and now Cliff?!"

    show cl cockycos
    cl "Actually, you technically didn't decide to show your face."
    cl "Pretty sure that was an accident on your behalf."
    cl "Regardless, it was dumb."
    cl "And so are you."

    show ra defaultcos
    ra "Cliff...there's no way you're actually here."
    ra "I must be imagining things."

    show cl sneercos
    cl "HA!"
    cl "Thankfully, you aren't."
    show cl defaultcos
    cl "Someone as amazing as me can't be conjured up by the feeble-minded mortal brain."
    cl "I am an enigma."

    "The vibes of this guy are so rancid, Biscuit has already scampered away to find some better party goers to jump on."

    "Already, Rachel's main solace has slipped away."

    show ra frowncos
    ra "Uhhh sure dude."
    ra "Listen, I'm already having a crappy night, so just do me a favor and ease off the gloating, okay?"

    "Cliff snorts from amusement, but the noise sounded less like a snort and more like something got stuck in the blender."

    cl "You? A favor?"
    show cl cockycos
    cl "Don't make me laugh."
    cl "Rachel, I think you've forgotten, but favors are for people who somewhat like each other."
    cl "Us?"
    show cl eyerollcos
    cl "We haven't even spoken since last year."

    if sendText == True:
        jump cliff_party_text

    cl "You know, when you dumped me."

    show ra defaultcos
    ra "Oh, you're still hung up on that?"
    ra "I thought you'd be over it by now."

    show cl cockycos
    cl "Well, yes, I am."
    cl "After all, I have many a maiden flocking towards me at all times."
    cl "But that's besides the point."
    show cl eyerollcos
    cl "You still dumped me two days before the junior prom."
    cl "Talk about shady."

    show ra frowncos
    "Rachel pinches her brow bone."

    ra "Yeah, I dumped you before prom-"
    ra "-because I found out that you were only dating me because you thought it'd get you info on the missing person's case."

    show cl cockycos
    cl "And you wouldn't do the same?"
    show cl sneercos
    cl "I mean, come ON!"
    cl "I thought you of all people would understand me."
    cl "We both have similar motives."

    show ra defaultcos
    ra "And what makes you think that?"

    cl "We both use people to get what we want."

    show ra frowncos
    ra "???"
    ra "Who is \"we\"???"
    show ra sadcos
    ra "I do not do that, that's so...gross."
    ra "Who the hell are you using?"
    show ra frowncos
    ra "And for what?"

    "Cliff places a gloved finger upon Rachel's lips, shushing her. Gross."

    show cl cockycos
    cl "Shhh, I can't reveal all my secrets, can I?"
    show cl defaultcos
    cl "Ahhh who am I kidding?"
    cl "I'll totally tell you."
    cl "It's Celine."

    show ra shockedcos
    ra "Celine?!"

    cl "Yup."
    cl "I'm trying to improve my journalism skills so that I can become head of the school paper."
    cl "What better thing to report on than a missing person's case that went cold, where your girlfriend is the main suspect?"
    show cl cockycos
    cl "Well, WAS my girlfriend."
    cl "I couldn't really get any good info since you refuse to budge, so I'm going to the next best thing."
    show cl sneercos
    cl "Who knows? Maybe I'll solve the case before the police?"
    cl "I'll have a whole article dedicated to me!"
    cl "Senior year, go out with a bang, you know?"

    show ra sadcos
    ra "Dude, that's so low."
    ra "She's already in a vulnerable position, and you're just using her for your own need for clout?!"

    show cl eyerollcos
    cl "Uhhh yeah, that's how it works."
    cl "Don't act all righteous now, we both know that charade won't do you any good."
    cl "And besides, I'm pretty sure she's using me too."
    cl "I'm probably the next best thing she can get, besides a detective."
    show cl defaultcos
    cl "Who knows? Maybe the conspiracy theorists are right and Mia WAS sacrificed to the devil."
    cl "One thing for sure is that I'll figure it out, and I'll be the one to present the info that'll lock you behind bars forever."

    ra "God, you're so gross..."

    cl "Hate the game, not the player."
    cl "Speaking of Celine, I gotta find her."
    cl "There's some intel I need to share with her."

    show ra frowncos
    ra "Ugh, she's over by the snack table."
    ra "She's in a pissy mood though, I don't recommend you go over there."

    show cl cockycos
    cl "Oh yeah?"
    cl "How come?"

    ra "We had a chat, and she isn't the happiest person in the world, knowing her nemesis is in her house, crashing her party."

    show cl defaultcos
    cl "Wait, you're serious?"
    cl "Celine SAW you?"
    cl "And you guys spoke?!"

    ra "I did say that, didn't I?"

    "Cliff lets out an enthused, giddy laugh."

    cl "Ohhh man, I gotta hear about this!"
    cl "This could be a great source of intel!"
    cl "You probably slipped up and said something incriminating, in which case I need her to tell me while it's fresh!"

    show ra shockedcos
    ra "Hey, that's-!"

    show cl sneercos
    cl "Ya snooze ya loose, Rachel!"

    "Off he goes."
    return
