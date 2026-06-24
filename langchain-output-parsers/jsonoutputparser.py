import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# Gemini model use karein
model = ChatGoogleGenerativeAI( model="gemini-2.5-flash")

# 1. Parser define karein
parser = JsonOutputParser()

# 2. Template mein parser ke instructions add karein
template = PromptTemplate(
    template='Give me 5 facts about {topic}. \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# 3. Chain define karein
chain = template | model | parser

# 4. Invoke
result = chain.invoke({'topic': 'black hole'})
print(result)

