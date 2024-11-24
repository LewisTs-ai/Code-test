from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from huggingface_hub import login
import argparse

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Process a text input.")
    
    # Add an argument for text input
    parser.add_argument('text', type=str, help='The text to be processed')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Access and use the provided text
    login(token="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")
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-3B")
    # Example processing (e.g., counting words)
    text = args.text

    prompt = f"Summarize the following text: {text}"
    summary = pipe(prompt, max_length=150, do_sample=False)[0]['generated_text']
    print("summary:", summary)

if __name__ == "__main__":
    main()
