from huggingface_hub import InferenceClient
from loguru import logger

import prompt_templates


def completion(
    client: InferenceClient,
    messages: list[dict],
    max_tokens: int = 1000,
    temperature: float = 0.2,
) -> dict:
    """Returns the next message using a chat completion.

    Args:
        client: The inference client.
        messages: A list of messages.
        max_token: The maximum number of tokens allowed in the response 75 words approximately equals 100 tokens.
        temperature: Controls randomness of the generations between [0, 2]. Lower values ensure less random completions.
    """
    output = client.chat_completion(
        messages, temperature=temperature, max_tokens=max_tokens
    )
    choices = output.choices
    choice = choices[0]
    message = choice.message
    message = {"role": message.role, "content": message.content}
    return message


def extract(client: InferenceClient, text: str, data_points: dict) -> dict:
    content = prompt_templates.render(
        prompt_templates.extract, text=text, data_points=data_points
    )
    messages = [{"role": "user", "content": content}]
    message = completion(client=client, messages=messages)
    logger.debug(f"{message = }")
