import sublime
import sublime_plugin
from os import path as pt
import glob

DIR = pt.dirname(pt.realpath(__file__))
DIR_SRC = pt.join(DIR, 'src')

class ColorSchemeListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        is_src = pt.realpath(view.file_name()).startswith(DIR_SRC + pt.sep)
        if is_src:
            rebuild()

def rebuild():
    rules_cache = {}
    for path in glob.iglob(pt.join(DIR_SRC, '*.json-color-scheme')):
        scheme = read_file(path)
        make_color_scheme(scheme, rules_cache)
        write_color_scheme_file(base_name_without_ext(path), scheme)

def make_color_scheme(scheme, rules_cache):
    rules_name = scheme.pop('rules')
    if rules_name not in rules_cache:
        rules_cache[rules_name] = read_src_file(rules_name)
    scheme.update(rules_cache[rules_name])

def read_file(path):
    with open(path) as file:
        return sublime.decode_value(file.read())

def read_src_file(name):
    return read_file(pt.join(DIR_SRC, name))

def write_color_scheme_file(name, value):
    write_out_file(name + '.sublime-color-scheme', value)

def write_out_file(name, value):
    path = pt.join(DIR, name)
    with open(path, mode='w') as file:
        file.write(sublime.encode_value(value, pretty=True))

def base_name_without_ext(path):
    (name, _) = pt.splitext(pt.basename(path))
    return name
