'''
TODO:
Documents & Embeddings: Basic text loading, splitting, and vector stores (conceptual understanding). 

Tools: why tools are used and how to use them? 

Understand the difference between zero shot, one short and few short prompting
'''

'''
Flow of Data is like: Load Data - > Split Data -> Create Embeddings -> Store Vectors
Loaders: Loaders help us in fetching files/documents
sample segment: 
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", "."],
    chunk_size=1000,
    chunk_overlap=200
)
Recursive Character Text Splitter can be used to split the input into smaller chunks

Embeddings:
Used to convert each chunk of text into a numerical vector

Vector Store:
    the embeddings are then stored into vector stores.
    They are basically fast and effiecent vector/embeddings storing db's
'''

# TODO  What was the | pipe operator

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key= api_key,
    temperature=0.5)

my_examples = [
    {
        "text": "The product is terrible",
        "sentiment" : "Negative"
    },
    {
        "text": "Super helpful, worth it",
        "sentiment": "Positive"
    }
]

ex_prompt = PromptTemplate(
    input_variables=["text", "sentiment"],
    template= "Statement : {text}. Sentiment: {sentiment}"
)

f_prompt = FewShotPromptTemplate(
    examples = my_examples,
    example_prompt = ex_prompt,
    suffix = "Question: {input}",
    input_variables = ["input"]
)

final_prompt = f_prompt.format(input="I Havent opened the package yet")
# print("THIS", final_prompt)

response = llm.invoke(final_prompt)
print(response)

'''
output: Neutral
'''


# TOOLS:

from langchain.agents import Tool
from langchain.agents import AgentType, initialize_agent, load_tools

def multiply(a: int, b: int=1) -> int:
   """Multiply two numbers"""
   return a * b

mult_tool = Tool(
    name="Multiplication Tool",
    func = multiply,
    description="Useful for multiplying two integers. Input should be two integers separated by a comma. Example: 3, 5"
)

tools1 = load_tools(["wikipedia"], llm =llm)
# tools = load_tools(["wikipedia", multiply], llm =llm)

tools2 = [mult_tool]

tools = tools1 + tools2

agent = initialize_agent(
    tools, 
    llm,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,    #Reason then act
    verbose = True
)

print(agent.run("Whats elon musks age in 2025"))
'''
ouptut:
Elon Musk was born on June 28, 1971. In 2025, he will be 54 years old (turning 54 on June 28, 2025).
'''


print(agent.run("mutliply 500 and 2341"))
'''
> Entering new AgentExecutor chain...
Action: Multiplication Tool     <------------yahan, it decides I will use the mul tool
Action Input: 500, 2341   
Observation: 500, 2341
Thought:I now know the final answer
Final Answer: 1170500

> Finished chain.
1170500
'''