#!/usr/bin/env python3

import os
import time
import json
import requests
import subprocess
import sys
from dotenv import load_dotenv

scriptDir = os.path.dirname(__file__)

envPath = os.path.join(scriptDir, ".env")
if os.path.isfile(envPath) is False:
    sys.exit("No .env file found, please create one. :)")

load_dotenv(envPath)
outputDir = os.getenv('OUTPUT_DIR')
githubUsername = os.getenv('GITHUB_USERNAME')
githubToken = os.getenv('GITHUB_TOKEN')
currentDate = time.strftime("%Y-%m-%d", time.gmtime())

if os.path.isdir(outputDir) is False:
    sys.exit("Invalid OUTPUT_DIR in .env file.")

headers = {'Authorization': 'token ' + githubToken}

# Get repo URLs.
print("Fetching repo URLs...")
lastPageReached = False
page = 1
repoUrls = []
while lastPageReached is False:
    r = requests.get(f'https://api.github.com/user/repos?type=all&per_page=100&page={page}', headers=headers)
    page += 1
    rJson = r.json()
    if len(r.json()) == 0 or len(r.json()) < 100:
        lastPageReached = True
    for repo in rJson:
        repoUrls.append(repo["clone_url"])

# Get Gist URLs.
print("Fetching Gist URLs...")
lastPageReached = False
page = 1
gistUrls = []
while lastPageReached is False:
    r = requests.get(f'https://api.github.com/users/{githubUsername}/gists?per_page=100&page={page}')
    page += 1
    rJson = r.json()
    if len(r.json()) == 0 or len(r.json()) < 100:
        lastPageReached = True
    for gist in rJson:
        gistUrls.append(gist["git_pull_url"])

saveDir = os.path.join(outputDir, currentDate)
os.mkdir(saveDir)

# Clone repos.
repoDir = os.path.join(saveDir, "repositories")
os.mkdir(repoDir)
for url in repoUrls:
    subprocess.run(f'cd {repoDir}; git clone --bare --recurse-submodules {url}', shell=True)

# Clone gists.
gistDir = os.path.join(saveDir, "gists")
os.mkdir(gistDir)
for url in gistUrls:
    subprocess.run(f'cd {gistDir}; git clone --bare {url}', shell=True)
