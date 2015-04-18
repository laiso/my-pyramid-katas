from webob.dec import wsgify


@wsgify
def application(request):
    request.response.text = "Hello, world!"
    return request.response
