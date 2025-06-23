import json
from jsonschema import validate, ValidationError

from groq import Groq

from helpers.constants import GROQ_API_KEY, LLM_MAX_RETRIES
from helpers.prompts import GOOD_BAD_UGLY_PROMPT
from helpers.schemas import GOOD_BAD_UGLY_SCHEMA


class LLM:
    def __init__(self):
        self.client: Groq = Groq(api_key=GROQ_API_KEY)
        self.max_retries: int = LLM_MAX_RETRIES

    def _call_model(self, message: str) -> str | None:
        
        resp = self.client.chat.completions.create(
            messages=[{"role": "user", "content": GOOD_BAD_UGLY_PROMPT.format(message=message)}],
            model="llama3-70b-8192"
        )
        return resp.choices[0].message.content

    def chat_good_bad_ugly(self, message: str) -> dict | None:
        for attempt in range(1, self.max_retries + 1):
            raw = self._call_model(message)
            if not raw:
                continue

            if isinstance(raw, dict):
                data = raw
            else:
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as e:
                    print(f"Attempt {attempt}: JSON parse error: {e}")
                    continue

            try:
                validate(instance=data, schema=GOOD_BAD_UGLY_SCHEMA)
            except ValidationError as e:
                print(f"Attempt {attempt}: Schema validation error: {e.message}")
                continue

            # Valid format
            return data

        print("Failed to get valid JSON after", self.max_retries, "attempts.")
        return None
