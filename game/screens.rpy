## screens.rpy

# This file declares all the screens and styles in DDLC.

## Initialization
################################################################################

init offset = -1

# Thanks RenpyTom! Borrowed from the Ren'Py Launcher
init python:
    # Ren'Py 6 doesn't have translate_string defined by default so
    # import it and set for Ren'Py 7 code workings.
    from renpy.translation import translate_string
    renpy.translate_string = translate_string

    def scan_translations():

        languages = renpy.known_languages()

        if not languages:
            return None

        rv = [(i, renpy.translate_string("{#language name and font}", i)) for i in languages ]
        
        # We will use a imported Ren'Py 7 function for Ren'Py 6
        if renpy.version_tuple == (6, 99, 12, 4, 2187):
            rv.sort(key=lambda a : filter_text_tags(a[1], allow=[]).lower())
        else:
            rv.sort(key=lambda a : renpy.filter_text_tags(a[1], allow=[]).lower())

        rv.insert(0, (None, "English"))

        # Cause Ren'Py 6 sets this as float, set it as int
        bound = int(math.ceil(len(rv)/2.))

        return (rv[:bound], rv[bound:2*bound])

default translations = scan_translations()

# Enables the ability to add more settings in the game such as uncensored mode.
default extra_settings = True
default enable_languages = True
default enable_extras_menu = True

## Color Styles
################################################################################

# This controls the color of outlines in the game like
# text, say, navigation, labels and such.
define -2 text_outline_color = "#83b8c7"

## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style splash_text:
    size 24
    color "#b3d7df"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style slider:
    ysize 18
    base_bar Frame("mod_assets/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style goofyslider:
    ysize 20
    base_bar Frame("mod_assets/skull.png", tile=False)
    thumb "mod_assets/pen.png"

style goofyslider2:
    ysize 10
    base_bar Frame("gui/slider/horizontal_hover_thumb.png", tile=False)
    thumb "mod_assets/horizontal_poem_bar.png"

style goofyslider3:
    ysize 30
    base_bar Frame("mod_assets/shrekdick.png", tile=False)
    thumb "mod_assets/ass.png"

style goofyslider4:
    ysize 18
    base_bar Frame("mod_assets/silver textbox.png", tile=False)
    thumb "mod_assets/silver namebox.png"

style goofyslider5:
    ysize 28
    base_bar Frame("mod_assets/hot.png", tile=False)
    thumb "mod_assets/nerd.png"

style goofyslider6:
    ysize 36
    base_bar Frame("mod_assets/cs1.png", tile=False)
    thumb "mod_assets/circle.png"


style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style goofyvslider:
    xsize 201
    base_bar Frame("mod_assets/pen", gui.vslider_borders, tile=gui.slider_tile)
    thumb "mod_assets/skull"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("mod_assets/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("mod_assets/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    #outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    recolorize ("gui/ctc.png", "#ffb6f0", "#b3d7df", 1)
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#1b3872")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## New as of 3.0.0
##    - You may now pass through argurments to the menu options to colorize
##      your menu as you like. Add (kwargs=[color hex or style name]) to your
##      menu option name and you get different buttons! 
##
##      Examples: "Option 1 (kwargs=#00fbff)" | "Option 2 (kwargs=#00fbff, #6cffff)"
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.0
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text




style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.


init python:
    def FinishEnterName1(launchGame=True):
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input_1")
        if launchGame:
            renpy.show_screen("name_input_2", message="Please enter Monika's nickname", ok_action=Function(FinishEnterName2))

    def FinishEnterName2(launchGame=True):
        if not mname: return
        persistent.monikaname = mname
        renpy.save_persistent()
        renpy.hide_screen("name_input_2")
        if launchGame:
            renpy.show_screen("pronoun_input_1", message="Enter your first pronoun (he/she/they)", ok_action=Function(FinishPronoun1))

    def FinishPronoun1(launchGame=True):
        if not he: return
        persistent.he = he
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_1")
        if launchGame:
            renpy.show_screen("pronoun_input_2", message="Enter your second pronoun (him/her/their)", ok_action=Function(FinishPronoun2))
        else:
            renpy.show_screen("pronoun_input_2", message="Enter your second pronoun (him/her/their)", ok_action=Function(FinishPronoun2, launchGame=False))

    def FinishPronoun2(launchGame=True):
        if not him: return
        persistent.him = him
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_2")
        if launchGame:
            renpy.show_screen("pronoun_input_3", message="Enter your third pronoun (he's/she's/they're)", ok_action=Function(FinishPronoun3))
        else:
            renpy.show_screen("pronoun_input_3", message="Enter your third pronoun (he's/she's/they're)", ok_action=Function(FinishPronoun3, launchGame=False))

    
    def FinishPronoun3(launchGame=True):
        if not hes: return
        persistent.hes = hes
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_3")
        if launchGame:
            renpy.show_screen("pronoun_input_4", message="Enter your fourth pronoun (I/we)", ok_action=Function(FinishPronoun4))
        else:
            renpy.show_screen("pronoun_input_4", message="Enter your fourth pronoun (I/we)", ok_action=Function(FinishPronoun4, launchGame=False))

    def FinishPronoun4(launchGame=True):
        if not we: return
        persistent.we = we
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_4")
        if launchGame:
            renpy.jump_out_of_context("start")

    def FinishEnterName1Goofy(launchGame=True):
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input_1")
        if launchGame:
            renpy.show_screen("name_input_2", message="whos your girlfriend", ok_action=Function(FinishEnterName2Goofy))

    def FinishEnterName2Goofy(launchGame=True):
        if not mname: return
        persistent.monikaname = mname
        renpy.save_persistent()
        renpy.hide_screen("name_input_2")
        if launchGame:
            renpy.show_screen("pronoun_input_1", "message=are you he or she or they or", ok_action=Function(FinishPronoun1Goofy))

    def FinishPronoun1Goofy(launchGame=True):
        if not he: return
        persistent.he = he
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_1")
        if launchGame:
            renpy.show_screen("pronoun_input_2", message="okay next on its him her their or whichever", ok_action=Function(FinishPronoun2Goofy))
        else:
            renpy.show_screen("pronoun_input_2", message="okay next on its him her their or whichever", ok_action=Function(FinishPronoun2Goofy, launchGame=False))

    def FinishPronoun2Goofy(launchGame=True):
        if not him: return
        persistent.him = him
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_2")
        if launchGame:
            renpy.show_screen("pronoun_input_3", message="sorry for all the questions um this one is if someone says your doing something so he's she's or they're or whatever", ok_action=Function(FinishPronoun3Goofy))
        else:
            renpy.show_screen("pronoun_input_3", message="sorry for all the questions um this one is if someone says your doing something so he's she's or they're or whatever", ok_action=Function(FinishPronoun3Goofy, launchGame=False))

    
    def FinishPronoun3Goofy(launchGame=True):
        if not hes: return
        persistent.hes = hes
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_3")
        if launchGame:
            renpy.show_screen("pronoun_input_4", message="okay last one do you call yourself i or we", ok_action=Function(FinishPronoun4Goofy))
        else:
            renpy.show_screen("pronoun_input_4", message="okay last one do you call yourself i or we", ok_action=Function(FinishPronoun4Goofy, launchGame=False))

    def FinishPronoun4Goofy(launchGame=True):
        if not we: return
        persistent.we = we
        renpy.save_persistent()
        renpy.hide_screen("pronoun_input_4")
        if launchGame:
            renpy.jump_out_of_context("start")

init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)


            # The sizes of some of the images.
            self.PADDLE_WIDTH = 14
            self.PADDLE_HEIGHT = 110
            self.PADDLE_X = 60
            self.BALL_WIDTH = 20
            self.BALL_HEIGHT = 20
            self.COURT_TOP = 0
            self.COURT_BOTTOM = 720


            # Some displayables we use.
            self.paddle = Solid("#b3d7df", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#83b8c7", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 400.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 550.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy


            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy


            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                        int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner == "eileen":
                renpy.quit()
            elif self.winner == "player":
                renpy.restart_interaction()
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add pong at pongfade

screen navigation():

    if persistent.goofygoober_mode:
        hbox:
            style_prefix "goober"
  
            xalign 0.7
            yalign 0.6

            spacing 10

            if not persistent.autoload or not main_menu:

                if main_menu:

                    textbutton _("goof off") action If(persistent.playername and persistent.monikaname, true=Start(), false=Show(screen="name_input_1", message="Please enter your name", ok_action=Function(FinishEnterName1)))
                else:

                    textbutton _("evidence") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                    textbutton _("wrap in tinfoil") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

                textbutton _("reheat leftovers") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

                textbutton _("go away") action MainMenu()

                if enable_extras_menu:
                    textbutton _("bonus stage") action [ShowMenu("extras"), SensitiveIf(renpy.get_screen("extras") == None)]


                textbutton _("fancy buttons") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

                if not enable_extras_menu:
                    textbutton _("who did it") action ShowMenu("about")

                if main_menu:
                    textbutton _("bye losers") action Quit(confirm=False)

    else:
        vbox:
            style_prefix "navigation"
  
            xpos gui.navigation_xpos
            yalign 0.8

            spacing gui.navigation_spacing

            if not persistent.autoload or not main_menu:

                if main_menu:

                    textbutton _("New Game") action If(persistent.playername and persistent.monikaname, true=Start(), false=Show(screen="name_input_1", message="Please enter your name", ok_action=Function(FinishEnterName1)))
                else:

                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                    textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

                textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

                if enable_extras_menu:
                    textbutton _("Extras") action [ShowMenu("extras"), SensitiveIf(renpy.get_screen("extras") == None)]

                elif not main_menu:
                    textbutton _("Main Menu") action MainMenu()

                textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

                if not enable_extras_menu:
                    textbutton _("Credits") action ShowMenu("about")

                if main_menu:
                    textbutton _("Quit") action Quit(confirm=False)

screen navigation2():

    hbox:
        style_prefix "goober"

        xalign 0.7
        yalign 0.6

        spacing 10

        if not persistent.autoload or not main_menu:

            if main_menu:
                null width 100
                vbox:
                    null height 60
                    textbutton _("goof off") action If(persistent.playername and persistent.monikaname, true=Start(), false=Show(screen="name_input_1", message="Please enter your name", ok_action=Function(FinishEnterName1)))
            else:

                textbutton _("evidence") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                vbox:
                    null height 100
                    textbutton _("wrap in tinfoil") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            vbox:
                null height 200
                textbutton _("reheat leftovers") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            vbox:
                null height 300
                textbutton _("go away") action MainMenu()

            if enable_extras_menu:
                vbox:
                    null height 400
                    textbutton _("bonus stage") action [ShowMenu("extras"), SensitiveIf(renpy.get_screen("extras") == None)]


            vbox:
                null height 500
                textbutton _("fancy buttons") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            if not enable_extras_menu:
                textbutton _("who did it") action ShowMenu("about")

            if main_menu:
                vbox:
                    null height 600
                    textbutton _("bye losers") action Quit(confirm=False)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/CamingoCode-Bold.ttf"
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"
    idle_color "#ffffff"
    #outlines [(0, text_outline_color, 0, 0), (0, text_outline_color, 0, 0)]
    outlines [(2, "#3bc4ff", 0, 0), (2, "#3bc4ff", 2, 2)]
    hover_outlines [(2, "#009cdf", 0, 0), (2, "#009cdf", 2, 2)]
    insensitive_outlines [(2, "#0077a6", 0, 0), (2, "#0077a6", 2, 2)]


style goober_button:
    properties gui.button_properties("navigation_button")
    background "mod_assets/nerd.png"
    hover_sound "mod_assets/goofyhover1.ogg"
    activate_sound "mod_assets/goofyhover2.ogg"

style goober_button_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/primer print bold.otf"
    color "#a73b3b"
    hover_color "#2d5257"
    selected_color "#7aa034"
    idle_color "#ca8434"
    outlines [(4, "#43167e", 2, 3), (6, "#1493c9", 3, 9)]
    hover_outlines [(5, "#743891", 8, 2), (2, "#359728", 0, 10)]
    insensitive_outlines [(12, "#e94d6f", 1, 2), (3, "#2bbd9d", 9, 0)]


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    if persistent.goofygoober_mode:

        add "menu_goofybg"
        add "menu_goofylogo"
        add "menu_sayo"
        add "menu_fog1"
        add "menu_fog2"

        use navigation2

    else:

        add "menu_monika"
        add "menu_logo"

        use pong

        ## The use statement includes another screen inside this one. The actual
        ## contents of the main menu are in the navigation screen.
        use navigation

        add "menu_fade"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#b3d7df"
    size 18
    outlines []

style main_menu_frame:
    xsize 310
    yfill True


style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    color "#b3d7df"
    size gui.title_text_size


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):

    # Add the backgrounds.
    if persistent.goofygoober_mode:
        if main_menu:
            add "game_menu_bggoofy"
        else:
            key "mouseup_3" action Return()
            add "game_menu_bggoofy"
    else:
        if main_menu:
            add "game_menu_bg"
        else:
            key "mouseup_3" action Return()
            add "game_menu_bg"

    if persistent.goofygoober_mode:
        style_prefix "goofygame_menu"
    else:
        style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")
    if persistent.goofygoober_mode:
        textbutton _("get out of here"):
            style "goofyreturn_button"
            action Return()
    else:
        textbutton _("Return"):
            style "return_button"
            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "mod_assets/CamingoCode-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    #outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos 80
    yalign 1.0
    yoffset -30



style goofygame_menu_outer_frame is empty
style goofygame_menu_navigation_frame is empty
style goofygame_menu_content_frame is empty
style goofygame_menu_viewport is gui_viewport
style goofygame_menu_side is gui_side
style goofygame_menu_scrollbar is gui_vscrollbar

style goofygame_menu_label is gui_label
style goofygame_menu_label_text is gui_label_text

style goofyreturn_button is goober_button
style goofyreturn_button_text is goober_button_text

style goofygame_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    #background "gui/overlay/game_menu.png"

style goofygame_menu_navigation_frame:
    xsize 280
    yfill True

style goofygame_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style goofygame_menu_viewport:
    xsize 920

style goofygame_menu_vscrollbar:
    unscrollable gui.unscrollable

style goofygame_menu_side:
    spacing 10

style goofygame_menu_label:
    xpos 50
    ysize 120

style goofygame_menu_label_text:
    font "mod_assets/orb.otf"
    size gui.title_text_size
    color "#e05a5a"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    #outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.9

style goofyreturn_button:
    xpos 483
    yalign 0.4
    yoffset 27


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        window:
            xoffset 35
            has fixed:
                yfit True

            vbox:
                label "[config.name!t]" xalign .5
                text _("Version [config.version!t]\n") xalign .5

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                ## Do not touch/remove these unless the © or – symbol isn't available in your font.
                ## You may add things above or below it.
                ## If you are not going with a splashscreen option, this first line MUST stay in the mod.
                text "Made with GanstaKingofSA's {a=https://github.com/GanstaKingofSA/DDLCModTemplate2.0}DDLC Mod Template 2.0{/a}.\nCopyright © 2019-" + str(datetime.date.today().year) + " Azariel Del Carmen (GanstaKingofSA). All rights reserved.\n"
                text "Doki Doki Literature Club. Copyright © 2017 Team Salvato. All rights reserved.\n"
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""

style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#000"
    outlines []
    text_align 0.5
    size gui.label_text_size

style about_text:
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color gui.idle_color
    hover_color gui.hover_color
    hover_underline True

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

                #textbutton _("{#auto_page}A") action FilePage("auto")

                #textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#af00b8"
    outlines []

screen viewframe_options(title):

    style_prefix "viewframe"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 2

            label title

            null height 10

            transclude

style viewframe_frame is confirm_frame
style viewframe_label is confirm_prompt:
    xalign 0.5
style viewframe_label_text is confirm_prompt_text
style viewframe_button is confirm_button
style viewframe_button_text is confirm_button_text
style viewframe_text is confirm_prompt_text:
    size 20
    yalign 0.7

# Windowed Resolutions
# Windowed Resolutions allow players to scale the game to different resolutions.
# Uncomment the below #'s to enable this.
screen confirm_res(old_res):
    
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 150

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            ## This if-else statement either shows a normal textbox or
            ## glitched textbox if you are in Sayori's Death Scene and are
            ## quitting the game.
            # if in_sayori_kill and message == layout.QUIT:
            #     add "confirm_glitch" xalign 0.5
            # else:
            label _("Would you like to keep these changes?"):
                style "confirm_prompt"
                xalign 0.5

            add DynamicDisplayable(res_text_timer) xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action Hide()
                textbutton _("No") action [Function(renpy.set_physical_size, old_res), Hide()]
    
    timer 5.0 action [Function(renpy.set_physical_size, old_res), Hide()]

init python:
    def res_text_timer(st, at):
        if st <= 5.0:
            time_left = str(round(5.0 - st))
            return Text(time_left, style="confirm_prompt_text"), 0.1
        else: return Text("0", style="confirm_prompt_text"), 0.0

    def set_physical_resolution(res):
        old_res = renpy.get_physical_size()
        renpy.set_physical_size(res)
        renpy.show_screen("confirm_res", old_res=old_res)

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    if persistent.goofygoober_mode:
        use game_menu(_("changey thingys")):

            viewport id "vp":
                draggable True
                mousewheel "horizontal-change"

                vbox:
                    xoffset 70

                    hbox:

                        if renpy.variant("pc"):

                        
                            vbox:
                                style_prefix "goofyradio"
                                label _("whats it look like")
                                textbutton _("move around") action Preference("display", "window")
                                textbutton _("only me") action Preference("display", "fullscreen")


                        vbox:
                            null height 60  
                            style_prefix "goofyconfirm"
                            label _("borringg")
                            textbutton _("i dont want to see this") action Preference("skip", "toggle")
                            textbutton _("speed run") action Preference("after choices", "toggle")

                        vbox:
                            style_prefix "goofycheck"
                            label _("bonus features")
                            textbutton _("dont turn me off pls") action Show("confirm", message="this is gonna start over the game and turn off this thing are u sure", 
                                    yes_action=[Hide("confirm"), ToggleField(persistent, "goofygoober_mode"), Start("goofygoober")],
                                    no_action=Hide("confirm")
                                )
                        hbox:
                            textbutton _("dont even bother") action If(persistent.hardmode, 
                                ToggleField(persistent, "hardmode"), 
                                Show("confirm", message="don't even", 
                                    yes_action=[Hide("confirm"), ToggleField(persistent, "hardmode")],
                                    no_action=Hide("confirm")
                                ))

                        ## Additional vboxes of type "radio_pref" or "check_pref" can be
                        ## added here, to add additional creator-defined preferences.

                    null height (2 * gui.pref_spacing)

                    hbox:
                        style_prefix "goofyslider"
                        box_wrap False

                        vbox:

                            label _("how fast can u read")

                            #bar value Preference("text speed")
                            bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
                            vbox:
                                style_prefix "goofyslider3"
                                label _("clicking is hard")

                                bar value Preference("auto-forward time")

                        vbox:
                            hbox:
                                vbox:
                                    style_prefix "goofyslider2"
                                    if config.has_music:
                                        label _("crank tunes")

                                        hbox:
                                            bar value Preference("music volume")
                                vbox:
                                    style_prefix "goofycheck"
                                    if config.has_sound:

                                        label _("bangs and stuff")

                                        hbox:
                                            bar value Preference("sound volume")

                                            if config.sample_sound:
                                                textbutton _("Test") action Play("sound", config.sample_sound)

                                vbox:
                                    style_prefix "goofyradio"
                                    if config.has_voice:
                                        label _("are you a goofy goober")

                                        hbox:
                                            bar value Preference("voice volume")

                                            if config.sample_voice:
                                                textbutton _("Test") action Play("voice", config.sample_voice)
                                    
                                vbox:
                                    style_prefix "goofyconfirm"
                                    if config.has_music or config.has_sound or config.has_voice:
                                        null height gui.pref_spacing

                                        textbutton _("I HATE EARS"):
                                            action Preference("all mute", "toggle")
                                            style "goofypref_label_text"
                    null height 20

                    hbox:
                        style_prefix "goofyradio"

                        hbox:
                            label _("who am i")
                            style_prefix "goofyradio"
                            if player == "":
                                text "i am nobody" style "goofyradio_text"
                            else:
                                text "i am [player]" style "goofyconfirm_text"
                            textbutton "i dont like my name" action Show(screen="name_input_1", message="whats my name", ok_action=Function(FinishEnterName1Goofy, launchGame=False)) xoffset -5

                        spacing 50
                        vbox:
                            vbox:
                                label _("girlfriend")
                                style_prefix "goofyconfirm"
                                null height 10
                                if mname == "":
                                    text "no bitches" style "goofyconfirm_text"
                                else:
                                    text "shes [mname]" style "goofyradio_text"
                                null height 5
                                textbutton "new girlfriend" action Show(screen="name_input_2", message="whos it gonna be", ok_action=Function(FinishEnterName2Goofy, launchGame=False)) xoffset -5

                            vbox:
                                label _("trans rights")
                                style_prefix "goofyslider"
                                null height 10
                                vbox:
                                    if are == "":
                                        text "i dont know what to call you" style "goofyradio_label_text"
                                    else:
                                        text "ill call you [he]/[him]/[hes]/[we]" style "goofyslider2_label_text"
                                    textbutton "call you something else" action Show(screen="pronoun_input_1", message="are you he or she or they or", ok_action=Function(FinishPronoun1Goofy, launchGame=False)) xoffset -5


    else:

        use game_menu(_("Settings"), scroll="viewport"):
            vbox:
                xoffset 10

                hbox:

                    if renpy.variant("pc"):

                    
                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Windowed") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")


                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")

                    vbox:
                        style_prefix "check"
                        label _("Extra Settings")
                        textbutton _("Goofy Goober") action If(persistent.goofygoober_mode, 
                            ToggleField(persistent, "goofygoober_mode"), 
                            Show("confirm", message="Are you sure you want to turn on Goofy Goober Mode?\nDoing so will make you a goofy goober.", 
                                yes_action=[Hide("confirm"), ToggleField(persistent, "goofygoober_mode"), Start("goofygoober")],
                                no_action=Hide("confirm")
                            ))
                        textbutton _("Hard Mode") action If(persistent.hardmode, 
                            ToggleField(persistent, "hardmode"), 
                            Show("confirm", message="Are you sure you want to turn on Hard Mode?\nThis will make the mod more challenging to complete.", 
                                yes_action=[Hide("confirm"), ToggleField(persistent, "hardmode")],
                                no_action=Hide("confirm")
                            ))

                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                null height (2 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:

                        label _("Text Speed")

                        #bar value Preference("text speed")
                        bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                        label _("Auto-Forward Time")

                        bar value Preference("auto-forward time")

                    vbox:
                        
                        if config.has_music:
                            label _("Music Volume")

                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:

                            label _("Sound Volume")

                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)


                        if config.has_voice:
                            label _("Voice Volume")

                            hbox:
                                bar value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
                null height 20

                hbox:
                    style_prefix "radio"

                    vbox:
                        label _("Player Name")
                        style_prefix "confirm"
                        null height 10
                        if player == "":
                            text "Current Name: No Name Set" style "viewframe_text"
                        else:
                            text "Current Name: [player]" style "viewframe_text"
                        null height 5
                        textbutton "Change Name" action Show(screen="name_input_1", message="Please enter your name", ok_action=Function(FinishEnterName1, launchGame=False)) xoffset -5

                    spacing 50

                    vbox:
                        label _("Monika's Name")
                        style_prefix "confirm"
                        null height 10
                        if mname == "":
                            text "Current Name: No Name Set" style "viewframe_text"
                        else:
                            text "Current Name: [mname]" style "viewframe_text"
                        null height 5
                        textbutton "Change Name" action Show(screen="name_input_2", message="Please enter Monika's nickname", ok_action=Function(FinishEnterName2, launchGame=False)) xoffset -5

                    vbox:
                        label _("Pronouns")
                        style_prefix "confirm"
                        null height 10
                        if are == "":
                            text "Current Pronouns: None Set" style "viewframe_text"
                        else:
                            text "Pronouns: [he]/[him]/[hes]/[we]" style "viewframe_text"
                        null height 5
                        textbutton "Change Pronouns" action Show(screen="pronoun_input_1", message="Enter your first pronoun (he/she/they)", ok_action=Function(FinishPronoun1, launchGame=False)) xoffset -5



