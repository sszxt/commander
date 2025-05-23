import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch
import shutil
import sys

BASE_MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
LORA_ADAPTER_REPO = os.path.join(os.path.dirname(__file__), "model", "checkpoint-750")
LOCAL_MODEL_DIR = os.path.expanduser("~/.model_cache/commander_model")

def download_and_cache_models():
    if not os.path.exists(LOCAL_MODEL_DIR):
        os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)
        print("Downloading base model...")
        base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_NAME, cache_dir=LOCAL_MODEL_DIR)
        tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME, cache_dir=LOCAL_MODEL_DIR)

        base_model.save_pretrained(LOCAL_MODEL_DIR)
        tokenizer.save_pretrained(LOCAL_MODEL_DIR)

        # Copy LoRA adapter
        lora_target_dir = os.path.join(LOCAL_MODEL_DIR, "lora_adapter")
        print(f"Copying LoRA adapter from {LORA_ADAPTER_REPO} to {lora_target_dir}...")
        shutil.copytree(LORA_ADAPTER_REPO, lora_target_dir)

        print("Models downloaded and cached.")
    else:
        print("Using cached models.")


def load_model():
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME, cache_dir=LOCAL_MODEL_DIR)
    base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_NAME, cache_dir=LOCAL_MODEL_DIR)

    # Load LoRA adapter
    # Correct path to where your LoRA adapter actually is
    lora_path = os.path.join(os.path.dirname(__file__), "model", "checkpoint-750")
    if not os.path.exists(lora_path):
        raise FileNotFoundError(f"LoRA adapter folder not found at '{lora_path}'.")

    model = PeftModel.from_pretrained(base_model, lora_path)
    model.eval()
    return tokenizer, model


def main():
    download_and_cache_models()
    tokenizer, model = load_model()

    # Check if a question was passed via CLI
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_length=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(response)
        return  # Exit immediately after responding

    # Fallback to interactive mode
    print("Terminal AI assistant ready! Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("\n> ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_length=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(response)
