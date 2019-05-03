import sublime
import sublime_plugin


class SetSingle(sublime_plugin.WindowCommand):
  def run(self):

    # layout with two windows
    self.window.set_layout( {
      "cols": [0.0, 1.0],
      "rows": [0.0, 1.0],
      "cells": [[0, 0, 1, 1]]
    } )

    self.window.set_minimap_visible(True)
    self.window.set_sidebar_visible(True)

    # larger font size with only one window
    s = sublime.load_settings("Preferences.sublime-settings")
    s.set("font_size", 14 )
