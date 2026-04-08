"""
openai_client.py — Thin OpenAI API wrapper with retries, timeouts, and env config.
"""

import os
import time
import json
import logging
import urllib.request
import urllib.error
from typing import Any

log = logging.getLogger(__name__)

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"
TIMEOUT = 60
MAX_RETRIES = 3
RETRY_DELAY = 2.0  # seconds, doubled on each retry


def chat(
    messages: list[dict],
    temperature: float = 0.2,
    max_tokens: int = 4096,
) -> str:
    """Send chat messages to OpenAI, return the assistant text."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set.")

    payload = json.dumps({
        "model": OPENAI_MODEL,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": messages,
    }).encode()

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    delay = RETRY_DELAY
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(OPENAI_URL, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = json.loads(resp.read().decode())
                return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            if e.code == 401:
                raise RuntimeError("Invalid OPENAI_API_KEY (401 Unauthorized).") from e
            if e.code == 429:
                log.warning("Rate limit hit (attempt %d). Retrying in %.1fs…", attempt, delay)
            else:
                log.warning("HTTP %d on attempt %d: %s", e.code, attempt, body[:200])
        except TimeoutError:
            log.warning("OpenAI request timed out (attempt %d).", attempt)
        except Exception as e:
            log.warning("Unexpected error on attempt %d: %s", attempt, e)

        if attempt < MAX_RETRIES:
            time.sleep(delay)
            delay *= 2

    raise RuntimeError(f"OpenAI API failed after {MAX_RETRIES} attempts.")
