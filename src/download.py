import os

from huggingface_hub import hf_hub_download
from loguru import logger

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

model_id = "lmsys/fastchat-t5-3b-v1.0"

filenames = [
    "pytorch_model.bin",
    "added_tokens.json",
    "config.json",
    "generation_config.json",
    "special_tokens_map.json",
    "spiece.model",
    "tokenizer_config.json",
]

for filename in filenames:
    downloaded_model_path = hf_hub_download(
        repo_id=model_id, filename=filename, token=HUGGING_FACE_API_KEY
    )
    logger.debug(f"{downloaded_model_path = }")
