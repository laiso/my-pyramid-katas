from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from .models import User


@view_config(route_name="top",
             renderer='templates/index.jinja2')
def index(request):
    return dict()


@view_config(route_name="user",
             renderer='templates/user.jinja2')
def user(request):
    username = request.matchdict["username"]
    user = User.query.filter(User.username == username).first()
    if user is None:
        raise HTTPNotFound

    return dict(user=user)
