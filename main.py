from mangum import Mangum

def app(scope, receive, send):
    """Ultra minimal ASGI app"""
    if scope["type"] == "http":
        response_body = b'{"message": "Zain RAG Bot Working!", "status": "success"}'
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"application/json"]],
        })
        await send({
            "type": "http.response.body",
            "body": response_body,
        })

handler = Mangum(app)