style goofypref_label is gui_label
style goofypref_label_text is gui_label_text
style goofypref_vbox is vbox

style goofyradio_label is goofypref_label
style goofyradio_label_text is goofypref_label_text
style goofyradio_button is gui_button
style goofyradio_button_text is gui_button_text
style goofyradio_vbox is goofypref_vbox

style goofycheck_label is goofypref_label
style goofycheck_label_text is goofypref_label_text
style goofycheck_button is gui_button
style goofycheck_button_text is gui_button_text
style goofycheck_vbox is goofypref_vbox

style goofyslider_label is goofypref_label
style goofyslider_label_text is goofypref_label_text
style goofyslider_slider is goofyslider
style goofyslider2_slider is goofyslider2
style goofyslider3_slider is goofyslider3
style goofyslider_button is gui_button
style goofyslider_button_text is gui_button_text
style goofyslider_pref_vbox is goofypref_vbox
style goofyradio_slider is goofyslider4
style goofyconfirm_slider is goofyslider5
style goofycheck_slider is goofyslider6

style goofymute_all_button is goofycheck_button
style goofymute_all_button_text is goofycheck_button_text

style goofypref_label:
    top_margin gui.pref_spacing
    bottom_margin 8

style goofypref_label_text:
    font "mod_assets/primer print bold.otf"
    size 38
    color "#fff"
    outlines [(13, "#ea00c3", 0, 10), (7, "#a4ea00", 2, 0)]
    yalign 0.6

style goofypref_vbox:
    xsize 140

style goofyradio_vbox:
    spacing 58

style goofyradio_label_text:
    size 48
    font "mod_assets/pixel.otf"
    outlines [(2, "#26a", 9, 1), (4, "#26a", 11, 0)]

style goofyradio_text:
    size 8
    font "mod_assets/pixel.otf"
    outlines [(2, "#b5b67f", 9, 1), (4, "#b07fd1", 11, 0)]

style goofyradio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style goofyradio_button_text:
    properties gui.button_text_properties("radio_button")
    font "mod_assets/pixel.otf"
    outlines [(6, "#2ab", 3, 0), (6, "#52a7", 12, 0)]

style goofycheck_vbox:
    spacing gui.pref_button_spacing

style goofycheck_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style goofycheck_button_text:
    properties gui.button_text_properties("check_button")
    font "mod_assets/scb.ttf"
    outlines [(3, "#37a3af", 8, 18), (8, "#52ba", 3, 2)]

style goofycheck_slider:
    xsize 380

style goofyslider_slider:
    xsize 219

style goofyslider_label_text:
    font "mod_assets/orb.otf"
    size 12
    color "#6ab"
    outlines [(2, "#877263", 35, 100), (37, "#62ff", 0, 0)]
    yalign 0.1

