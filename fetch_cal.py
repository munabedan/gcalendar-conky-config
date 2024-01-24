import socket
import time
from datetime import datetime
import re
import subprocess



def format_calendar_input(input_text):
    lines = input_text.split('\n')

    current_date = None

    for line in lines:
        # Use regular expression to extract date-time range and event title
        match = re.match(r'(\d{4}-\d{2}-\d{2}:\d{2}:\d{2} - \d{4}-\d{2}-\d{2}:\d{2}:\d{2})\s+(.*)', line)

        # Check if the line has the expected format
        if match:
            date_time_range, event_title = map(str.strip, match.groups())
        else:
            # Handle lines with unexpected format
            # print(f"Skipping line with unexpected format: {line.strip()}")
            continue

        # Parse the start and end dates and times
        start_datetime_str, end_datetime_str = map(str.strip, date_time_range.split(' - '))
        start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d:%H:%M')
        end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%d:%H:%M')

        # Check if the date has changed
        if current_date != start_datetime.date():
            current_date = start_datetime.date()
            print(f'{current_date.strftime("%b %d, %Y")}')  # Bold white text

        # Check if the event is "All Day"
        if start_datetime.time() == end_datetime.time() == datetime.min.time():
            time_range = "All Day"
        else:
            # Format the time range
            time_range = f'{start_datetime.strftime("%I:%M %p")} - {end_datetime.strftime("%I:%M %p")}'  # Bold white text

        # Print the formatted output
        print(f'\t{time_range} ~ {event_title}')  # Bold white text


def run_gcalendar_and_format():
    try:
        # Run the 'gcalendar' command and capture its output
        gcalendar_output = subprocess.check_output(['gcalendar'], text=True, stderr=subprocess.STDOUT)

        # Format the 'gcalendar' output using the existing function
        format_calendar_input(gcalendar_output)

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the command execution
        print(f"Error running 'gcalendar' command: {e.output}")




def wait_for_internet(timeout=300, interval=5):
    """
    Wait for internet connectivity.

    Parameters:
    - timeout: Maximum time (in seconds) to wait for internet connectivity.
    - interval: Time (in seconds) between each retry.

    Returns:
    - True if internet connectivity is established within the timeout.
    - False if the timeout is reached without internet connectivity.
    """
    start_time = time.time()

    while True:
        if is_internet_available():
            return True

        elapsed_time = time.time() - start_time

        if elapsed_time >= timeout:
            return False

        time.sleep(interval)

def is_internet_available():
    try:
        # Try to connect to a well-known host (e.g., Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

# Example usage:
if wait_for_internet():
    # print("Internet connection established!")
    run_gcalendar_and_format()
else:
    print("Timeout reached. No internet connection.")


