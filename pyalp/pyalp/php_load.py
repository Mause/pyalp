import re

COMMENT_RE = re.compile(r'//([^\n]*\n)')
INLINE_REPLACE_RE = re.compile(r'("\.(\w+)\.")')
KILL_INSTALL_RE = re.compile(r'\$lang\["install"\].*;')

replacements = {'MONEY_SYMBOL': '$'}

subs = [
    # remove comments
    (COMMENT_RE, lambda k: '# ' + k.groups()[0]),

    # mend inline replacements
    (INLINE_REPLACE_RE, lambda k: replacements.get(k.groups()[1], '')),

    # kill install crap
    (KILL_INSTALL_RE, lambda _: '')
]

literals = [
    ('=>', ':'),
    (' :', ':'),
    ('<?php', ''), ('?>', ''),
    ('array(', '{'), (')', '}'),
    ('\t', '    ')
]


def load_php_file(path, context=None, custom_subs=None, custom_literals=None):
    """
    Load a php file containing translations in PHP Arrays

    the french dataset is encoded in latin-1, so we load in binary mode,
    try and decode using utf-8 first, then latin-1 if utf-8 fails
    """
    cur_subs = subs + (custom_subs or [])
    cur_literals = literals + (custom_literals or [])

    with open(path, 'rb') as fh:
        data = fh.read()

    try:
        data = data.decode('utf-8')
    except UnicodeDecodeError:
        data = data.decode('latin-1')

    # regex replacements
    for RE, func in cur_subs:
        data = RE.sub(func, data)

    # literal replacements
    for before, after in cur_literals:
        data = data.replace(before, after)

    context = context or {}
    exec(data, context)

    if '__return__' in context:
        del context['__return__']
    if '__builtins__' in context:
        del context['__builtins__']

    return context


def load_lang_file(path):
    return load_php_file(
        path,
        custom_literals=[('$lang', 'lang')]
    )['lang']
