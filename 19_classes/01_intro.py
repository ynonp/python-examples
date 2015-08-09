"""
1. Class syntax
2. Passing parameters to methods and constructor
3. Object vs. Class variables/methods
4. Private members
"""

class Light(object):
    def __init__(self, val=False):
        self._on = val

    def lights_on(self):
        if not self._on:
            print "Lights on"
            self._on = True

    def lights_off(self):
        if self._on:
            print "Lights off"
            self._on = False

l = Light()
g = Light(val=True)

l.lights_on()

l._on = False

l.lights_on()

