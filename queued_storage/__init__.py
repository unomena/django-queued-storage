__version__ = "0.6.unomena"


def version_hook(config):
    config['metadata']['version'] = __version__
