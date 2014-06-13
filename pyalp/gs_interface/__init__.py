from os.path import join, dirname, exists, isdir

HERE = dirname(__file__)


KEYS_DIR = join(HERE, 'keys')
assert exists(KEYS_DIR) and isdir(KEYS_DIR)


def init():
    import sys
    sys.path.insert(
        0,
        join(HERE, 'tinyrpc')
    )
