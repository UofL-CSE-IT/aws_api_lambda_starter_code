import json
from handlers import write_to_database, read_from_database

def lambda_handler(event, context):
    path = event.get('path')
    method = event.get('httpMethod')

    if path == '/teams/16/write' and method == 'POST':
        return write_to_database.handler(event, context)
    elif path == '/teams/16/read' and method == 'GET':
        return read_from_database.handler(event, context)
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Not Found'})
        }

def main():
    # Example event for testing POST /write
    event_write = {
        "path": "/teams/16/write",
        "httpMethod": "POST",
        "body": json.dumps(
            {
                "first_name": "Joe",
                "last_name": "Trump",
                "address": "1600 Pennsylvania Ave NW",
                "city": "Washington",
                "state": "DC",
                "zip": "20500"
            }
        )
    }

    # Example event for testing GET /read
    event_read = {
        "path": "/teams/16/read",
        "httpMethod": "GET"
    }

    # Simulate AWS Lambda context (can be empty for testing)
    context = {}

    # Test the write_to_database handler
    response_write = lambda_handler(event_write, context)
    print("Response for POST /write:")
    print(json.dumps(response_write, indent=4))

    # Test the read_from_database handler
    response_read = lambda_handler(event_read, context)
    print("Response for GET /read:")
    print(json.dumps(response_read, indent=4))

if __name__ == "__main__":
    main()