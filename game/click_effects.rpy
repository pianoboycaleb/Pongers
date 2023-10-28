init python in click_effects:
    from renpy import store
    from store import At, Transform, Fixed, Null, SpriteManager, config
    import pygame_sdl2 as pygame

    if renpy.version_tuple < (7, 5):
        raise Exception("this tool can only be used on renpy 7.5.0/8.0.0+")
    
    config.always_shown_screens.append("click_effects")

    class ClickEffects(SpriteManager, renpy.python.NoRollback):
        """
        Shows stuff when clicking.

        `clicked_d`: renpy.Displayable | callable | None
            If not None, a displayable of a function called with no argument each time a displayable is needed.
            It is shown where the mouse cursor is upon clicking.
        
        `clicked_uptime`: int | float
            A number of seconds giving how long the displayable should be on the screen.
        
        `clicked_fixed`: bool
            If true, the displayable will be wrapped in a `Fixed`. This is needed for displayables who aren't "Containers"
            (displayables who render multiple displayables).
        
        The `moved_d`, `moved_uptime` and `moved_fixed` parameters are the same, but when the mouse is being dragged.
        """
        def __init__(self,
                clicked_d=None, clicked_uptime=0.0, clicked_fixed=False,
                moved_d=None,   moved_uptime=0.0,   moved_fixed=False
            ):
            super(ClickEffects, self).__init__(event=self._event_function, update=self._update_function, predict=self._predict_function)

            self.clicked_d = (renpy.easy.displayable_or_none(clicked_d) or Null()) if not (callable(clicked_d) and not isinstance(clicked_d, renpy.display.core.Displayable)) else clicked_d
            self.clicked_fixed = clicked_fixed
            self.clicked_uptime = float(clicked_uptime)

            self._clicked = False

            self.moved_d = (renpy.easy.displayable_or_none(moved_d) or Null()) if not (callable(moved_d) and not isinstance(moved_d, renpy.display.core.Displayable)) else moved_d
            self.moved_fixed = moved_fixed
            self.moved_uptime = float(moved_uptime)

            self.clicked_ids = set()
            self.moved_ids = set()
        
        def _update_function(self, st):
            for s in self.children:
                id_s = id(s)

                if id_s in self.clicked_ids:
                    time = self.clicked_uptime
                    _set = self.clicked_ids
                
                elif id_s in self.moved_ids:
                    time = self.moved_uptime
                    _set = self.moved_ids
                
                else:
                    time = 0.0
                    _set = None

                cache = s.cache

                if cache.st is not None and st - cache.st >= time:
                    s.destroy()
                    if _set is not None: _set.remove(id_s)
            
            return 0.0
        
        def _predict_function(self):
            rv = [ ]
            if isinstance(self.clicked_d, renpy.display.core.Displayable): rv.append(self.clicked_d)
            if isinstance(self.moved_d, renpy.display.core.Displayable):   rv.append(self.moved_d)
            return rv 
        
        def _event_function(self, ev, x, y, st):
            if getattr(ev, "button", None) in (4, 5): return # checking for mousewheel

            if ev.type == pygame.MOUSEBUTTONUP:
                self._clicked = False

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                self._clicked = True

                d = self._get_displayable(self.clicked_d, self.clicked_fixed)

                s = self.create(d)
                s.x = x
                s.y = y
                s.zorder = 1

                self.clicked_ids.add(id(s))

                self.redraw()
            
            elif ev.type == pygame.MOUSEMOTION and self._clicked:
                d = self._get_displayable(self.moved_d, self.moved_fixed)

                s = self.create(d)
                s.x = x
                s.y = y
                s.zorder = 0

                self.moved_ids.add(id(s))

                self.redraw()

            return None
    
        @staticmethod
        def _get_displayable(d, fixed):
            if callable(d) and not isinstance(d, renpy.display.core.Displayable): d = d()
            d = Transform(d, anchor=(0.5, 0.5))
            if fixed: d = Fixed(d)
            return d

# examples

# this is the screen needed
screen click_effects():
    zorder 999 layer "front"

    default effects = click_effects.ClickEffects(
        # using the type (a callable)     a class variable                         no need to wrap it since it's a container
        click_effects.ClickEffectExample, click_effects.ClickEffectExample.UPTIME, False,
        #                                                                                                                                                             need to wrap it since it's a single displayable
        At("gui/menu_particle.png", Transform(xysize=(15, 15)), _move_particle_example(click_effects.MOVED_UPTIME_EXAMPLE)), click_effects.MOVED_UPTIME_EXAMPLE, True
    )

    add effects


transform _click_particle_example(start_pos, end_pos, t):
    zoom 1.0 alpha 0.6
    pos start_pos subpixel True

    parallel:
        easeout t pos end_pos zoom 1.0
    parallel:
        easein (t * 0.2) zoom 1.2
        easeout (t * 0.8) zoom 0.0
    parallel:
        ease 0.095 alpha (0.6 - random.choice((0.3, -0.2)))
        ease 0.095 alpha 0.6
        repeat

transform _click_circle_example(t):
    zoom 1.0 subpixel True alpha 1.0
    easein (t * 0.2) zoom 1.05
    easeout_quad (t * 0.8) zoom 0.0 alpha 0.0

transform _move_particle_example(t):
    alpha 1.0 subpixel True
    ease t alpha 0.0

init python in click_effects:
    import random
    import math
    from store import absolute

    # how long the `moved_d` displayable is shown
    MOVED_UPTIME_EXAMPLE = 0.3

    class ClickEffectExample(renpy.display.layout.Container):
        # the radius of the circle, kinda?
        RADIUS = 25

        # how long this displayable shows for
        UPTIME = 0.47

        # how many particles show when clicking
        PARTICLE_NUMBER = 8

        def __init__(self):
            super(ClickEffectExample, self).__init__()

            self.add(
                At(
                    "mod_assets/circle.png",
                    Transform(xysize=(absolute(self.RADIUS * 1.8), absolute(self.RADIUS * 1.8)), anchor=(0.5, 0.5)),
                    store._click_circle_example(self.UPTIME)
                )
            )

            for _ in range(self.PARTICLE_NUMBER):
                angle = random.uniform(0.0, 360.0)

                start_pos = self.find_pos(angle, 1.0)
                end_pos   = self.find_pos(angle, 2.4)

                d = Transform("gui/menu_particle.png", xysize=(20, 20), anchor=(0.5, 0.5), rotate=angle)
                d = Transform(d, zoom=random.uniform(0.8, 1.0))

                triangle = At(d, store._click_particle_example(start_pos, end_pos, self.UPTIME))
                self.add(triangle)

        def find_pos(self, angle, r):
            x = math.cos(angle) * self.RADIUS * r
            y = math.sin(angle) * self.RADIUS * r
            return absolute(x), absolute(y)