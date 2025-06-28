
# TODO: differnce b/w library and framework
'''
libraries are tools we use, while frameworks are structures we build with 
'''


llm = ChatOpenAI(
   model="gpt-4o-mini-2024-07-18",
   openai_api_key=api_key,
   temperature=1,     # Temparature means how creative your model will be. 0 for very safe and 1 for creativity/risks 
   max_tokens=100
)

# TODO  what is temparature
'''
Controls Randomness as it
modifies the probability distribution of the next word predicted by the LLM

This  sentence   is      is 0.9 / the 0.01 / am / mahad  <------ each word has a prob distribution(look it up google)
'''

# TODO : what are n-grams?
'''
They are a sequences of n items from a given text
Mostly used in NLP
Used in statistical language models for prediction and classification
'''


#TODO: try these
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Create a prompt with a variable
prompt_template = PromptTemplate(
   input_variables=["topic"],                        # all the inputs to be used in the template
   template="Give me a short summary about {topic}"  # template prompt    
)

chain = LLMChain(llm=llm, prompt=prompt_template) #We tell the chain our LLM and the prompt template to use
output = chain.run("Peshawar")

'''
run():
Used for: Simple, single input
Takes: A string or a dict

Returns: A string (raw output from the LLM)

output = chain.run("Peshawar")
# or
output = chain.run({"topic": "Peshawar"})



predict()
Used for: Simple, single input like run()
Takes: Keyword arguments
Returns: A string

output = chain.predict(topic="Peshawar")


apply()
Used for: Multiple inputs in a list of dictionaries
Takes: A list of input dictionaries
Returns: A list of outputs (strings)

inputs = [{"topic": "Peshawar"}, {"topic": "Islamabad"}]
outputs = chain.apply(inputs)


generate()
Used for: Like .apply() but you want richer info
Takes: A list of input dictionaries
Returns: LLMResult (structured, includes generations, tokens, etc.)

results = chain.generate([{"topic": "Peshawar"}, {"topic": "Islamabad"}])
print(results.generations[0][0].text)  # Get the output text from the first result

Use if you want more control (e.g. token info, reasoning steps in ReAct, etc)
'''



# TODO  What is | pipe operator

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import Runnable

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18",
    openai_api_key=api_key,
    temperature=0.7,
    max_tokens=100
)

# Create the prompt template
prompt = PromptTemplate.from_template("Give me a funny joke about {topic}")

# Pipe: prompt → LLM
chain = prompt | llm

# Run the chain with input
output = chain.invoke({"topic": "Gardeners"})

print(output)
'''
output:

Why did the gardener plant a light bulb?
Because he wanted to grow a power plant!'
'''