style goofyslider_button:
    properties gui.button_properties("slider_button")
    yalign 0.2
    left_margin 32

style goofyslider_button_text:
    properties gui.button_text_properties("slider_button")

style goofyslider_vbox:
    xsize 270

style goofyslider2_slider:
    xsize 219

style goofyslider2_label_text:
    font "mod_assets/scb.ttf"
    size 20
    color "#006b29"
    outlines [(6, "#ffa4b1", 0, 9), (11, "#22ff98ff", 0, 20)]
    yalign 0.8

style goofyslider2_button:
    properties gui.button_properties("slider_button")
    yalign 0.2
    left_margin 32

style goofyslider2_button_text:
    properties gui.button_text_properties("slider_button")

style goofyslider2_vbox:
    xsize 400


style goofyslider3_slider:
    xsize 402

style goofyslider3_label_text:
    font "mod_assets/primer print bold.otf"
    size 20
    color "#000000"
    outlines [(6, "#a2cf00", 9, 9), (11, "#22a7ffff", 0, 10)]
    yalign 0.8

style goofyslider3_button:
    properties gui.button_properties("slider_button")
    yalign 0.7
    left_margin 32

style goofyslider3_button_text:
    properties gui.button_text_properties("slider_button")

style goofyslider3_vbox:
    xsize 200





style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "mod_assets/CamingoCode-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#00a4ea", 0, 0), (1, "#00a4ea", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 0

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False
    if persistent.goofygoober_mode:
        use game_menu(_("what did they say"), scroll=("vpgrid" if gui.history_height else "viewport")):
            style_prefix "goofyhistory"
            for h in _history_list:
                window:
                    has fixed:
                        yfit True
                    if h.who:
                        label h.who:
                            style "goofyhistory_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    $ what = filter_text_tags(h.what, allow=set([]))
                    text what:
                        substitute False
            if not _history_list:
                label _("they didnt say anything yet")
    else:
        use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):
            style_prefix "history"
            for h in _history_list:
                window:
                    has fixed:
                        yfit True
                    if h.who:
                        label h.who:
                            style "history_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    $ what = filter_text_tags(h.what, allow=set([]))
                    text what:
                        substitute False
            if not _history_list:
                label _("The dialogue history is empty.")

python early:
    import renpy.text.textsupport as textsupport
    from renpy.text.textsupport import TAG, PARAGRAPH
    
    def filter_text_tags(s, allow=None, deny=None):
        if (allow is None) and (deny is None):
            raise Exception("Only one of the allow and deny keyword arguments should be given to filter_text_tags.")

        if (allow is not None) and (deny is not None):
            raise Exception("Only one of the allow and deny keyword arguments should be given to filter_text_tags.")

        tokens = textsupport.tokenize(unicode(s))

        rv = [ ]

        for tokentype, text in tokens:

            if tokentype == PARAGRAPH:
                rv.append("\n")
            elif tokentype == TAG:
                kind = text.partition("=")[0]

                if kind and (kind[0] == "/"):
                    kind = kind[1:]

                if allow is not None:
                    if kind in allow:
                        rv.append("{" + text + "}")
                else:
                    if kind not in deny:
                        rv.append("{" + text + "}")
            else:
                rv.append(text.replace("{", "{{"))

        return "".join(rv)

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



