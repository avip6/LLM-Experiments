"""
Search within contents using large language models (LLMs) and Langchain.

* **Search a document:** How to use LLM to search within a document
* **Search a data dictionary:** Create a data dictionary and search within that.

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
    text = "Act as an executive in charge of accounrting company. What Strategists Should know about Machine learning and Artificial intelligence in general?"
    return llm(text)


# def introduction_to_prompt():
#     llm = OpenAI(temperature=0.9)
#     prompt = PromptTemplate(
#         input_variables=["country"],
#         template="What is a good name for a baby boy in {country}?",
#     )
#     # prompt.format(country="China")
#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain.run("Australia")


# # example 1:
print(simple_text_prediction())

# # example 2: Extend with prompt
# print(introduction_to_prompt())
