from __future__ import print_function

import boto3
import json

def lambda_handler(event, context):
    
    dynamo = boto3.resource('dynamodb').Table('toDoList')
    
    
    route = event['routeKey']
    response = "{}"
    payload = "{}"
    body = json.loads(event['body'].strip()) if len(event['body']) > 0 else {}
    print(len(body))
    try:

        if len(body) > 0:
            payload = {
                    'id': body['id'],
                    'name': body['name'],
                    'status': body['status']
                }
   
    
        response=payload
        
        if route == "GET /items": # Get List of tasks
            items =  dynamo.scan()
            print(items)
            response = items["Items"]
            statusCode = 200
        if route == "PUT /items":
            response = dynamo.put_item(Item=payload)
            statusCode = 201
        if(route == 'GET /items/{id}'):
            params = event['pathParameters']
            getItem = dynamo.get_item( Key = params)

            if 'Item' in getItem:
                response = getItem['Item']
                statusCode = 200
            else:
                return {
                    'statusCode': '404',
                    'body': 'Not found'
                }
        if(route == 'DELETE /items/{id}'):
            params = event['pathParameters']
            delete = dynamo.delete_item(Key = params)
            print(delete)
            
            if delete['ResponseMetadata']['HTTPStatusCode'] == 200:
                response = 'record deleted'
                statusCode = 200
            else:
                response = delete
                statusCode = delete['ResponseMetadata']['HTTPStatusCode']
    
    except:
        response = "Something else went wrong" 
        statusCode = 400
    
    return {
        'statusCode': statusCode,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,HEAD'
        },
        'body': json.dumps(response)
        
        
    }