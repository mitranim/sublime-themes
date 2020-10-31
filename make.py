import sublime
import sublime_plugin
from os import path as pt
import glob

DIR = pt.dirname(pt.realpath(__file__))
DIR_SRC = pt.join(DIR, 'src')

def build():
    with open(pt.join(DIR_SRC, 'rules.json')) as file:
        rules = sublime.decode_value(file.read())

    for src_path in glob.iglob(pt.join(DIR_SRC, '*.json-color-scheme')):
        with open(src_path) as src:
            config = sublime.decode_value(src.read())
            config.update(rules)

        (name, _) = pt.splitext(pt.basename(src_path))
        out_path = pt.join(DIR, name + '.sublime-color-scheme')

        with open(out_path, mode='w') as out:
            out.write(sublime.encode_value(config, pretty=True))

class ColorSchemeListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        is_src = view.file_name().startswith(DIR_SRC + pt.sep)
        if is_src:
            build()
