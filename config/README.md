# Example configuration only

These files are references, not full device exports. Back up your live settings privately, exit KOReader and **merge** changes. Never copy the complete device settings back into this Git checkout.

- `rss/`: local accounts plus public feed definitions. Copy the two example files to the RSS plugin directory after removing `.example` from their names, or merge existing entries.
- `rakuyomi/settings.example.json`: merge into the device's `koreader/rakuyomi/settings.json`; source extensions are installed separately through Manage Sources.
- `assistant/assistant.settings.example.lua`: reference for the AI Assistant 1.21 UI-editable provider registry, normally stored as device `koreader/settings/assistant.lua`. Use only for a fresh Assistant setup; merge existing providers instead of overwriting them.
- `assistant/configuration.example.lua`: a valid empty file-provider configuration. UI-added providers are configured separately. Do not copy the upstream sample containing placeholder providers unchanged and assume it is ready to use.

Device `/mnt/us/...` paths refer to the Kindle USB storage, not a private computer home directory. No actual Key, login state or book content belongs in these examples.
