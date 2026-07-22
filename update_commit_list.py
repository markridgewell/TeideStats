
from pathlib import Path
import json
from datetime import datetime

commits = []

for file in Path('build_times').glob('*.json'):
    with open(file) as f:
        data = json.load(f)['run_data']

    start_time = data['started_at'] if 'started_at' in data else data['created_at']
    end_time = data['completed_at'] if 'completed_at' in data else data['updated_at']
    elapsed_time_s = datetime.fromisoformat(end_time) - datetime.fromisoformat(start_time)

    commits.append({
        'hash': data['head_sha'],
        'created_at': data['created_at'],
        'build_time_s': elapsed_time_s.total_seconds(),
        'display_title': data['display_title']
    })

commits.sort(key=lambda x: x['created_at'])

with open('commits.json', 'w') as f:
    json.dump({'commits': commits}, f, indent=4)