style goofyhistory_window is empty

style goofyhistory_name is gui_label
style goofyhistory_name_text is gui_label_text
style goofyhistory_text is gui_text

style goofyhistory_text is gui_text

style goofyhistory_label is gui_label
style goofyhistory_label_text is gui_label_text

style goofyhistory_window:
    xfill True
    ysize 30

style goofyhistory_name:
    xpos 40
    xanchor 0.8
    ypos 5
    xsize 100

style goofyhistory_name_text:
    min_width 50
    text_align 0.1

style goofyhistory_text:
    xpos 300
    ypos 3
    xanchor 0.1
    xsize 800
    min_width 100
    text_align 0.6
    layout ("subtitle" if gui.history_text_xalign else "tex")

style goofyhistory_label:
    xfill True

style goofyhistory_label_text:
    xalign 0.8

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Help"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
#
#            if device == "keyboard":
#                use keyboard_help
#            elif device == "mouse":
#                use mouse_help
#            elif device == "gamepad":
#                use gamepad_help
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Space")
#        text _("Advances dialogue without selecting choices.")
#
#    hbox:
#        label _("Arrow Keys")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Escape")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Skips dialogue while held down.")
#
#    hbox:
#        label _("Tab")
#        text _("Toggles dialogue skipping.")
#
#    hbox:
#        label _("Page Up")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Page Down")
#        text _("Rolls forward to later dialogue.")
#
#    hbox:
#        label "H"
#        text _("Hides the user interface.")
#
#    hbox:
#        label "S"
#        text _("Takes a screenshot.")
#
#    hbox:
#        label "V"
#        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Left Click")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Middle Click")
#        text _("Hides the user interface.")
#
#    hbox:
#        label _("Right Click")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Mouse Wheel Up\nClick Rollback Side")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Mouse Wheel Down")
#        text _("Rolls forward to later dialogue.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Right Trigger\nA/Bottom Button")
#        text _("Advance dialogue and activates the interface.")
#
#    hbox:
#        label ("Left Trigger\nLeft Shoulder")
#        text _("Roll back to earlier dialogue.")
#
#    hbox:
#        label _("Right Shoulder")
#        text _("Roll forward to later dialogue.")
#
#    hbox:
#        label _("D-Pad, Sticks")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Start, Guide")
#        text _("Access the game menu.")
#
#    hbox:
#        label _("Y/Top Button")
#        text _("Hides the user interface.")
#
#    textbutton _("Calibrate") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Additional screens
################################################################################

