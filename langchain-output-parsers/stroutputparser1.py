import os
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]
if "CURL_CA_BUNDLE" in os.environ:
    del os.environ["CURL_CA_BUNDLE"]

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-2.5-flash")

parser = StrOutputParser()

# 3. Prompts define karein
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n {text}',
    input_variables=['text']
)

# 4. Chain banayein (Yeh sabse best practice hai)
# Chain 1: Topic -> Detailed Report
chain1 = template1 | model | parser

# Chain 2: Report -> Summary
chain2 = template2 | model | parser

# 5. Execution
topic = 'black hole'
report = chain1.invoke({'topic': topic})
print(f"--- Detailed Report ---\n{report}\n")

summary = chain2.invoke({'text': report})
print(f"--- Summary ---\n{summary}")