# AI coding Graz: local inference

These are the slides and examples for my talk about local inference at the [#2 AI coding Grazz](https://kommunity.com/ai-coding-graz/events/2-ai-coding-meetup-graz-4361f9ca).

## Setup

1. Install [Ollama](https://ollama.com/). Consider using [homebrew](https://brew.sh/) to easily keep Ollama up to date and run it as a local service.
2. Download the models you want to use. For Linux, run:
   ```bash
   ollama pull gemma4:e2b
   ollama pull gemma4:e4b
   ollama pull gemma4:31b
   ollama pull qwen3.8:27b
   ```
   For macOS, run:
   ```bash
   ollama pull gemma4:e2b-mlx
   ollama pull gemma4:e4b-mlx
   ollama pull gemma4:31b-mlx
   ollama pull qwen3.8:27b-mlx
   ```

To set up the local Python environment:

1. Install [uv](https://docs.astral.sh/uv/).
2. Run:
   ```bash
   uv sync --all-packages
   ```

To run the demo script:

```bash
uv run build_demo_app
```

This script asks various LLMs to build a web app and output some statistics. The app is a single HTML and can be found in `src/demo/generated`. It computes costs of local inference.

## AI disclosure

Some Python functions have been generated with AI. Humans have reviewed all of them. Possible flaws have either been fixed or marked with a `TODO` comment.

## License

[#2 AI coding meetup Graz: Local inference](https://github.com/roskakori/talks) © 2026 by [Thomas Aglassinger](https://roskakori.at) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).