import azure.functions as func
import logging
import mysql.connector
from mysql.connector import errorcode

t1 = func.Blueprint()


@t1.route(route="test01", auth_level=func.AuthLevel.ANONYMOUS)
def test01(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger(test01) function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function(test01) executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
