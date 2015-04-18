from pyramid.view import view_config


@view_config()
def index(request):
    request.response.text = "Hello, world!"
    return request.response
