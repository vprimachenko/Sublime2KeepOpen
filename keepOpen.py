import sublime, sublime_plugin

class keepOpen(sublime_plugin.EventListener):
    def on_close(self, view):
       if len(sublime.windows()) == 1 and len(sublime.windows()[0].views()) == 1:
       		sublime.windows()[0].new_file()
