import logging
import re
import time
import sys
from pathlib import Path

import requests

DEFAULT_OLLAMA_URL = "http://localhost:11434/"
DEFAULT_MODEL = "gemma4:e2b-mlx"
DEFAULT_TARGET_PATH = Path("tmp.md")

DEFAULT_PROMPT = "Build a Python script to print the text 'Hello world!'."
DEFAULT_TIMEOUT_IN_SECONDS = 3600

_BASE_APP_PATH = Path(__file__).parent.absolute()
_IS_MACOS = sys.platform == "darwin"

_log = logging.getLogger("demo")

def main():
    logging.basicConfig(level=logging.INFO)
    target_folder_path = _BASE_APP_PATH / "generated"
    target_folder_path.mkdir(exist_ok=True)
    prompt = prompt_for_token_cost_calculator()
    print(f"Model\tTokens per second\tTokens\tTime in seconds")

    for model in [
        "gemma4:e2b",
        "gemma4:e4b",
        # "gemma4:31b",
        # "qwen3.8:27b",
    ]:
        target_path = target_folder_path / f"{cleaned_name(model)}-demo-app.md"
        generate_target_code(model=model, prompt=prompt, markdown_target_path=target_path)


def prompt_for_token_cost_calculator() -> str:
    prompt_path = _BASE_APP_PATH / "prompt-for-token-cost-calculator.md"
    _log.info("Loading prompt from %s", prompt_path)
    return prompt_path.read_text()


def generate_target_code(
    *,
    prompt: str = DEFAULT_PROMPT,
    model: str = DEFAULT_MODEL,
    markdown_target_path: Path | str = DEFAULT_TARGET_PATH,
) -> None:
    markdown_target_path = Path(markdown_target_path)
    start_time = time.perf_counter()

    if _IS_MACOS and not model.endswith("-mlx"):
        # TODO: Only switch to MLX if the model is available.
        model += "-mlx"

    ollama_generate_url = DEFAULT_OLLAMA_URL + "/api/generate"

    _log.info("Processing prompt with model %s with Ollama at %s", model, ollama_generate_url)
    response = requests.post(
        ollama_generate_url,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
    )
    response.raise_for_status()

    elapsed_seconds = time.perf_counter() - start_time
    result = response.json()

    markdown_response = result.get("response", "")
    _log.info("Writing result to: %s", markdown_target_path)
    markdown_target_path.write_text(markdown_response, encoding="utf-8")

    prompt_token_count = result.get("prompt_eval_count", 0)
    response_token_count = result.get("eval_count", 0)
    token_count = prompt_token_count + response_token_count
    token_count_per_second = token_count / elapsed_seconds

    _log.info(f"Performance with model {model}: {token_count_per_second:.1f} tokens per seconds with {token_count} tokens in {elapsed_seconds:.2f} seconds")
    print(f"{cleaned_name(model)}\t{token_count_per_second:.1f}\t{token_count}\t{elapsed_seconds:.2f}")

    write_first_source_block(markdown_response, markdown_target_path)

def cleaned_name(name) -> str:
    # TODO Preserve only characters that are A-Z, 0-9, underscore (_) or dot (.).
    return name.replace(":", "-").replace("/", "-").replace("\\", "-").replace(";", "-")


def write_first_source_block(markdown: str, markdown_path: Path) -> Path | None:
    """
    Extract the first fenced source code block with a language marker from markdown
    and write it to target_path with the suffix changed to the language marker.

    Example:
        ```python
        print("hello")
        ```

    If target_path is Path("output.txt"), this writes to Path("output.python").
    """
    # TODO Review and clean up slop-coded function.
    match = re.search(
        r"```([A-Za-z0-9_-]+)[^\n]*\n(.*?)```",
        markdown,
        flags=re.DOTALL,
    )

    if match is None:
        _log.warning("Cannot find source code block, skipping %s", markdown_path)
        return None

    language = match.group(1)
    source_code = match.group(2)

    source_code_target_path = markdown_path.with_suffix(f".{language}")
    source_code_target_path.write_text(source_code, encoding="utf-8")

    return source_code_target_path

if __name__ == "__main__":
    main()