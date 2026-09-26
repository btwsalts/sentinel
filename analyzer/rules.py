from collections import Counter
from datetime import datetime, timedelta

def _parse_time(value):
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None

def analyze_events(events):
    alerts = []
    failed = [e for e in events if "failed login" in e["message"].lower() and e.get("ip")]
    by_ip = {}
    for event in failed:
        by_ip.setdefault(event["ip"], []).append(event)

    for ip, attempts in by_ip.items():
        times = [_parse_time(e["timestamp"]) for e in attempts]
        times = [t for t in times if t]
        for index, current in enumerate(times):
            window = [t for t in times[index:] if t - current <= timedelta(seconds=60)]
            if len(window) >= 5:
                alerts.append({
                    "type": "Possible Brute Force",
                    "severity": "HIGH",
                    "ip": ip,
                    "count": len(window),
                    "message": f"{len(window)} failed login attempts from {ip} within 60 seconds.",
                    "timestamp": current.isoformat(),
                })
                break

    errors = Counter(e.get("ip") for e in events if e["level"] in {"ERROR", "CRITICAL"} and e.get("ip"))
    for ip, count in errors.items():
        if count >= 3:
            alerts.append({
                "type": "Repeated Server Errors",
                "severity": "MEDIUM",
                "ip": ip,
                "count": count,
                "message": f"{count} error-level events observed from {ip}.",
                "timestamp": next(e["timestamp"] for e in events if e.get("ip") == ip),
            })
    return alerts
