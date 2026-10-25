# Publishing promptstudio on GitHub

Use this description in the repository's **About** section:

> Local AI prompt editor for image and video models. Windows desktop app with Ollama, 43 model guides, 258 presets, and English/Spanish UI.

Suggested topics: `prompt-editor`, `ollama`, `local-ai`, `desktop-app`, `windows`, `python`, `react` and `fastapi`.

## Upload the source

Create an empty GitHub repository without generating another README or license. Before committing, check your Git author name and email, including existing history. Use a GitHub noreply address if you do not want to publish a personal email. From the project root:

```powershell
git status
git add .
git diff --cached --stat
git diff --cached --check
git commit -m "Initial release of promptstudio"
```

Configure `origin` with your repository URL, verify it with `git remote -v`, then run:

```powershell
git push -u origin main
```

The ignore rules exclude local settings, databases, logs, environments, editor settings, build output, archives and experiments. Keep `frontend/package-lock.json` and `recursos/PS.png` in version control. Publish from Git; do not upload the whole working folder, which can contain ignored private files. Never include `.git`, `.env`, `data`, `.venv` or `node_modules` in a source archive.

## Publish a Windows download

After the checks pass, build locally with `scripts/empaquetar_windows.ps1` or run **Build Windows executable** in the Actions tab. The manual workflow produces an artifact; it does not create a public release.

Create a `v1.0.0` release and attach `promptstudio.exe` and `SHA256SUMS.txt`. GitHub supplies source archives from the tag. Describe the Windows, WebView2 and Ollama requirements in the release notes. The executable is unsigned; do not claim code signing or automatic updates.

The **Checks** workflow runs Python tests with mocked inference and compiles the frontend. Neither workflow downloads model weights or generates prompts.
