from pyramid.view import view_config


@view_config(route_name="top")
def index(request):
    request.response.text = "Hello, world!"
    return request.response


@view_config(route_name="user")
def user(request):
    username = request.matchdict["username"]
    request.response.text = "Hello, {username}!".format(username=username)
    return request.response
