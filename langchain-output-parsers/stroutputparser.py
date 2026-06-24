import os
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import PromptTemplate

# 1. Model aur Tokenizer load karein
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", # Agar GPU hai toh automatically use karega
    torch_dtype="auto"
)

# 2. Pipeline setup
pipe = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
    max_new_tokens=500
)

# 3. LangChain LLM wrapper
llm = HuggingFacePipeline(pipeline=pipe)

# 4. Templates define karein
template1 = PromptTemplate(
    template='Write a detailed report on {topic}', 
    input_variables=['topic']
)
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n {text}', 
    input_variables=['text']
)

# 5. Execution Flow
# Prompt 1
prompt1 = template1.invoke({'topic': 'black hole'})
result = llm.invoke(prompt1)
print(f"--- Detailed Report ---\n{result}\n")

# Prompt 2 (Result ko input ki tarah use karein)
prompt2 = template2.invoke({'text': result})
result1 = llm.invoke(prompt2)
print(f"--- Summary ---\n{result1}")