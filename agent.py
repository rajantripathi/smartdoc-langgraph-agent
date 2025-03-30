from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"   

def get_llama_agent():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe


def get_llama_agent():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe
