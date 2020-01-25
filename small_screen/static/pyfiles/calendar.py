import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_events():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z' 
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return {"start": "", "event": "Heute steht nichts an!"}
    for event in events:
        start_raw = event['start'].get('dateTime', event['start'].get('date'))
        end_raw = event["end"].get("dateTime", event["end"].get("date"))
        
        event_dt = datetime.datetime.strptime(start_raw.split("T")[0], "%Y-%m-%d") # error
        start = datetime.datetime.strptime(start_raw.split("T")[1].split("+")[0], "%H:%M:%S")
        end = datetime.datetime.strptime(end_raw.split("T")[1].split("+")[0], "%H:%M:%S")
        event_dt_split = str(event_dt).split()[0].replace("-", ".").split(".")
        _event = f"{event_dt_split[2]}.{event_dt_split[1]}.{event_dt_split[0]}"
        
        return {"start": str(start).split()[1], "event": event["summary"], "end": str(end).split()[1], "event_dt": _event}