import sublime
import sublime_plugin


class DoubleView(sublime_plugin.WindowCommand):
  def run(self):

    # layout with two windows
    self.window.set_layout( {
      "cols": [0.0, 0.5, 1.0],
      "rows": [0.0, 1.0],
      "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
    } )

    self.window.set_sidebar_visible(False)
    self.window.set_minimap_visible(False)

    # fixes a rendering bug where sublime shows lots of scroll bars
    self.window.focus_group(1)

    #smaller font to see side by side
    s = sublime.load_settings("Preferences.sublime-settings")
    s.set("font_size", 10 )
    
