#!/usr/bin/env python3
"""Check publication candidates without echoing matched private values."""
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
paths = subprocess.check_output(
    ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
    cwd=ROOT,
).decode().split('\0')
checks = {
    'personal filesystem path': re.compile(r'/(?:Users|home)/[^\s/]+/'),
    'private network address': re.compile(r'\b(?:192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b'),
    'device serial': re.compile(r'\bG[A-Z0-9]{15}\b'),
    'private key': re.compile(r'-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----'),
    'access token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,})\b'),
    'nonempty credential field': re.compile(r'''["'](?:api_key|token|password|secret|authorization)["']\s*[:=]\s*["']([^"']+)["']''', re.I),
}
issues = []
for name in sorted(set(paths) - {''}):
    p = ROOT / name
    allowed = name in {'README.md', 'SECURITY.md', 'LICENSE', '.gitignore'} or (
        name.startswith(('docs/', 'config/', 'scripts/')) and p.suffix in {'.md', '.lua', '.json', '.py'}
    )
    if not allowed or p.is_symlink():
        issues.append(f'{name}: unexpected publication artifact')
        continue
    try:
        data = p.read_text(encoding='utf-8')
    except (UnicodeError, OSError):
        issues.append(f'{name}: non-text or unreadable artifact')
        continue
    if p.stat().st_size > 100_000:
        issues.append(f'{name}: unexpectedly large artifact')
    for label, pattern in checks.items():
        for match in pattern.finditer(data):
            line = data.count('\n', 0, match.start()) + 1
            issues.append(f'{name}:{line}: {label}')
    if p.suffix == '.json':
        try:
            json.loads(data)
        except ValueError:
            issues.append(f'{name}: invalid JSON')
if issues:
    print('\n'.join(issues), file=sys.stderr)
    sys.exit(1)
print(f'Publication policy check passed: {len(set(paths) - {""})} text files')
