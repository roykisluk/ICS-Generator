from datetime import datetime

# Define the events
events = [
    {"date": "2025-05-05", "day": "יום ב", "start_time": "09:00", "end_time": "12:00"},
    {"date": "2025-05-08", "day": "יום ה", "start_time": "15:00", "end_time": "18:00"},
    {"date": "2025-05-12", "day": "יום ב", "start_time": "09:00", "end_time": "12:00"},
    {"date": "2025-05-15", "day": "יום ה", "start_time": "15:00", "end_time": "18:00"},
    {"date": "2025-05-19", "day": "יום ב", "start_time": "09:00", "end_time": "12:00"},
    {"date": "2025-05-22", "day": "יום ה", "start_time": "15:00", "end_time": "18:00"},
    {"date": "2025-05-26", "day": "יום ב", "start_time": "09:00", "end_time": "12:00"},
    {"date": "2025-05-28", "day": "יום ד", "start_time": "16:00", "end_time": "19:00"}
]

# Start building the iCalendar content
ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Schedule//EN
CALSCALE:GREGORIAN
"""

# Add each event to the calendar
for e in events:
    start_dt = datetime.strptime(f"{e['date']} {e['start_time']}", "%Y-%m-%d %H:%M").strftime('%Y%m%dT%H%M%S')
    end_dt = datetime.strptime(f"{e['date']} {e['end_time']}", "%Y-%m-%d %H:%M").strftime('%Y%m%dT%H%M%S')
    timestamp = datetime.now().strftime('%Y%m%dT%H%M%SZ')
    ics_content += f"""BEGIN:VEVENT
SUMMARY:Dynamic Models
DTSTART:{start_dt}
DTEND:{end_dt}
DTSTAMP:{timestamp}
END:VEVENT
"""

# End the calendar
ics_content += "END:VCALENDAR"

# Save the content to a file
with open("schedule.ics", "w", encoding="utf-8") as file:
    file.write(ics_content)

print("ICS file 'schedule.ics' created successfully.")
