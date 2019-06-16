try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Aidan',
        'url': '<source url>',
        'download_url': 'Where to download it.',
        'author_email': 'My email',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'projectname'
}

setup(**config)
