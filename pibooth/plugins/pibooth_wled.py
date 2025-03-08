# -*- coding: utf-8 -*-

import pibooth
from pibooth import evts
from pibooth.plugins.wled_api import WLEDAPI


"""Plugin to manage the some leds via WLED api.
"""
__version__ = "0.0.1"

wled = WLEDAPI("192.168.20.135")

@pibooth.hookimpl
def state_wait_enter(app):
    wled.set_effect(184)
    wled.set_brightness(100)
    wled.on()


#@pibooth.hookimpl
#def state_wait_do(self, app, events):
#    if evts.find_event(events, evts.EVT_PIBOOTH_PRINT) and app.previous_picture_file and app.printer.is_ready():
#       if app.count.remaining_duplicates <= 0:
#            app.leds.printer.off()
#
#    if not app.previous_picture_file and app.leds.printer._controller:  # _controller == blinking
#        app.leds.printer.off()
#
@pibooth.hookimpl
def state_wait_exit(app):
    wled.off()

@pibooth.hookimpl
def state_choose_enter(app):
    wled.set_effect(0)
    wled.set_brightness(50)

#@pibooth.hookimpl
#def state_choose_exit(self, app):
#    app.leds.capture.off()
#    app.leds.printer.off()

#@pibooth.hookimpl
#def state_print_enter(self, app):
#    app.leds.blink(on_time=self.blink_time, off_time=self.blink_time)

#@pibooth.hookimpl
#def state_print_do(self, app, events):
#    if evts.find_event(events, evts.EVT_PIBOOTH_PRINT):
#        app.leds.printer.on()
#        app.leds.capture.off()

@pibooth.hookimpl
def state_finish_enter(app):
    wled.off()
