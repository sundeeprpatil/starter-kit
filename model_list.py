#curl -L   -H "Accept: application/vnd.github+json"   -H "Authorization: Bearer <token>"   -H "X-GitHub-Api-Version: 2026-03-10"   https://models.github.ai/catalog/models

import requests
import os 
headers = {
    "Authorization": f"Bearer {os.environ['GITHUB_KEY']}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10"
}

resp = requests.get(
    "https://models.github.ai/catalog/models",
    headers=headers
)
import json
models = json.loads(resp.content)

import pandas as pd
pd.DataFrame(models)



