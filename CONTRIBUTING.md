# Contributing

For a bug report, include the app version, Windows version, selected profile and steps to reproduce the problem. If a prompt produces the wrong format, include a small example and the expected result. Remove personal information before sharing logs or exported prompts.

For changes to a model guide, link the provider's documentation and identify the model version and endpoint. Keep uncertain capabilities marked as uncertain. Examples from a guide should not become default scene content.

Keep changes focused. Existing presets and field IDs need to remain readable, and new interface text needs both English and Spanish labels.

## Local checks

Install `requirements-dev.txt` in a virtual environment and run:

```text
python -m pytest -q
```

From `frontend`:

```text
npm ci
npm run build
```

Inference is mocked in tests. Do not add a model download or a live generation requirement to CI.

Build changes should also be checked with `scripts/empaquetar_windows.ps1` on Windows. Temporary experiments belong in `laboratorio/`; remove them before submitting a change. Leave environments, logs, local databases, generated bundles and EXEs out of commits.
