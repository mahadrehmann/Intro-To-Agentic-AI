'''
Section 1: Prompt Templates
Section 1.1
Create a LangChain script that uses ChatPromptTemplate to summarize text with the following requirements:
Use a system message to define the assistant's role: "You are a professional summarization assistant"
Use a human message template that takes {text} as input
Generate a 1-sentence summary that captures the key points
Use OpenAI's chat model (gpt-4o-mini-2024-07-18)
'''

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Here I load the key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18",
    openai_api_key=api_key,
    temperature=0.5,     # Temparature means how creative your model will be. 0 for very safe and 1 for creativity/risks 
    max_tokens=200
)

# Used for creating a template for a list of chat messages
chat = ChatPromptTemplate([
   ("system","You are a professional summarization assistant. You Generate a 1-sentence summary that captures the key points"),
   ("human","{input}")
])

# Use LLMChain to run it
chain = LLMChain(llm=llm, prompt=chat) #We tell the chain our LLM and the prompt template to use

text = "Pakistan, officially the Islamic Republic of Pakistan, is a populous multiethnic country in South Asia with a rich history, diverse geography, and a predominantly Muslim population. Established in 1947 through the partition of British India, it is bordered by India to the east, Afghanistan to the west, Iran to the southwest, and China to the northeast, with a coastline along the Arabian Sea and the Gulf of Oman. The country features varied landscapes, including deserts, plains, and high mountains, and is home to ancient civilizations like the Indus Valley"

output = chain.run(text)  #llm.generate() bhi use hota hai for structured
print(output) 
'''
Ouput:
Pakistan, established in 1947 as a multiethnic Islamic republic in South Asia, is bordered by India, Afghanistan, Iran, and China, features diverse landscapes, and has a rich history that includes ancient civilizations like the Indus Valley.

'''


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Section 1.2
Task:
Using LangChain's FewShotPromptTemplate, create a simple sentiment classifier that:
Learns from examples like (1 positive, 1 negative)
Classifies new text inputs as either "Happy" or "Sad"
Formats the prompt clearly with examples and instructions
Requirements:
Define training examples. Like:
"text": "I got a promotion today!", "label": "Happy"
"text": "My dog passed away", "label": "Sad"
Test your classifier with:
"I failed my exam" (should return "Sad")

Question:
Write the complete Python code to implement this classifier using LangChain's few-shot learning components.
'''
from langchain.prompts.few_shot import FewShotPromptTemplate

sentiments = [
    {
        "text": "I got a promotion today!",
        "label": "Happy"
    },
    {
        "text": "My dog passed away",
        "label": "Sad"
    }
]

sent_prompt = PromptTemplate(
    input_variables=["text", "label"], template="Text: {text}, Label: {label}"
)

# print(sent_prompt.format(**sentiments[0]))

prompt = FewShotPromptTemplate(
    examples=sentiments,
    example_prompt=sent_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)
# print(prompt.format(input="I failed my exam"))

formatted_prompt = prompt.format(input="I failed my exam")

response = llm.invoke(formatted_prompt)
print(response)
print(response.content)

# OR WE could have created a chain to call it 

'''
Output:
content='Label: Sad' additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 3, 'prompt_tokens': 36, 'total_tokens': 39, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_34a54ae93c', 'finish_reason': 'stop', 'logprobs': None} id='run--8ed52978-8352-486b-be2e-279c73514491-0'

Label: Sad
'''



#----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

Section 2: Sequential chains
Section 2.1
Task:
Create a LangChain application that generates creative product names and slogans using sequential chains. Implement a system where:
The first step generates a company name based on a product description
The second step creates a slogan based on the generated company name
Both steps use OpenAI LLMs model (gpt-4o-mini-2024-07-18)

Requirements:
Define two prompt templates:
name_template: Takes {product} as input, outputs company name
Template: "Generate a creative name for a company that makes {product}"
slogan_template: Takes {company_name} as input, outputs slogan
Template: "Create a catchy slogan for this company: {company_name}"

Create two LLM chains:
name_chain with output key "company_name"
slogan_chain with output key "slogan"
Combine chains using SequentialChain and generate an output. Test with:
"eco-friendly water bottles"
(Example output: "AquaGreen Solutions" with slogan "Hydrate Sustainably!")
'''
from langchain.chains import SimpleSequentialChain

name_template = PromptTemplate(
    input_variables=["product"],
    template = "Generate a creative name for a company that makes {product}"
)

