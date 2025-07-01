'''
Project 2: Simulated Recipe Finder with Ingredient Matching 
Objective: Create a RAG-like system that helps users find recipes based on ingredients they have. This will simulate a more advanced search where the "query" might match only parts of the "documents." 

Concepts to Apply: 
Data Representation: Represent recipes as dictionaries or objects containing name, ingredients (list of strings), and instructions. Create a dataset of 5-10 mock recipes. 
Document Creation: For each recipe, create a "searchable document" string (e.g., combining recipe name and ingredients: "name: [Recipe Name], ingredients: [ingredient1], [ingredient2]..."). 
Simulated Embeddings: Generate mock embeddings for these searchable recipe documents. 
Vector Store: Store these recipe embeddings and their original recipe data (or a reference to it) in your SimpleVectorStore. 
Query Processing: When a user lists ingredients, create a query string from them (e.g., "recipes with: [user_ingredient1], [user_ingredient2]"). 
Retrieval: Use your retrieve_top_k to find recipes whose "searchable document" embeddings are most similar to the user's ingredient query embedding. 
Prompt Augmentation & Mock LLM: Augment a prompt to the mock LLM with the retrieved recipe details and ask it to "suggest a recipe you can make with these ingredients." 

Core Features: 
Define Mock Recipes: Create a Python list of dictionaries representing various recipes. 
Index Recipes: For each recipe, generate a searchable text representation, embed it, and add it to the SimpleVectorStore. 
User Ingredient Input: Prompt the user to enter a comma-separated list of ingredients they have. 
Generate Query Embedding: Create a mock embedding for the user's ingredient list. 
Retrieve Recipes: Find the top K most similar recipe documents from the vector store. 
Suggest Recipe: Augment the mock LLM's prompt with the retrieved recipe information (e.g., full recipe details or just names/key ingredients) and the user's query. Ask the mock LLM to suggest a recipe or list suitable recipes. 
Display Suggestion: Print the mock LLM's generated suggestion. 

Example Flow: 
--- Recipe Finder --- 
Enter ingredients you have (comma-separated, e.g., 'chicken, rice, broccoli'): [User Input] 
Searching for recipes... 
 
[Mock LLM Suggestion: "Based on your ingredients, you could make: 
Recipe Name: Chicken Stir-fry 
Ingredients: Chicken, Rice, Broccoli, Soy Sauce, Ginger 
Instructions: ... 
"] 
 
Want to find more recipes? (yes/no): 
> [User Input] 
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
    
    def print_all(self):
        for id, emb, text in self.lis:
            print(id, text, "\n")
    '''
    Retrieval Step 
    '''
    def retrieve_top_k(self, query_embedding, k=1):
        vals = []
        for id, emb, text in self.lis:
            sim = calculate_cosine_similarity(emb, query_embedding)
            vals.append((id, text, sim))

        vals.sort(key=lambda x: x[2], reverse=True)

        print("\n\nValues are: ", vals, "\n------------------------")

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
    prompt = f"you are a assistant that helps in retriving recipies based on similairty ingredients. Find {query} in {retrieved_texts}"
    return prompt

def mock_llm_response(prompt, nearest) :
    return f"Based on the provided information, I suggest this recipie:\n {nearest[1]}"


# Sample Reciepies
recipies = {
    1 : {
        "name" : "Chicken Tikka",
        "ingredients": ["chicken", "masala", "seasoning"],
        "instructions": "Marinate the chicken and cook it"
    },
    2 : {
        "name" : "Burger",
        "ingredients": ["patty", "buns", "ketchup"],
        "instructions": "Cook the patty and assemble"
    },
    3 : {
        "name" : "car",
        "ingredients": ["dough", "chicken", "ketchup"],
        "instructions": "Cook the base and add chicken on top"
    },
    4 : {
        "name" : "empyty",
        "ingredients": [""],
        "instructions": ""
    },
    5 : {
        "name" : "Pizza",
        "ingredients": ["dough", "chicken", "ketchup"],
        "instructions": "Cook the base and add chicken on top"
    },
    6 : {
        "name" : "Steak",
        "ingredients": ["beef", "butter", "vegetable"],
        "instructions": "Cook the steak in butter and then the veggies"
    },
    7 : {
        "name" : "Pulao",
        "ingredients": ["rice", "chicken", "beef", "seasoning"],
        "instructions": "Cook the rice with the chicken or beef"
    },
    8 : {
        "name" : "Plane",
        "ingredients": ["wings", "steering", "enginer"],
        "instructions": "Fly everything"
    },
}


def document_creator(dict):
    chunks = []
    for i in range (1,9):
        doc= ""
        print("right now item: ", dict[i].items(), "\n=============================")
        for x, obj in dict[i].items():
            # item = x + ": "
            item = ""
            
            if x=="ingredients":
                for y in obj:
                    # print(y)
                    item += y + " "
            else: 
                item += obj
            # print(item)
            doc += item
            doc+=" "
        chunks.append(doc)
        print(doc, "\n")
    return chunks


def run_rag_pipeline(query, vector_store, embedding_func, mock_llm_func, k=1):

    vector_store.print_all()

    emb = create_mock_embedding(query)
    nearest = vector_store.retrieve_top_k(emb, k)
    print("nearest values are:", nearest, "\n----------------------------------")
    prompt = augment_prompt(query, nearest)
    print("\nAugmented prompt:", prompt)
    prompt = mock_llm_func(prompt, nearest[0])
    return prompt


vec = SimpleVectorStore(0, [], "")
chunks = document_creator(recipies)
index_documents(chunks, vec, create_mock_embedding)

input_var = ""
input_var = input("\nEnter ingredients you have (e.g. chicken rice broccoli): ")

while input_var != "exit":   
    final = run_rag_pipeline(input_var, vec, create_mock_embedding, mock_llm_response, 5)

    print("\nFinal Response:\n", final)
    input_var = input("\nEnter ingredients you have (e.g. chicken rice broccoli) (exit to quit): ")
