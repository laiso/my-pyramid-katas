import os
from . import main

here = os.getcwd()

settings = {
    'sqlalchemy.url': 'sqlite:///{here}/myapp4.sqlite'.format(here=here),
    'sqlalchemy.echo': True,
}

application = main({}, **settings)
