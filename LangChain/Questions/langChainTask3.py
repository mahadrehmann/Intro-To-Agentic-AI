
'''
Cosine Similarity measures the cosine of the angle between two vectors. If two vectors are pointing in the same direction, the angle between them is zero, and the cosine is 1
'''

'''
Question 1.1: Write a Python function create_mock_embedding(text) that takes a string and returns a simple list of 3 floating-point numbers as its "embedding." Make the numbers slightly different for different inputs (e.g., based on len(text) or character sums) to simulate unique embeddings. 
'''

def create_mock_embedding(text):
    embedding = []

    for char in text:   
        x1 = 1+ord(char)   # 1−1/(1+x) normalizes value b/w 0 and 1
        x2 = 1 / x1
        x = 1-x2
        embedding.append(x)
    return embedding

# var = len (0)


print(create_mock_embedding("Mahad"))




'''
Question 1.2: Use your create_mock_embedding function to generate embeddings for three short sentences: "The cat sat on the mat.", "The dog barked loudly.", and "A small feline rested on a rug." Store these sentences along with their mock embeddings in a list of tuples (sentence, embedding). 
'''

print("Embedding 1:", create_mock_embedding("The cat sat on the mat."))
print("Embedding 2:",create_mock_embedding("The dog barked loudly."))
print("Embedding 3:",create_mock_embedding("A small feline rested on a rug."))


'''
Question 1.3: Modify create_mock_embedding to ensure that if the input text is identical, the exact same mock embedding is returned. This simulates deterministic embedding models. 
'''

from sklearn.metrics.pairwise import cosine_similarity  #TODO 

emb1 = create_mock_embedding("Test String")
emb2 = create_mock_embedding("Test String")


similar = cosine_similarity([emb1], [emb2])
print(f"\n\nCosine Similarity (scikit-learn): {similar[0][0]}")


if emb1 == emb2:
    print("They are same")
    