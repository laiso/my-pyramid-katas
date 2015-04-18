from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(
        settings=settings)
    config.scan()
    return config.make_wsgi_app()
