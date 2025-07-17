import win32evtlog
import datetime
import sys
import ctypes

def get_first_login():
    server = 'localhost'
    logtype = 'Security'
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    now = datetime.datetime.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)

    events = []
    hand = win32evtlog.OpenEventLog(server, logtype)
    try:
        while True:
            records = win32evtlog.ReadEventLog(hand, flags, 0)
            if not records:
                break
            for event in records:
                if event.EventID == 4624:
                    timestamp = event.TimeGenerated
                    if timestamp < today:
                        break
                    events.append(timestamp)
            else:
                continue
            break
    finally:
        win32evtlog.CloseEventLog(hand) 

    if events:
        return min(events)

def make_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        is_admin = False

    if not is_admin:
        # Alle Startargumente korrekt zusammensetzen (für Leerzeichen etc.)
        params = ' '.join([f'"{x}"' if ' ' in x else x for x in sys.argv])
        rc = ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        if int(rc) <= 32:
            sys.exit(1)
        sys.exit(0)
