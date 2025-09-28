import json, time
from pathlib import Path
import os

# Use local logs directory instead of /opt/genai-agent/logs
LOG = Path(os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "audit.jsonl"))
LOG.parent.mkdir(parents=True, exist_ok=True)

def audit_log(**kwargs):
    with open(LOG, "a") as f:
        f.write(json.dumps({"ts": time.time(), **kwargs}) + "\n")
