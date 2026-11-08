# Privacy and publication boundaries

Only newly written documentation, public feed URLs and empty-key examples are published. No device snapshot is included.

Never commit live `settings.reader.lua`, `settings/assistant.lua`, WeRead session state, browser data, authorization cookies, API keys, credentials, SSH keys, device serials, private network addresses, personal books, reading history, highlights, SQLite databases, screenshots, backups or crash logs.

`.gitignore` reduces accidental additions; it does not sanitize files, protect forced additions, or remove existing Git history. Run the publication checks and inspect the exact staged diff before every push:

```sh
python3 scripts/check-publication.py
# Optional additional scanner; installed separately:
gitleaks dir . --redact --no-banner
git diff --cached --stat
git diff --cached
```

The checker is intentionally conservative and only covers common patterns and permitted artifact types. No scanner proves that arbitrary content has no privacy risk. Do not suppress a finding without inspecting the file locally. Avoid printing real secrets into terminal transcripts or public issue reports.

API values in examples are empty. Enter credentials on the device, or in a private file outside the checkout. Keep device backups outside this repository. Scan only the clean publication checkout, not a directory of private backups.

If a credential is accidentally published: revoke/rotate it first, then remove the file and coordinate Git-history cleanup. Merely deleting the latest version is insufficient.

For public issues, share the smallest redacted error excerpt. Never attach raw device logs or configuration exports.
