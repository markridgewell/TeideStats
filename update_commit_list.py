
from pathlib import Path
import json

commits = []

for file in Path('build_times').glob('*.json'):
    with open(file) as f:
        data = json.load(f)
    commits += [{'hash': data['run_data']['head_sha']}]

with open('commits.json', 'w') as f:
    json.dump({'commits': commits}, f, indent=4)
