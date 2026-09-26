import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\S+\s+\S+)\s+"
    r"(?P<level>INFO|WARN|WARNING|ERROR|FAILED|CRITICAL)\s+"
    r"(?P<message>.*?)(?:\s+ip=(?P<ip>[0-9.]+))?$",
    re.IGNORECASE,
)

def parse_log(raw):
    events = []
    for line_number, line in enumerate(raw.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        match = LOG_PATTERN.match(line)
        if not match:
            continue
        data = match.groupdict()
        timestamp = data["timestamp"]
        try:
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").isoformat()
        except ValueError:
            pass
        events.append({
            "line": line_number,
            "timestamp": timestamp,
            "level": data["level"].upper(),
            "message": data["message"].strip(),
            "ip": data.get("ip"),
        })
    return events
