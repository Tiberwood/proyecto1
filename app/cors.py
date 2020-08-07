class CorsMiddleware(object):

    def process_response(self, request, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response