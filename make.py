import re
from os import path
from collections import OrderedDict
import json
import sublime
import sublime_plugin


DIR = path.dirname(path.realpath(__file__))


def build():
    with open(path.join(DIR, 'src/rules.json-scs')) as file:
        rules = sublime.decode_value(file.read())

    with open(path.join(DIR, 'src/Cloud.json-scs')) as file:
        cloud = OrderedDict(sublime.decode_value(file.read()))
        cloud.update(rules)

    with open(path.join(DIR, 'src/Nether.json-scs')) as file:
        nether = OrderedDict(sublime.decode_value(file.read()))
        nether.update(rules)

    # Note: we encode with json rather than sublime.encode_value because it
    # respects ordered dicts.

    with open(path.join(DIR, 'Cloud.sublime-color-scheme'), mode='w') as file:
        file.write(json.dumps(cloud, indent=2))

    with open(path.join(DIR, 'Nether.sublime-color-scheme'), mode='w') as file:
        file.write(json.dumps(nether, indent=2))



class ColorSchemeListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        pt = view.file_name()
        rel = path.relpath(view.file_name(), DIR)
        if rel.startswith('src/'):
            build()
