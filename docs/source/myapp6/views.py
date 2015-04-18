from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid_deform import FormView
from colanderalchemy import SQLAlchemySchemaNode
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


@view_config(route_name="users",
             renderer="templates/users.jinja2")
def users(request):
    users = User.query.all()
    return dict(users=users)


@view_config(route_name="new_user",
             renderer="templates/new_user.jinja2")
class NewUserForm(FormView):
    schema = SQLAlchemySchemaNode(User,
                                  excludes=['id'])
    buttons = ('add',)

    def add_success(self, values):
        user = User(**values)
        user.query.session.add(user)
        return HTTPFound(self.request.route_url('users'))
