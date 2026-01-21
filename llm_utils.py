# ---------------- llm_utils.py ----------------
import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




def run_prompt(prompt: str, content: str, max_tokens: int = 1500) -> str:
response = client.chat.completions.create(
model="gpt-4o",
messages=[
{"role": "system", "content": "You are a helpful research assistant."},
{"role": "user", "content": f"{prompt}\n\n{content}"},
],
max_tokens=max_tokens,
)
return response.choices[0].message.content