screen name_input_1(message, ok_action):


    modal True

    zorder 200
    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen name_input_2(message, ok_action):


    modal True
    zorder 200

    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("mname") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action


screen pronoun_input_1 (message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
                style "confirm_prompt"
                xalign 0.5
            

        input default "" value VariableInputValue("he") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action


screen pronoun_input_2 (message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
                style "confirm_prompt"
                xalign 0.5
            

        input default "" value VariableInputValue("him") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen pronoun_input_3 (message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
                style "confirm_prompt"
                xalign 0.5
            

        input default "" value VariableInputValue("hes") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen pronoun_input_4 (message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    if persistent.goofygoober_mode:
        style_prefix "goofyconfirm"

        add "mod_assets/goofyconfirm.png"
        key "K_RETURN" action [Play("sound", "mod_assets/goofyhover2.ogg"), ok_action
        ]

    else:
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action
        ]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
                style "confirm_prompt"
                xalign 0.5
            

        input default "" value VariableInputValue("we") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



    

screen dialog(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm
screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            ## This if-else statement either shows a normal textbox or
            ## glitched textbox if you are in Sayori's Death Scene and are
            ## quitting the game.
            # if in_sayori_kill and message == layout.QUIT:
            #     add "confirm_glitch" xalign 0.5
            # else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                ## This if-else statement disables quitting from the quit box
                ## if you are in Sayori's Death Scene, else normal box.
                # if in_sayori_kill and message == layout.QUIT:
                #     textbutton _("Yes") action NullAction()
                #     textbutton _("No") action Hide("confirm")
                # else:
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#ffffff"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")

style goofyconfirm_frame is gui_frame
style goofyconfirm_prompt is gui_prompt
style goofyconfirm_prompt_text is gui_prompt_text
style goofyconfirm_button is gui_medium_button
style goofyconfirm_button_text is gui_medium_button_text

style goofyconfirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style goofyconfirm_label_text:
    font "mod_assets/pixel.otf"
    size 33

style goofyconfirm_prompt_text:
    color "#307e30"
    size 9
    font "mod_assets/orb.otf"
    outlines []
    text_align 0.8
    layout "subtitle"

style goofyconfirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound "mod_assets/goofyhover1.ogg"
    activate_sound "mod_assets/goofyhover2.ogg"

style goofyconfirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    font "mod_assets/scb.ttf"
    size 43


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label renpy.translate_string(_("{#in language font}Please select a language"), local_lang):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign .5
                for tran in translations:
                    vbox:
                        for tlid, tlname in tran:
                            textbutton tlname:
                                xalign .5
                                action SetScreenVariable("chosen_lang", tlid)
                                hovered SetScreenVariable("local_lang", tlid)
                                unhovered SetScreenVariable("local_lang", chosen_lang)

            $ lang_name = renpy.translate_string("{#language name and font}", local_lang)
            
            hbox:
                xalign 0.5
                spacing 100

                textbutton renpy.translate_string(_("{#in language font}Select"), local_lang):
                    style "confirm_button"
                    action [Language(chosen_lang), Return()]

translate None strings:
    old "{#language name and font}"
    new "English"

label choose_language:
    call screen choose_language
    return