slogan_template = PromptTemplate(
    input_variables=["company_name"],
    template = "Create a catchy slogan for this company: {company_name}"
)

name_chain = LLMChain(llm = llm, prompt = name_template)
slogan_chain = LLMChain(llm = llm, prompt = slogan_template)

main_chain = SimpleSequentialChain(chains =[name_chain,slogan_chain], verbose = True)

result = main_chain.run("eco-friendly water bottles")
print(result)
'''
ouput:
> Entering new SimpleSequentialChain chain...

"EcoSip Solutions"

"Drink Green, Live Clean with EcoSip Solutions!"

'''



#----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Section 2.2
You are building an AI assistant for job seekers. Create a SequentialChain that does the following:
Extracts the key responsibilities from a raw job description text.
Identifies the top 3 skills required for the job based on the extracted responsibilities.

Generates a personalized summary for a candidate, assuming their name is "Alex" and they are applying for the job.
Implement this 3-step pipeline using SequentialChain and multiple LLMChains in LangChain.
'''

description_prompt = PromptTemplate(
    input_variables=["job_desc"],
    template="You are an AI assistant for job seekers. Extract the key responsibilities from a raw job description text. Text: {job_desc}"
)

skills_prompt = PromptTemplate(
    input_variables=["responsibilities"],
    template="You are an AI assistant for job seekers. Identify the top 3 skills required for the job based the given responsibilities. Responsibilities: {responsibilities}"
)

personalized_prompt = PromptTemplate(
    input_variables=["skills"],
    template="You are an AI assistant for job seekers. Generate a personalized summary for Alex, for these skills: {skills}  "
)


desc_chain = LLMChain(llm=llm, prompt= description_prompt)
skills_chain = LLMChain(llm=llm, prompt= skills_prompt)
personal_chain = LLMChain(llm=llm, prompt= personalized_prompt)

main_chain = SimpleSequentialChain(chains = [desc_chain, skills_chain,personal_chain], verbose=True)

job_desc = "A Front-End Developer is responsible for building the visual and interactive elements of websites and web applications, ensuring a seamless user experience and optimizing for performance, responsiveness, and cross-browser compatibility. Their role involves translating UI/UX designs into functional code using languages like HTML, CSS, and JavaScript, and often utilizing frameworks such as React, Vue, or Angular."

result = main_chain.run(job_desc)
print(result)

'''
output:

> Entering new SimpleSequentialChain chain...
Key Responsibilities of a Front-End Developer:

1. Build visual and interactive elements of websites and web applications.
2. Ensure a seamless user experience.
3. Optimize performance, responsiveness, and cross-browser compatibility.
4. Translate UI/UX designs into functional code.
5. Utilize languages such as HTML, CSS, and JavaScript.
6. Use frameworks like React, Vue, or Angular.
Based on the responsibilities outlined for a Front-End Developer, the top three skills required for the job are:

1. **Proficiency in HTML, CSS, and JavaScript**: These are the foundational languages for building the structure, style, and interactivity of web applications. A strong grasp of these languages is essential for translating UI/UX designs into functional code.

2. **Experience with Front-End Frameworks (e.g., React, Vue, Angular)**: Familiarity with modern JavaScript frameworks is crucial for creating dynamic and responsive user interfaces efficiently. These frameworks help streamline development processes and enhance performance.      

3. **Understanding of UI/UX Principles**: A solid understanding of user interface and user experience design principles is necessary to ensure a seamless user experience and effectively translate designs into functional code. This includes optimizing for performance and cross-browser compatibility. 

These skills collectively enable a Front-End Developer to build engaging, efficient, and user-friendly web applications.
**Personalized Summary for Alex:**

As a highly skilled Front-End Developer, I possess a strong proficiency in HTML, CSS, and JavaScript, which form the foundation of my ability to construct dynamic and interactive web applications. My expertise in these core languages allows me to effectively translate UI/UX designs into functional, user-friendly code that meets both aesthetic and functional requirements.

I have hands-on experience with modern front-end frameworks such as React, Vue, and Angular, which has significantly enhanced my ability to create responsive user interfaces efficiently. My familiarity with these frameworks not only streamlines the development process but also improves the overall performance of the applications I build.

Additionally, I have a solid understanding of UI/UX principles, which enables me to prioritize user experience in every project. I am adept at optimizing web applications for performance and ensuring cross-browser compatibility, ensuring that users enjoy a seamless experience regardless of their device or browser.

With a passion for creating engaging and efficient web applications, I am excited to leverage my

'''