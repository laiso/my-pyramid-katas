from pyramid.config import Configurator


def index(request):
    request.response.text = "Hello, world!"
    return request.response

config = Configurator()
config.add_view(index)
application = config.make_wsgi_app()
