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
Question 2.1: Write a Python function load_and_split_text(long_text, chunk_size=50). This function should take a long string and split it into chunks of approximately chunk_size characters, ensuring chunks don't cut words in half (simple approach: split by space and combine words until chunk_size is met or exceeded). Return a list of these text chunks. 
'''
def load_and_split_text(long_text, chunk_size=50):
    chunks = []

    if chunk_size <= 0:
        print("Size Cant be Negativeor zero")
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
                    i = i - 1

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

# /////


print(load_and_split_text("thw news has reachd my ears we w forensic ", 0), "\n")                


'''
Question 2.2: Take a sample paragraph (e.g., 200-300 words) about a general topic (like "The history of computers"). Use load_and_split_text to split it into chunks of chunk_size=100. Print each chunk and its length. 
'''

# Sampele Text
the_internet = "The Internet, a technological marvel born from the minds of visionaries, has grown into a global phenomenon that touches every facet of our lives. Its roots trace back to ARPANET’s inception in the 1960s when the revolutionary concept of interconnected computers was born. This early network laid the groundwork for the modern Internet, enabling computers to share data and communicate over vast distances. In the subsequent decades, this technology evolved, leading to the creation of the World Wide Web by Tim Berners-Lee in the late 1980s. Today, the Internet serves as a digital frontier that transcends geographical boundaries. It provides access to a staggering wealth of information, entertainment, and services. From social networking and e-commerce to online education and remote work, its applications are diverse and far-reaching. Moreover, the Internet’s impact on communication cannot be understated, as it has transformed how people interact, fostering connections and collaborations across the globe.However, this technological marvel also presents challenges. The prevalence of misinformation, cybercrimes, and privacy breaches remind us of the Internet’s dual nature. Striking a balance between its advantages and disadvantages is imperative as we navigate this digital landscape."


chunks = load_and_split_text(the_internet, 100)
print(chunks)                


'''
Indexing Data 
Question 2.3: Create a function index_documents(texts, vector_store_instance, embedding_function) that takes a list of text chunks, your SimpleVectorStore instance, and your create_mock_embedding function. It should iterate through the texts, generate an embedding for each using embedding_function, and add them to the vector_store_instance with a unique ID for each chunk. 
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
    Question 2.6: Add a method retrieve_top_k(query_embedding, k=1) to your SimpleVectorStore class. This method should: 
    Calculate the cosine similarity between query_embedding and every embedding stored in the vector store. 
    Return the k (default 1) (document_id, original_text, similarity_score) tuples with the highest similarity scores, sorted in descending order of similarity. 
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
Question 2.4: Take your 200-300 word sample paragraph from Q2.2, split it, and then use index_documents to add all its chunks and their mock embeddings to a new instance of your SimpleVectorStore. 
'''
s1 = SimpleVectorStore(0,[0, 0, 0], "")

index_documents(chunks, s1, create_mock_embedding)
print("Id of this is:",s1.get_document_by_id(10))

'''
Question 2.5: After indexing, verify that your chunks are stored by iterating through the vector_store_instance's internal storage and printing a few document IDs and their corresponding original texts. 
'''

random = 1
while 1:
    text = s1.get_document_by_id(random)
    
    if text =="none":
        break
    print("Id",random,  "of this is:",text)
    random+=2


'''
Retrieval Step 
Question 2.6: Add a method retrieve_top_k(query_embedding, k=1) to your SimpleVectorStore class. This method should: 
Calculate the cosine similarity between query_embedding and every embedding stored in the vector store. 
Return the k (default 1) (document_id, original_text, similarity_score) tuples with the highest similarity scores, sorted in descending order of similarity. 
'''
#done above in the class structure

'''
Question 2.7: Formulate a sample "query" string related to your indexed paragraph (e.g., "When was the first computer invented?"). Generate a mock embedding for this query. Then, use retrieve_top_k on your SimpleVectorStore to find the top 2 most relevant chunks. Print the retrieved chunks and their similarity scores. 
'''

query = " this digital landscape."
emb = create_mock_embedding(query)

print(s1.retrieve_top_k(emb, 2))


'''
Augmenting the Prompt & Full RAG Chain (Conceptual/Mock LLM) 
Question 2.8: Write a Python function augment_prompt(query, retrieved_texts) that takes a user query string and a list of retrieved_texts (the actual text content of the chunks). It should return a single string representing the augmented prompt, clearly indicating the context from the retrieved texts and the original query. 
'''
def augment_prompt(query, retrieved_texts):
    prompt = f"you are a assistant that helps in retriving documents based on similairty. Find {query} in {retrieved_texts}"
    return prompt


'''
Question 2.9: Simulate a simple LLM response. Write a function mock_llm_response(prompt) that takes the augmented prompt string and returns a hardcoded, generic response (e.g., "Based on the provided information, I can answer your question."). This is a placeholder for an actual LLM call. 
'''
def mock_llm_response(prompt) :
    return "Based on the provided information, I can answer your question. I am thrilled to announce that your query....."


'''
Question 2.10: Combine all the simulated steps into a full run_rag_pipeline(query, vector_store, embedding_func, mock_llm_func, k=1) function. Demonstrate its usage with a query, and print the final "LLM" response. 
'''
print("-------------------------------------------------------------")
# Sampele Text
the_internet = "The Internet, a technological marvel born from the minds of visionaries, has grown into a global phenomenon that touches every facet of our lives. Its roots trace back to ARPANET’s inception in the 1960s when the revolutionary concept of interconnected computers was born. This early network laid the groundwork for the modern Internet, enabling computers to share data and communicate over vast distances. In the subsequent decades, this technology evolved, leading to the creation of the World Wide Web by Tim Berners-Lee in the late 1980s. Today, the Internet serves as a digital frontier that transcends geographical boundaries. It provides access to a staggering wealth of information, entertainment, and services. From social networking and e-commerce to online education and remote work, its applications are diverse and far-reaching. Moreover, the Internet’s impact on communication cannot be understated, as it has transformed how people interact, fostering connections and collaborations across the globe.However, this technological marvel also presents challenges. The prevalence of misinformation, cybercrimes, and privacy breaches remind us of the Internet’s dual nature. Striking a balance between its advantages and disadvantages is imperative as we navigate this digital landscape."


def run_rag_pipeline(query, vector_store, embedding_func, mock_llm_func, k=1):
    
    chunks = load_and_split_text(the_internet, 100)

    index_documents(chunks, vector_store, embedding_func)

    emb = create_mock_embedding(query)
    nearest = vector_store.retrieve_top_k(emb, 2)
    print("nearest values are:", nearest)
    prompt = augment_prompt(query, nearest[0]) 
    prompt = mock_llm_func(prompt)
    return prompt
    

vec = SimpleVectorStore(0, [], "")

final = run_rag_pipeline("digital landscape", vec, create_mock_embedding, mock_llm_response, 2)

print("\nFinal Response: ", final)

