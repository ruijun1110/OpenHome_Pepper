import datetime
import os.path
from conversation_manager import manage_conversation
from LLM import chatgpt
from colorama import Fore, Style 
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import pytz

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
weekdays = {6:"Sunday", 0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday"}
command_processing_prompt_file = open("capabilities/command_processing_prompt.txt", "r")
command_processing_prompt = command_processing_prompt_file.read()
command_processing_prompt_file.close()
# If modifying these scopes, delete the file token.json.
deletion_prompt_file = open("capabilities/deletion_prompt.txt", "r")
deletion_prompt = deletion_prompt_file.read()
deletion_prompt_file.close()

def calendar_authenticate():
    """Authenticate the user and return the credentials."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def command_processing(file_data, command):
    date = datetime.date.today()
    pst_datetime = datetime.datetime.now(pytz.timezone('US/Pacific')).isoformat()
    weekday = weekdays[datetime.date.today().weekday()]
    print(f"[current datetime] {pst_datetime} {weekday}")
    edit_user_message = f"[date] {date} [weekday] {weekday} [datetime] {pst_datetime} [Inquiry] {command}"
    command_process_conversation = manage_conversation(edit_user_message, [], role='user') 
    response = chatgpt(file_data['openai_api_key'], command_process_conversation, command_processing_prompt, temperature=1.2)
    command_process_conversation = manage_conversation(response, command_process_conversation, role='assistant')
    print(Fore.CYAN + f"Command processed: {response}" + Style.RESET_ALL) 
    return command_to_function_mapping(file_data, remove_quotation_marks(response), command)

def command_to_function_mapping(file_data, response, user_message):
    command_args = response.split(",")
    system_response = ""
    if command_args[0] == "search":
        system_response = get_calendar_events(time_min=command_args[1], time_max=command_args[2])
    elif command_args[0] == "insert":
        system_response = create_event(start_datetime=command_args[1], end_datetime=command_args[2], description=command_args[3])
    elif command_args[0] == "delete":
        system_response = delete_event(user_message=user_message, time_min=command_args[1], time_max=command_args[2], file_data=file_data)
    return system_response

def get_calendar_events(number_of_events=5, time_min=None, time_max=None):
  creds = calendar_authenticate()

  try:
    events_summary = "Search Result \n"
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    # RFC3339 timestamp with mandatory time zone offset
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=time_min if time_min else now,
            timeMax=time_max,
            timeZone="America/Los_Angeles",
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      events_summary += "No events found in the given time range."    
    else :
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            events_summary += start + " " + event["summary"] + "\n"

    return events_summary

  except HttpError as error:
    print(f"An error occurred: {error}")

def get_calendar_events_with_id(time_min=None, time_max=None):
  creds = calendar_authenticate()

  try:
    events_summary = "[Events]: \n"
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    # RFC3339 timestamp with mandatory time zone offset
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=time_min if time_min else now,
            timeMax=time_max,
            timeZone="America/Los_Angeles",
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      events_summary += "No events found in the given time range."    
    else :
        for event in events:
            description = event["summary"]
            event_id = event["id"]
            events_summary += event_id + ": " + description +"\n"

    #   print(start, event["summary"])
    return events_summary

  except HttpError as error:
    print(f"An error occurred: {error}")   

def create_event(start_datetime, end_datetime, description):
  creds = calendar_authenticate()
  service = build("calendar", "v3", credentials=creds)
  event = {
    'summary': description,
    'start': {
        'dateTime': start_datetime,
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': end_datetime,
        'timeZone': 'America/Los_Angeles',
    }
  }
  # Determine if the datetime string contains microseconds
  if '.' in start_datetime:
    # If microseconds are present, include them in the format string
    format_string = '%Y-%m-%dT%H:%M:%S.%f%z'
  else:
    # If microseconds are not present, exclude them from the format string
    format_string = '%Y-%m-%dT%H:%M:%S%z'
  start_date = datetime.datetime.strptime(start_datetime, format_string).strftime('%A %B %d %Y %H:%M')
  if '.' in end_datetime:
    format_string = '%Y-%m-%dT%H:%M:%S.%f%z'
  else:
    format_string = '%Y-%m-%dT%H:%M:%S%z'
  end_datetime = datetime.datetime.strptime(end_datetime, format_string).strftime('%A %B %d %Y %H:%M')
#   print(f'Creating an event for {description} from {start_date} to {end_datetime}')
  event = service.events().insert(calendarId='primary', body=event).execute()
  return f'Your event for {description} on {start_date} has been created.'

def delete_event(user_message,time_min, time_max, file_data):
  creds = calendar_authenticate()
  calendar_data = get_calendar_events_with_id(time_min=time_min, time_max=time_max)
  command = f"[Description]{user_message} {calendar_data}"
  temp_conversation = manage_conversation(command, [], role='user')
  event_id = chatgpt(file_data['openai_api_key'], temp_conversation, deletion_prompt, temperature=1.2)
  service = build("calendar", "v3", credentials=creds)
  try:
    service.events().delete(calendarId='primary', eventId=event_id).execute()
    return f'Your event has been deleted.'
  except HttpError as error:
    print(f"An error occurred: {error}")


def remove_quotation_marks(s):
    # Check if the string starts and ends with a quotation mark
    if s.startswith('"') and s.endswith('"'):
        # Remove the quotation marks from both ends
        return s.strip('"')
    # If the string does not start and end with a quotation mark, return it as is
    return s


if __name__ == "__main__":
  get_calendar_events()