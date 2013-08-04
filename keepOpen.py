import sublime, sublime_plugin

class keepOpen(sublime_plugin.EventListener):
    def on_close(self, view):
        # get version via api change
        sv = 2
        if hasattr(sublime.Window,"lookup_symbol_in_index"):
            sv = 3

        if len(sublime.windows()) == 1 and len(sublime.windows()[0].views()) == [43,1,1,0][sv]:
            sublime.windows()[0].new_file()
