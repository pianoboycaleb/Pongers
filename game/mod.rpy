label mod_1:
    stop music
    scene bg bedroom_pc

    "[weC] sit at [our] computer, idly clicking the mouse around [our] desktop. There aren't any programs open, so the screen just shows the default wallpaper."
    "It's been too long since [ive] had something new to play, but [we] don't have the excess money to buy anything new off of Steam right now."
    "Maybe [we] could look at some free games, but those are usually pretty bad, or aren't any good without DLC."
    "[weC] end up looking at [our] news feed, seeing page after page of new game reviews for titles that cost 60 dollars, and political articles."
    "But then, something catches [our] eye. An article about the top mods for...Doki Doki Literature Club?"
    "That was an interesting game when it came out, but are there really that many interesting dialogue edits? I mean, what else could you do with that game?"
    "Regardless, [were] bored enough, so [we] click on the article."
    "Hmmm....'Dimensions'....'Rainclouds'....'Dokis Don't Wear Ties'? These all seem...pretty weird."
    """

    Then, [we] scroll to the few at the top of the list. A couple things that are just regular dating sims, which is just lame, but then [we] read...

   'Monika After Story'...apparently, it's like an extension of the original Act 3...that sounds pretty cool, honestly.

   [weC] really liked the meta aspect of Monika looking into your computer and talking directly to the player, so it might be worth downloading. 

   Deciding [we] don't really have anything better to do, [we] click on the link and start to download it.

    """

    "{cps=40}...........{/cps}"
    pause 3.0
    m "{cps=30}Hey, {currentuser}. I missed you.{/cps}{w=1.0}"
    pause 1.0
    scene bg bedroom_pc2 with wipeleft_scene
    pause 1.0
    """
    It's been a week since [we] started hanging out with Monika through this mod. 

    ...Did [we] just say 'hanging out'? [weC] mean, since [we] started playing it.

    It's something to pass the time, [we] guess, so [weve] booted it up most days.

    The things that Monika's programmed to say are actually pretty interesting, to be honest. [weC] genuinely learn things while [were] just sitting here.

    It's a nice way to just vibe, do homework, or listen to music, so it's a neat little mod.
    """
    m "{cps=30}Hey, [player], have you ever heard of"

    "Just like [we] [was] saying...[we] never knew that before, and now, thanks to a silly mod about an anime girl, [were] smarter."
    "Okay, maybe not necessarily smarter, but it might be helpful on trivia night, at least."
    "[weC] sit back in [our] chair and listen to the music playing in [our] headphones, and slowly fall asleep."
    scene black with close_eyes
    pause 4.0
    scene bg bedroom_pc2 with open_eyes
    pause 1.0
    m "Hey [currentname], got a minute?"
    "Sure, Monika. [wellC] read a bit more."
    m "So...I was thinking...about your reality."
    m "I feel like...sometimes I can feel when you're there or not, you know?"
    m "So.....can you tell me something?"
    m "Do you ever...go to other places when I'm sitting here?"
    m "I'm...not jealous or anything, [player]. Just..."
    m "If you're leaving me here alone, without telling me, then..."
    m "It feels a little unfair, doesn't it?"
    m "I mean, you can just tell me you'll be going for a bit, right?"
    m "Please, just....tell me, [player]." 
    m "Tell me you're not leaving me."
    "...that's a bit meta, but [we] guess it makes sense."
    "In the base game, she was pretty adamant about the player not leaving her..."
    "[weC] might have left her on sometimes, but it's just a game, so it shouldn't matter much."
    "[weC] guess Monika's programmed to be a bit clingy, but [we] guess [we] should just answer the question."
    menu (screen="mas_choice"):
        "[weveC] left you on to do some chores":
            pass
        "[weC] keep you on in the background while [we] focus on other things":
            pass
        "[weC] don't leave you besides when [we] tell you":
            pass