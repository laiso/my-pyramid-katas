from webob import Request, Response


def application(environ, start_response):
    request = Request(environ)
    response = Response(request=request)
    response.text = "Hello, world!"
    return response(environ, start_response)
