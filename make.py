from os import path
import sublime
import sublime_plugin


DIR = path.dirname(path.realpath(__file__))


def build():
    with open(path.join(DIR, 'src/rules.sublime-color-scheme')) as file:
        rules = sublime.decode_value(file.read())

    with open(path.join(DIR, 'src/Cloud.sublime-color-scheme')) as file:
        cloud = sublime.decode_value(file.read())
        cloud.update(rules)

    with open(path.join(DIR, 'Cloud.sublime-color-scheme'), mode='w') as file:
        file.write(sublime.encode_value(cloud, True))

    with open(path.join(DIR, 'src/Nether.sublime-color-scheme')) as file:
        nether = sublime.decode_value(file.read())
        nether.update(rules)

    with open(path.join(DIR, 'Nether.sublime-color-scheme'), mode='w') as file:
        file.write(sublime.encode_value(nether, True))


class ColorSchemeListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        pt = view.file_name()
        rel = path.relpath(view.file_name(), DIR)
        if rel.startswith('src/'):
            build()
