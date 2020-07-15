import logging
import requests
import azure.functions as func


GRAPH_API_URL = 'https://graph.microsoft.com/'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #auth = req.headers['Authorization']
    split_url = req.url.split('/api/HttpTrigger1/', 1)
    new_url = GRAPH_API_URL + split_url[1]
    method = req.method
    response = requests.request(
        method=method,
        url=new_url,
        headers=req.headers,
        data=req.get_json()
    )
    return func.HttpResponse(f"Hello! Repsonse was{response}")
    #return func.HttpRequest(method=req.method, url=new_url, headers=req.headers, params=req.params, body=req.body)

    # pathsplit = url.split('/', 1)
    
    # if len(pathsplit) < 2 or pathsplit[0] not in ['v1.0', 'beta']:
    #     return Response('', status=503)
    # if request.method == 'GET':
    #     r = requests.get(f'{GRAPH_API_URL}/{path}', data=request.data,
    #                      params=request.args, headers=request.headers)
    # elif request.method == 'POST':
    #     r = requests.post(f'{GRAPH_API_URL}/{path}', data=request.data, 
    #                       params=request.args, headers=request.headers)
    # elif request.method == 'DELETE':
    #     r = requests.delete(f'{GRAPH_API_URL}/{path}', data=request.data,
    #                         params=request.args, headers=request.headers)
    # else:
    #     raise MiddlewareException("Unhandled forward")
    # if not r.ok or r.status_code < 200 or r.status_code > 299:
    #     logging.warning(f"Failed pass-through to {path} with {r.status_code} due to {r.text}")
    #     logging.warning(request.headers)
    # return Response(r.content, status=r.status_code)
