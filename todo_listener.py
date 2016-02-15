import sublime
import sublime_plugin


class TODOListener(sublime_plugin.EventListener):
    '''Boxes 'todo' statements (ignores case) in the buffer'''
    def on_modified_async(self, view):
        found = view.find_all("TODO", sublime.IGNORECASE)
        view.add_regions("todo", found, "comment", '', sublime.DRAW_NO_FILL)
