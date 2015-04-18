from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(
        settings=settings)
    config.include("pyramid_tm")
    config.include("pyramid_sqlalchemy")
    config.include("pyramid_jinja2")
    config.include("pyramid_deform")
    config.include("pyramid_layout")
    config.add_route('top', '/')
    config.add_route('users', '/users')
    config.add_route('new_user', '/new_user')
    config.add_route('user', '/users/{username}')
    config.scan()
    return config.make_wsgi_app()
