"""
This code provides a few simple examples of how to use large language models (LLMs) using Langchain.

LLMs are a type of artificial intelligence (AI) that can generate text, translate languages, write different kinds of content, and answer user's questions in an informative way.

* **Text generation:** This example shows how to use an LLM to generate a name of a child.
* **Translation:** This example shows how to use an LLM to translate text from one language to another.
* **Summarization:** This example shows how to use an LLM to summarize text.
"""

import os
from dotenv import load_dotenv                              # to open env files
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate                # for prompting

load_dotenv()

# if you want to check if the API key is loaded
# print(os.getenv("OPENAI_API_KEY"))


def simple_text_prediction():
    llm = OpenAI(temperature=0.8)
    text = "What is a good name for a baby boy that has a universal name and appeals to everyone?"
    return llm(text)


print(simple_text_prediction())
