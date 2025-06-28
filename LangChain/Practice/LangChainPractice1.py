'''
1. Introduction to LangChain: What it is, why use it. 
2. LLMs: Interacting with various LLMs (OpenAI, Hugging Face, etc.). 
3. Prompts: Crafting effective prompts, prompt templates. 
4. Chains: Combining LLMs and prompts, simple sequential chains. 

'''

from dotenv import load_dotenv
import os

# Here i load the key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#now i am creating the LLM model to use
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
   model="gpt-4o-mini-2024-07-18",
   openai_api_key=api_key,
   temperature=0.7,     # Temparature means how creative your model will be. 0 for very safe and 1 for creativity/risks 
   max_tokens=100
)

# TODO ; what is temparature
'''
Controlling Randomness:
Temperature modifies the probability distribution of the next word (or token) predicted by the LLM
'''

# TODO : what are n-grams?

response = llm.predict("Tell me a fun fact about space.")
print(response)
'''
Output:
 A fun fact about space is that a day on Venus is longer than a year on Venus! Venus has an extremely slow rotation on its axis, taking about 243 Earth days to complete one full rotation. In contrast, it takes only about 225 Earth days for Venus to orbit the Sun. This means that a single day on Venus lasts longer than its entire year!
'''

# Templates allow us to have reusable templates with placeholders {value}
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Create a prompt with a variable
prompt_template = PromptTemplate(
   input_variables=["topic"],                        # all the inputs to be used in the template
   template="Give me a short summary about {topic}"  # template prompt    
)

# Use LLMChain to run it
chain = LLMChain(llm=llm, prompt=prompt_template) #We tell the chain our LLM and the prompt template to use

output = chain.run("Peshawar")
print(output) 

#TODO: try these
'''
.apply() when we have a list of inputs and want to get the LLM to generate text for each one
.generate() is similar to apply, except it returns an structured LLMResult 
.predict() when we want to pass inputs as keyword arguments instead of a dictionary
.run() when we want to pass the input as a dictionary and get the raw text output from the LLM.

'''


'''
Ouput:
Peshawar is the capital of Khyber Pakhtunkhwa province in Pakistan and is one of the country's oldest cities, with a rich history that dates back over 2,000 years. It has served as a significant cultural and economic hub due to its strategic location near the Khyber Pass, which connects Pakistan to Afghanistan. The city is known for its diverse population, vibrant bazaars, and historical landmarks, including the Bala Hisar Fort and the Mahabat Khan Mosque. Pesh
'''

from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate

# My first prompt asking topic names
summary_prompt = PromptTemplate.from_template("Suggest 3 important topics for job profile {input}. Give topic only, no details")
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

# My second prompt asking for questionsfrom those topics 
translation_prompt = PromptTemplate.from_template("Give me one interview question from each of these topics: {input}")
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

# Here we combine the 2 chains
sequential_chain = SimpleSequentialChain(chains=[summary_chain, translation_chain], verbose=True) #ouputs intermediate steps for understanding

result = sequential_chain.run("Ai Agents Engineer")
print(result)


'''
Output:


> Entering new SimpleSequentialChain chain...
1. Natural Language Processing (NLP) Techniques  
2. Machine Learning Algorithms and Frameworks  
3. Ethical Considerations in AI Development  
Sure! Here are interview questions from each of the specified topics:

1. **Natural Language Processing (NLP) Techniques**:  
   *Question:* Can you explain the difference between tokenization and lemmatization in NLP, and when you would use each technique?

2. **Machine Learning Algorithms and Frameworks**:  
   *Question:* What is the difference between supervised and unsupervised learning, and can you provide an example of a problem that is best solved using each approach?

3

> Finished chain.
Sure! Here are interview questions from each of the specified topics:

1. **Natural Language Processing (NLP) Techniques**:
   *Question:* Can you explain the difference between tokenization and lemmatization in NLP, and when you would use each technique?

2. **Machine Learning Algorithms and Frameworks**:
   *Question:* What is the difference between supervised and unsupervised learning, and can you provide an example of a problem that is best solved using each approach?

3

'''