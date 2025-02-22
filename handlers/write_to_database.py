import json
import pymysql
from db_credentials import db_username, db_password, db_name, db_url

def handler(event, context):
    # Extract data from the event
    body = json.loads(event.get('body', '{}'))
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    address = body.get('address')
    city = body.get('city')
    state = body.get('state')
    zip_code = body.get('zip')

    # Validate the input data
    if not all([first_name, last_name, address, city, state, zip_code]):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing required fields'})
        }

    # Connect to the database
    connection = pymysql.connect(
        host=db_url,
        user=db_username,
        password=db_password,
        database=db_name
    )

    try:
        with connection.cursor() as cursor:
            # Execute the insert query
            sql = """
                INSERT INTO fake_users (first_name, last_name, address, city, state, zip)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (first_name, last_name, address, city, state, zip_code))
            connection.commit()

    finally:
        connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data written to database successfully'})
    }