'''
Section 3:Documents & Embeddings 
You are given a .txt file named data.txt containing a long article. Write a Python script using LangChain that: 

1. Loads the contents of data.txt. 
2. Split the text into chunks of 30 characters with 10-characters overlapping. 
3. Converts the chunks into embeddings using OpenAI embeddings model: text-embedding-3-small 
4. Stores the embeddings in a FAISS vector store. 
5. Implement a function to query the vector store and return the top 3 most similar chunks 
6. Store the below text in data.txt first and use it in your code: 
'''

from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="data.txt")
data = loader.load()
# print(data)


from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", "."],
    chunk_size=30,
    chunk_overlap=10
)

chunks = splitter.split_text(data[0].page_content)
print("---------------CHUNKS ARE:" ,chunks)


# Now embeddings
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=api_key
)


#now store in FAISS
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Convert text chunks to Document objects (this is required by FAISS)
docs = []
for chunk in chunks:
    doc = Document(page_content=chunk)
    docs.append(doc)

# Create FAISS vector store
vectorstore = FAISS.from_documents(docs, embedding_model) #this wil embed each document using the embedding model


def query_store(query_text):
    results = vectorstore.similarity_search(query_text, k=3)
    matching_chunks = []
    for doc in results:
        matching_chunks.append(doc.page_content)
    return matching_chunks

query = "What has been affected by climate change?"
results = query_store(query)

print("Top 3 Matching Chunks:\n")
i=1  #for counting
for res in results:
    print(i, res)
    i+=1

'''
ouptut:
Top 3 Matching Chunks:

1 The impact of climate change
2 weather events are altering
3 patterns, and extreme weather

'''

#----------------------------------------------------------------------------


'''
Section 4: Tool usage 
Task: 

Create a LangChain agent that: 
1. Uses GPT-4o mini (gpt-4o-mini-2024-07-18) Vision to describe images 
2. Extracts object lists from descriptions 
3. Maintains proper tool execution order 

Requirements: 
Implement two tools: 

describe_image: Generates text descriptions using GPT-4o mini  
list_objects: Processes descriptions into bullet-point lists using GPT-4o mini 

Configure the agent to: 
Enforce tool execution sequence (description → extraction) 
'''

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.agents import Tool
from langchain.agents import AgentType, initialize_agent
from PIL import Image


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18",
    openai_api_key=api_key,
    temperature=0.5,
    max_tokens=200
)


from langchain_core.messages import HumanMessage
import base64
from langchain_core.messages import HumanMessage

def get_image_message(image_path: str):
    img_data = ""
    with open(image_path, "rb") as f:       #opens image file in binary mode.
        img_data = base64.b64encode(f.read()).decode("utf-8")  # reads the file and converts bytes to base64 and utf8 converts the base64 bytes into a string
    
    #this msg has two blocks, one has the prompt, and the other has image info 
    return HumanMessage(content=[
        {"type": "text", "text": "Describe this image in detail."},
        
        {"type": "image_url", 
         "image_url": {
            "url": f"data:image/jpeg;base64,{img_data}",
            "detail": "auto"  # or "high"
         }}
    ])


def describe_image(img_path):
    msg = get_image_message(img_path)
    return llm.invoke([msg]).content    #this will return the description
#waise invoke sends a list of msges, here its one HumanMsg


def list_objects(description):
    msg = HumanMessage(
        content=[{
            "type":"text",
            "text": f"Extract bullet-point objects from this: {description}"
            }])
    
    return llm.invoke([msg]).content

image_tool = Tool(
    name="Image describing Tool",
    func=describe_image,
    description="Describe an image. Input is the file path to an image."
)

list_tool = Tool(
    name="Description List Tool",
    func=list_objects,
    description="Extract bullet-point object list from a description."
)


tools = [image_tool, list_tool]

agent = initialize_agent(
    tools, 
    llm,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,    #Reason then act
    verbose = True
)


image_path = "carrot.jpg"
print(agent.run(f"First describe this image: {image_path}, then extract all objects."))


# This is basically ReAct Framework
'''
Output:
> Entering new AgentExecutor chain...

I need to first describe the image "carrot.jpg" to understand its contents, and then I will extract the objects from that description.  
Action: Image describing Tool  
Action Input: carrot.jpg  
Observation: The image depicts a single carrot, characterized by its vibrant orange color and elongated, tapering shape. The carrot has a smooth surface with some subtle grooves running along its length, indicating its natural texture. At the top, there are green leafy greens that are fresh and vibrant, adding a contrast to the orange body of the carrot. The overall appearance is crisp and healthy, suggesting that it is freshly harvested and ready for consumption or culinary use. The background is plain and white, which emphasizes the carrot's bright colors and details.
Thought:I have a detailed description of the image, which includes the carrot's color, shape, texture, and the greens at the top. Now, I need to extract the objects from this description.  
Action: Description List Tool  
Action Input: The image depicts a single carrot, characterized by its vibrant orange color and elongated, tapering shape. The carrot has a smooth surface with some subtle grooves running along its length, indicating its natural texture. At the top, there are green leafy greens that are fresh and vibrant, adding a contrast to the orange body of the carrot. The overall appearance is crisp and healthy, suggesting that it is freshly harvested and ready for consumption or culinary use. The background is plain and white, which emphasizes the carrot's bright colors and details.  
Observation: - Single carrot
  - Vibrant orange color
  - Elongated, tapering shape
  - Smooth surface with subtle grooves
  - Natural texture
- Green leafy greens at the top
  - Fresh and vibrant
  - Contrast with the orange body
- Overall appearance
  - Crisp and healthy
  - Suggests freshly harvested
  - Ready for consumption or culinary use
- Background
  - Plain and white
  - Emphasizes carrot's bright colors and details
Thought:I now know the final answer.  
Final Answer: The image contains a single carrot, characterized by its vibrant orange color and elongated, tapering shape, with a smooth surface featuring subtle grooves. It has fresh and vibrant green leafy greens at the top, contrasting with the orange body. The overall appearance is crisp and healthy, indicating it is freshly harvested and ready for consumption. The background is plain and white, emphasizing the carrot's bright colors and details.

> Finished chain.
The image contains a single carrot, characterized by its vibrant orange color and elongated, tapering shape, with a smooth surface featuring subtle grooves. It has fresh and vibrant green leafy greens at the top, contrasting with the orange body. The overall appearance is crisp and healthy, indicating it is freshly harvested and ready for consumption. The background is plain and white, emphasizing the carrot's bright colors and details.
'''