
import requests
from groq import Groq


def search_claims(api_key, query):
    url = 'https://factchecktools.googleapis.com/v1alpha1/claims:search'
    

    params = {
        'key': api_key,
        'query': query  
    }
    
 
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        
        print(response)
        return response.json()  
    else:
        return f"Error: {response.status_code}, {response.text}"

def extract_titles_from_fact_check_results(results):
    titles = []
    for result in results.get("claims", []):
        claim_review = result.get("claimReview", [])
        for review in claim_review:
            title = review.get("title")
            if title:
                titles.append(title)
    return titles


def generate_llama_response(predefined_prompt, api_key):
    prompt = predefined_prompt

   
    client = Groq(api_key=api_key)

 
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192", 
    )
    
    llama_response_content = response.choices[0].message.content
 
    return llama_response_content


api_key_fact_check = "AIzaSyCils4GVVHtQyBcyCmrGWNAUpoR7dmOBy0"  
api_key_llama = "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"  
query = "Narendra Modi deid " 

# Step 1: Get fact-check results
result = search_claims(api_key_fact_check, query)

# Step 2: Extract titles from the fact-check results
titles = extract_titles_from_fact_check_results(result)

# Step 3: Create predefined prompt
predefined_prompt = f"Here are some facts about the query '{query}':\n" + "\n".join(titles) + "\n\n, tell whether the user query is real or fake news.only tell fake or real use your own knowladge also "
# predefined_prompt = f"Here are some fact-checked titles related to '{query}':\n" + "\n".join(titles) + "\n\n respond with 'The provided news is Real' or 'The provided news is Fake'and dont include anything extra we are knowing that this is a response by LLm, followed by the justification.,Use yout knowladge also "


llama_response = generate_llama_response( predefined_prompt, api_key_llama)


print("Llama Response:", llama_response)


