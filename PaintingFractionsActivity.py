from sugar.activity import activity
import logging
 
import sys, os
import gtk
import pygame
from sugar.activity import activity
from sugar.graphics.toolbutton import ToolButton
import gobject
import sugargame.canvas
import color

 
class PaintingFractionsActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.game = color.pyGrafic()
	self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
	self._pygamecanvas.run_pygame(self.game.loop)

	toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()
