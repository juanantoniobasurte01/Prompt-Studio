# Local AI models

Place single-file `.gguf` language models in this folder. In promptstudio, open **Settings → AI engine → Refresh**, select the file, give it a name and click **Import into Ollama**. Then select the imported engine from the installed-model list.

Use an instruction/chat model supported by your installed Ollama version. Importing registers the weights in Ollama; it does not generate text. Ollama may keep another copy of the weights, so allow enough disk space. Files split across several GGUF shards must be imported with Ollama outside this app; they can then be selected normally.

The folder is `ai-models` beside the EXE in a desktop distribution, or at the project root when running from source. `PROMPT_STUDIO_MODELS_DIR` can point to another writable folder. Model weights are excluded from Git and the executable.

See [Ollama's import documentation](https://docs.ollama.com/import).
