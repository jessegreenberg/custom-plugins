# Custom Sublime Package

This package can be used with sublime to add custom tasks to the command palette.

To add these to your copy of sublime, locate your Packages folder. `Preferences --> Browse Packages`. Then copy the  `custom-plugin` folder into the `Packages` directory. (On Windows the file path looks like: 
`C:\Users\{{USER}}\AppData\Roaming\Sublime Text 3\Packages\`).

When these commands are added into the `Packages` folder in the Sublime installation directory, then they will also be
added to the command palette, although a restart may be required.

## List of Commands:
- git_log_selection:
  - Opens a window showing commits for selected lines in the view.
- single_view:
  - Sets the Sublime window to settings that look good with a single view (larger fonts, show minimap, show sidebar).
- double_view:
  - Sets the Sublime window to settings that look good with a double view (smaller font, hide minimap, hide sidebar)