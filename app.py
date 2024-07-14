import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv(find_dotenv())

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"                      # Enable tracing -> Application will get traced when we execute it
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
                                [
                            ("system", "You are a helpful assistant. Please response to the user request only based on the given context"),
                            ("user","Question:{question}\nContext:{context}")
                            ]
)

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

question = "Can you summerize the speech?"
context = """
Drawing from the skills and values he gained during his time at LASS, coupled with the pivotal experiences during university, Rombek embarked on an entrepreneurial journey to address the persisting issues that stem from overgrowth in his hometown of Gulu, Uganda. With determination and resilience, Rombek launched a lawn mowing business in 2020 called Aromaro Compound Service. Its primary services include lawn mowing, compound cleaning, bush clearance, and flower trimming.

The road was not easy, but he persevered. Over time, his business began to thrive, fulfilling one of his primary goals to create employment opportunities for other community members. As his business grew, he went from a single mower to seven and began teaching and employing the once homeless street children.
"""

print(chain.invoke({"question": question, "context": context}))