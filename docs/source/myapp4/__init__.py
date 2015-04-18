from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(
        settings=settings)
    config.include("pyramid_tm")
    config.include("pyramid_sqlalchemy")
    config.include("pyramid_jinja2")
    config.add_route('top', '/')
    config.add_route('user', '/users/{username}')
    config.scan()
    return config.make_wsgi_app()
