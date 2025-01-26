
from flask import Flask, request, jsonify
import requests
from groq import Groq
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# Function to fetch fact-check results
def search_claims(api_key, query):
    url = 'https://factchecktools.googleapis.com/v1alpha1/claims:search'
    params = {'key': api_key, 'query': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API error: {response.status_code}", "details": response.text}

# Function to extract titles from the fact-check results
def extract_titles_from_fact_check_results(results):
    titles = []
    for result in results.get("claims", []):
        claim_review = result.get("claimReview", [])
        for review in claim_review:
            title = review.get("title")
            if title:
                titles.append(title)
    return titles

# Function to generate Llama response
def generate_llama_response(predefined_prompt, api_key):
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": predefined_prompt}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content

# API keys
API_KEY_FACT_CHECK = "AIzaSyCils4GVVHtQyBcyCmrGWNAUpoR7dmOBy0"
API_KEY_LLAMA = "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"

# Flask route to handle the API call
@app.route('/verify-news', methods=['POST'])
def verify_news():
    # Parse JSON input
    data = request.get_json()
    if not data or 'news_query' not in data:
        return jsonify({"error": "Invalid input. Please provide 'news_query' in JSON format."}), 400

    query = data['news_query']

    # Step 1: Get fact-check results
    fact_check_results = search_claims(API_KEY_FACT_CHECK, query)

    if "error" in fact_check_results:
        return jsonify({"error": fact_check_results["error"], "details": fact_check_results["details"]}), 500

    # Step 2: Extract fact-check titles
    fact_titles = extract_titles_from_fact_check_results(fact_check_results)

    # Step 3: Create a predefined prompt
    predefined_prompt = (
        f"Here are some fact-checked titles related to the query '{query}':\n"
        + "\n".join(fact_titles) +
        "\n\nBased on the above fact-checked titles and your own knowledge, "
        "determine whether the user's query is real or fake news. Respond with the following format:\n"
        "- 'The provided news is Real' or 'The provided news is Fake'\n"
        "- Provide a brief justification explaining your reasoning."
    )

    # Step 4: Get Llama response
    llama_response = generate_llama_response(predefined_prompt, API_KEY_LLAMA)

    # Return the response as JSON
    return jsonify({"llama_response": llama_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
