import sublime
import sublime_plugin
import subprocess
import os

class GitLogSelection(sublime_plugin.WindowCommand):
  def run(self, cmd):

    if "$file_name" in cmd:
      view = self.window.active_view()
      cmd = cmd.replace( "$file_name",view.file_name() )

    if "$lines" in cmd:

      # code section copied from https://stackoverflow.com/questions/19707727/api-how-to-get-selected-text-from-object-sublime-selection
      selection = view.sel()

      if len( selection ) > 0:
        selectedRegion = selection[0]

        startLine, startColumn = view.rowcol( selectedRegion.begin() )
        endLine, endColumn = view.rowcol( selectedRegion.end() )

        numberOfLines = endLine - startLine

        cmd = cmd.replace( "$lines", str( startLine ) + ',+' + str( numberOfLines ) )
        
        print ('Running custom command:', cmd)

        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=os.path.split(view.file_name())[0])

        # self.view.insert(edit, 0, "Hello, World!")
        outputView = self.window.new_file()
        outputView.set_name( "Git Log Selection")
        # sublime.run_command("new_window")
        # sublime.active_window().view.insert( edit, 0, "Hey there world!")
        while proc.poll() is None:
          line = proc.stdout.readline()
          if( len(line) > 0):

            # from a WindowCommand, must use run_command to get an edit
            outputView.run_command( "view_append", { "text": line.decode("utf-8") } )            

            # print (line.decode("utf-8")) # give output from your execution/your own message
        self.commandResult = proc.wait() # catch return code

        # don't save or edit the output
        outputView.set_scratch( True )

        syntax_file = "Packages/Git/syntax/Git Commit View.tmLanguage"
        outputView.set_syntax_file(syntax_file)

class ViewAppend(sublime_plugin.TextCommand):
  def run( self, edit, text ):
    self.view.insert( edit, self.view.size(), text )