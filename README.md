# github-clone-all
Very basic and [bodged](https://www.youtube.com/watch?v=lIFE7h3m40U) together Python script to clone --bare all of your GitHub scripts and Gists. Cloning is done using HTTPS and not SSH.

## Quck start
1. Setup Git on local machine.
2. Install dependencies (`pip install -r requirements.txt`)
3. Copy `.env.example` to `.env`.
4. Add your own values to `.env`.
5. Run `github-clone-all.py` script (`python github-clone-all.py`).
6. Profit?

## Output file structure
```
output_dir/
├── 2022-01-07/
│   ├── repositories/
│   │   ├── repo1/
│   │   │   └── file
│   │   └── repo2/
│   │       └── file
│   └── gists/
│       ├── gist1/
│       │   └── file
│       └── gist2/
│           └── file
└── 2022-01-08/
    ├── repositories/
    │   ├── repo1/
    │   │   └── file
    │   └── repo2/
    │       └── file
    └── gists/
        ├── gist1/
        │   └── file
        └── gist2/
            └── file
```

## Might add in the future
* Support for GitHub LFS.
* Support for unlisted Gists.
