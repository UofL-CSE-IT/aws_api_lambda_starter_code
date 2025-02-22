import json
import pymysql
from db_credentials import db_username, db_password, db_name, db_url

def handler(event, context):
    # Connect to the database
    connection = pymysql.connect(
        host=db_url,
        user=db_username,
        password=db_password,
        database=db_name
    )

    try:
        with connection.cursor() as cursor:
            # Execute the query
            sql = "SELECT id, first_name, last_name, address, city, state FROM fake_users"
            cursor.execute(sql)
            result = cursor.fetchall()

            # Convert the result to a list of dictionaries
            data = []
            for row in result:
                data.append({
                    'id': row[0],
                    'first_name': row[1],
                    'last_name': row[2],
                    'address': row[3],
                    'city': row[4],
                    'state': row[5]
                })

    finally:
        connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }