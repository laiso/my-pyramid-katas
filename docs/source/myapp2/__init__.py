from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(
        settings=settings)
    config.add_route('top', '/')
    config.add_route('user', '/users/{username}')
    config.scan()
    return config.make_wsgi_app()
