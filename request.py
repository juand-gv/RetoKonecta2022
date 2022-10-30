import requests
import psycopg2
import json
from time import sleep
from datetime import datetime

while(True):
    resp = requests.get('https://mqjl9s6vf4.execute-api.eu-west-1.amazonaws.com/prod/v1/hackday/public/event')
    event = resp.json()
    event = event["payload"]["data"]["onCreateHackathonEvents"]["event"]
    event = json.loads(event)
    event1 = event["detail"]["events"][0]
    event2 = event["detail"]["events"][1]
    time1 = int(event1["time"])
    # datetime1 = datetime.fromtimestamp(time1)
    servicio = event1["detail"]["eventBody"]["service"]["name"]
    rMemberUsers = int(event1["detail"]["eventBody"]["data"]["metrics"][0]["stats"]["count"])
    rActiveMembers = int(event1["detail"]["eventBody"]["data"]["metrics"][1]["stats"]["count"])
    INTERACTING = int(event1["detail"]["eventBody"]["data"]["metrics"][2]["stats"]["count"])
    IDLE = int(event1["detail"]["eventBody"]["data"]["metrics"][3]["stats"]["count"])
    ACW = int(event1["detail"]["eventBody"]["data"]["metrics"][4]["stats"]["count"])


    try:
        connection = psycopg2.connect(host='localhost',
                                            database='konecta',
                                            user='postgres',
                                            password='toor',
                                            port='5432')
        cursor = connection.cursor()

        postgres_insert_query = f"""INSERT INTO streamingdata (timestamp, rMemberUsers, rActiveMembers, rOnQueueUsers_INTERACTING, rOnQueueUsers_IDLE, rOnQueueUsers_ACW) 
                            VALUES 
                            ({time1},{rMemberUsers},{rActiveMembers},{INTERACTING},{IDLE},{ACW}) """
        record_to_insert = (5, 'One Plus 6', 950)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into streamingdata table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into streamingdata table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    sleep(5)
