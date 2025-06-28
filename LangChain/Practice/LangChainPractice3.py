'''
Concept of RAG: Why it's needed, how it improves LLM outputs. 
Vector Databases (Conceptual): Understanding how information is stored and retrieved. 
 
'''


# Retrieveal Augmented Generation

from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="sherlock.txt")
data = loader.load()
# print(data)


from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", "."],
    chunk_size=500,
    chunk_overlap=50
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

query = "the woman"
results = query_store(query)

print("Top 3 Matching Chunks:\n")
i=1  #for counting
for res in results:
    print(i, res)
    i+=1

'''
output:
Top 3 Matching Chunks:

1 mental results. Grit in a sensitive instrument, or a crack in one of
     his own high-power lenses, would not be more disturbing than a strong
     emotion in a nature such as his. And yet there was but one woman to
     him, and that woman was the late Irene Adler, of dubious and
     questionable memory.

2 To Sherlock Holmes she is always the woman. I have seldom heard him
     mention her under any other name. In his eyes she eclipses and
     predominates the whole of her sex. It was not that he felt any
     emotion akin to love for Irene Adler. All emotions, and that one
     particularly, were abhorrent to his cold, precise but admirably
     balanced mind. He was, I take it, the most perfect reasoning and
     observing machine that the world has seen, but as a lover he would

3 "My dear Holmes," said I, "this is too much. You would certainly have
     been burned, had you lived a few centuries ago. It is true that I had
     a country walk on Thursday and came home in a dreadful mess, but as I
     have changed my clothes I can't imagine how you deduce it. As to Mary
     Jane, she is incorrigible, and my wife has given her notice, but
     there, again, I fail to see how you work it out."

     He chuckled to himself and rubbed his long, nervous hands together.
'''



'''
Vecotr Index:

A vector index is a specialized data structure designed to efficiently store and retrieve vector embeddings

While:


'''

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key= api_key,
    temperature=0.5)

from langchain.agents import Tool
from langchain.agents import AgentType, initialize_agent, load_tools


tools = load_tools(["wikipedia"], llm =llm)

agent = initialize_agent(
    tools, 
    llm,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,    #Reason then act
    verbose = True
)

print(agent.run("Who made facebook and why?"))
'''
ouput:
> Entering new AgentExecutor chain...
Action: wikipedia
Action Input: Facebook
Observation: Page: Facebook
Summary: Facebook is a social media and social networking service owned by the American technology conglomerate Meta. Created in 2004 by Mark Zuckerberg with four other Harvard College students and roommates, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students. Membership was initially limited to Harvard students, gradually expanding to other North American universities. 
Since 2006, Facebook allows everyone to register from 13 years old, except in the case of a handful of nations, where the age requirement is 14 years. As of December 2023, Facebook claimed almost 3.07 billion monthly active users worldwide. As of November 2024, Facebook ranked as the third-most-visited website in the world, with 23% of its traffic coming from the United States. It was the most downloaded mobile app of the 2010s.
Facebook can be accessed from devices with Internet connectivity, such as personal computers, tablets and smartphones. After registering, users can create a profile revealing personal information about themselves. They can post text, photos and multimedia which are shared with any other users who have agreed to be their friend or, with different privacy settings, publicly. Users can also communicate directly with each other with Messenger, edit messages (within 15 minutes after sending), join common-interest groups, and receive notifications on the activities of their Facebook friends and the pages they follow.
Facebook has often been criticized over issues such as user privacy (as with the Facebook–Cambridge Analytica data scandal), political manipulation (as with the 2016 U.S. elections) and mass surveillance. The company has also been subject to criticism over its psychological effects such as addiction and low self-esteem, and over content such as fake news, conspiracy theories, copyright infringement, and hate speech. Commentators have accused Facebook of willingly facilitating the spread of such content, as well as exaggerating its number of users to appeal to advertisers.

Page: Facebook Reels
Summary: Facebook Reels or Reels on Facebook is a short-form video-sharing platform complete with music, audio and artificial effects, offered by Facebook, an online social networking service owned by the American company Meta Platforms. Similar to Facebook's main service, the platform hosts user-generated content, but it only allows for pieces to be 90 seconds long and have a 9:16 aspect ratio.

Page: Meta Platforms
Summary: Meta Platforms, Inc. is an American multinational technology company headquartered in Menlo Park, California. Meta owns and operates several prominent social media platforms and communication services, including Facebook, Instagram, Threads, Messenger and WhatsApp. The company also operates an advertising network for its own sites and third parties; as of 2023, advertising accounted for 97.8 percent of its total revenue.
The company was originally established in 2004 as TheFacebook, Inc., and was renamed Facebook, Inc. in 2005. In 2021, it rebranded as Meta Platforms, Inc. to reflect a strategic shift toward developing the metaverse—an interconnected digital ecosystem spanning virtual and augmented reality technologies.
Meta is considered one of the Big Five American technology companies, alongside Alphabet (Google), Amazon, Apple, and Microsoft. In 2023, itSummary: Meta Platforms, Inc. is an American multinational technology company headquartered in Menlo Park, California. Meta owns and operates several prominent social media platforms and communication services, including Facebook, Instagram, Threads, Messenger and WhatsApp. The company also operates an advertising network for its own sites and third parties; as of 2023, advertising accounted for 97.8 percent of its total revenue.
The company was originally established in 2004 as TheFacebook, Inc., and was renamed Facebook, Inc. in 2005. In 2021, it rebranded as Meta Platforms, Inc. to reflect a strategic shift toward developing the metaverse—an interconnected digital ecosystem spanning virtual and augmented reality technologies.
Meta is considered one of the Big Five American technology companies, alongside Alphabet (Google), Amazon, Apple, and Microsoft. In 2023, itThe company was originally established in 2004 as TheFacebook, Inc., and was renamed Facebook, Inc. in 2005. In 2021, it rebranded as Meta Platforms, Inc. to reflect a strategic shift toward developing the metaverse—an interconnected digital ecosystem spanning virtual and augmented reality technologies.
Meta is considered one of the Big Five American technology companies, alongside Alphabet (Google), Amazon, Apple, and Microsoft. In 2023, ited reality technologies.
Meta is considered one of the Big Five American technology companies, alongside Alphabet (Google), Amazon, Apple, and Microsoft. In 2023, itMeta is considered one of the Big Five American technology companies, alongside Alphabet (Google), Amazon, Apple, and Microsoft. In 2023, it was ranked 31st on the Forbes Global 2000 list of the world's largest public companies. As of 2022, it was the world's third-largest spender on research and development, with R&D expenses totaling US$35.3 billion.
Thought:Final Answer: Facebook was created in 2004 by Mark Zuckerberg with four other Harvard College students and roommates: Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes. It was initially created as a "face book" directory for American university students, starting with Harvard students and then expanding to other North American universities.

> Finished chain.
Facebook was created in 2004 by Mark Zuckerberg with four other Harvard College students and roommates: Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes. It was initially created as a "face book" directory for American university students, starting with Harvard students and then expanding to other North American universities.
'''