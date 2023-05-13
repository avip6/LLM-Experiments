"""
This code provides a few simple examples of how to use large language models (LLMs) using Langchain.

LLMs are a type of artificial intelligence (AI) that can generate text, translate languages, write different kinds of content, and answer user's questions in an informative way.

* **Text generation:** This example shows how to use an LLM to generate a name of a child.
* **Prompt and User inputs:** Prompts are an important building block of LLM applications. This extends the previous text generation with prompts.

"""

import os
from dotenv import load_dotenv                              # to open env files
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate                # for prompting
from langchain.chains import LLMChain

load_dotenv()

# if you want to check if the API key is loaded
# print(os.getenv("OPENAI_API_KEY"))


def simple_text_prediction():
    llm = OpenAI(temperature=0.8)
    text = "What is a good name for a baby boy in Australia?"
    return llm(text)


def introduction_to_prompt():
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["country"],
        template="What is a good name for a baby boy in {country}?",
    )
    # prompt.format(country="China")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run("Australia")


# example 1:
print(simple_text_prediction())

# example 2: Extend with prompt
print(introduction_to_prompt())
