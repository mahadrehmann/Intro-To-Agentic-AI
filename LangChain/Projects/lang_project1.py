'''
Project 1: Local Document Q&A Chatbot 

Objective: Develop a simple RAG-based Q&A chatbot that can answer questions based on the content of a local text file (e.g., a .txt file containing a fictional story, a Wikipedia article, or a policy document). 

Concepts to Apply: 
Document Loading: Read content from a local .txt file. 
Text Splitting/Chunking: Divide the document into smaller, manageable chunks. 
Simulated Embeddings: Use your create_mock_embedding function from Section 1 to generate embeddings for each chunk. 
Vector Store: Use your SimpleVectorStore class to store the chunks and their embeddings. 
Retrieval: Implement the retrieve_top_k method to find relevant chunks based on a user query. 
Prompt Augmentation: Construct an augmented prompt that combines the user's query and the retrieved context. 
Mock LLM: Use your mock_llm_response function to simulate the LLM's answer generation. 
Basic Chat Loop: Implement a simple command-line interface where the user can enter questions, and the chatbot provides answers. 

Core Features: 
Load Document: User specifies a .txt file to load. 
Index Document: The system reads the file, chunks it, generates mock embeddings, and stores them in the vector store. 
User Query Input: Prompt the user to enter a question. 
Retrieve Context: Convert the user's question into a mock embedding, then retrieve the top K relevant chunks from the vector store. 
Generate Response: Augment a prompt with the retrieved context and the user's query, then feed it to the mock LLM. 
Display Answer: Print the mock LLM's response. 
Loop: Allow continuous questioning until the user types 'exit'. 

Example Flow: 
--- Local Document Q&A Chatbot --- 
Enter path to text document (e.g., 'my_story.txt'): [User Input] 
 
Indexing document... Done. 
 
Ask me a question (type 'exit' to quit): 
> [User Question] 
Thinking... 
[Mock LLM Answer based on retrieved context] 
 
Ask me another question (type 'exit' to quit): 
> [User Question] 
... 

'''

# Cosine Code:
import math

def calculate_dot_product(vec1, vec2):
    sum=0
    for v1, v2 in zip(vec1,vec2):
        sum+=v1*v2;
    return sum

def calculate_magnitude(vec):
    res = 0
    for v in vec:
        res+= v**2

    return math.sqrt(res)

def calculate_cosine_similarity(vec1, vec2):
    '''
    Formula ye hai: (vec1 . vec2) / (||vec1|| * ||vec2||)
    '''
    num = calculate_dot_product(vec1, vec2)
    div = calculate_magnitude(vec1) * calculate_magnitude(vec2)

    if div == 0:
        return -1
    else:
        return (num/div)


'''
Document Loading and Chunking (Simple) 
'''
def load_and_split_text(long_text, chunk_size=50):
    chunks = []

    if chunk_size <0:
        print("Size Cant be Negative")
    else:    
        loop = 0
        while 1:
            # print("Loop iteration", loop, "chunks are", chunks)
            if long_text == " ": 
                break

            if chunk_size > len(long_text):
                chunks.append(long_text[:])
                break

            if long_text[chunk_size]== " ":
                chunks.append(long_text[:chunk_size])
                long_text = long_text[chunk_size:]
            else:
                isSpace = long_text[chunk_size] 
                i = chunk_size
                while (1):
                    i = i + 1

                    if i > len(long_text):
                        chunks.append(long_text[:])
                        break

                    isSpace = long_text[i]
                
                    if (isSpace == " "):
                        chunks.append(long_text[:i])
                        long_text = long_text[i:]
                        break
            loop +=1
        
    return chunks            


'''
Indexing Data 
'''
def create_mock_embedding(text): #From Q1.1
    embedding = []

    for char in text:   
        x1 = 1 + ord(char)
        x2 = 1 / x1
        x = 1 - x2
        embedding.append(x)
    return embedding

class SimpleVectorStore:
    def __init__(self, document_id, embedding, original_text):
        tup = tuple((document_id,embedding, original_text))
        self.lis = list()
        self.lis.append(tup)

    def add_document(self, document_id,embedding ,text ):
        tup = tuple(( document_id,  embedding, text))
        self.lis.append(tup)
        # print(self.lis)

    def get_all_embeddings(self):
        embeds =[]
        for id, emb, text in self.lis:
            embeds.append(emb)
        
        return embeds
    
    def get_document_by_id(self, document_id):
        for id, emb, text in self.lis:
            if id == document_id:
                return text
        return "none"    
    
    '''
    Retrieval Step 
    '''
    def retrieve_top_k(self, query_embedding, k=1):
        vals = []
        for id, emb, text in self.lis:
            sim = calculate_cosine_similarity(emb, query_embedding)
            vals.append((id, text, sim))

        
        vals.sort(key=lambda x: x[2], reverse=True)

        final_vals = []

        for node in vals:
            if k==0:
                break
            else:    
                final_vals.append(node)
                k-=1
        return final_vals    


def index_documents(texts, vector_store_instance, embedding_function):
    index = 1
    for chunk in texts:
        vector_store_instance.add_document(index,  embedding_function(chunk), chunk)
        index+=1

'''
Augmenting the Prompt & Full RAG Chain (Conceptual/Mock LLM) 
'''
def augment_prompt(query, retrieved_texts):
    prompt = f"you are a assistant that helps in retriving documents based on similairty. Find {query} in {retrieved_texts}"
    return prompt

def mock_llm_response(prompt, nearest) :
    return f"Based on the provided information, I can answer your question. I am thrilled to announce that your query..... matches with {nearest[0]}"


file_path = input("\nEnter file location: ")
f = open(file_path)
data = f.read()
print(data)
chunks = load_and_split_text(data, 100)
print(chunks)


def run_rag_pipeline(query, vector_store, embedding_func, mock_llm_func, k=1):
    index_documents(chunks, vector_store, embedding_func)

    emb = create_mock_embedding(query)
    nearest = vector_store.retrieve_top_k(emb, 3)
    print("nearest values are:", nearest)
    prompt = augment_prompt(query, nearest[0])
    print("\nAugmented prompt:", prompt)
    prompt = mock_llm_func(prompt, nearest[0])
    return prompt

vec = SimpleVectorStore(0, [], "")

input_var = ""
input_var = input("enter question: ")
while input_var != "exit":

   
# D:\sherlock.txt
    '''
    sample string: 
        To Sherlock Holmes she is always the woman. I have seldom heard him
        mention her under any other nam

    '''
    final = run_rag_pipeline(input_var, vec, create_mock_embedding, mock_llm_response, 2)

    print("\nFinal Response:\n", final)
    input_var = input("\nEnter question: (exit to quit): ")

