from pyramid.view import view_config


@view_config(route_name="top",
             renderer='templates/index.jinja2')
def index(request):
    return dict()


@view_config(route_name="user",
             renderer='templates/user.jinja2')
def user(request):
    username = request.matchdict["username"]
    return dict(username=username)
