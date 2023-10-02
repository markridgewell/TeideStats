
from pathlib import Path
import json

commits = []

for file in Path('build_times').glob('*.json'):
    with open(file) as f:
        data = json.load(f)['run_data']
    commits += [{'hash': data['head_sha'], 'created_at': data['created_at']}]

commits.sort(key=lambda x: x['created_at'])

with open('commits.json', 'w') as f:
    json.dump({'commits': commits}, f, indent=4)
