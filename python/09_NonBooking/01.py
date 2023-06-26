import os.path
import datefinder
from flask import Flask, request, jsonify
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json')
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'CREDENTIALS_FILE.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Initialize Flask app
app = Flask(__name__)

# Setup route for creating events
@app.route('/create_event', methods=['POST'])
def create_event():
    data = request.get_json()

    # Make sure all necessary data is provided
    if not all(key in data for key in ['summary', 'description', 'start', 'end']):
        return jsonify({'error': 'Missing data'}), 400

    # Parse dates
    start_matches = list(datefinder.find_dates(data['start']))
    if len(start_matches):
        start_time = start_matches[0]
    else:
        return jsonify({'error': 'Invalid start date format'}), 400

    end_matches = list(datefinder.find_dates(data['end']))
    if len(end_matches):
        end_time = end_matches[0]
    else:
        return jsonify({'error': 'Invalid end date format'}), 400

    # Build the event body
    event_body = {
        'summary': data['summary'],
        'description': data['description'],
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Bangkok',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Bangkok',
        },
    }

    try:
        # Call the Calendar API
        service = build('calendar', 'v3', credentials=creds)
        event = service.events().insert(calendarId='primary', body=event_body).execute()
        return jsonify({'event_id': event['id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
