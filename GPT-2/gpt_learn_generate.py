import gpt_2_simple as gpt2
import os

model_name = "117M"

if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

