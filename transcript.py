


from flask import Flask, request, jsonify
import requests
from groq import Groq
from flask_cors import CORS
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)

def search_claims(api_key, query):
    url = 'https://factchecktools.googleapis.com/v1alpha1/claims:search'
    params = {'key': api_key, 'query': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.text)
        return response.json()
    else:
        return {"error": f"API error: {response.status_code}", "details": response.text}


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
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": predefined_prompt}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content


def is_news_item(text, api_key):
    predefined_prompt = (
        f"Determine whether the following text is a news statement or general text. "
        f"Respond with 'News' if it's a news item or 'General' if it's not.\n\n"
        f"Text: \"{text}\"\n\nResponse:"
    )
    response = generate_llama_response(predefined_prompt, api_key)
  
    response_clean = response.strip().lower()
    if "news" in response_clean:
        return True
    elif "general" in response_clean or "not a news" in response_clean:
        return False
    else:
   
        return False


API_KEY_FACT_CHECK = "AIzaSyCils4GVVHtQyBcyCmrGWNAUpoR7dmOBy0"
API_KEY_LLAMA = "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"


@app.route('/verify-news', methods=['POST'])
def verify_news():
    
    data = request.get_json()
    if not data or 'news_query' not in data:
        return jsonify({"error": "Invalid input. Please provide 'news_query' in JSON format."}), 400

    query = data['news_query']

 
    is_news = is_news_item(query, API_KEY_LLAMA)
    if not is_news:
        return jsonify({
            "message": "The provided input does not appear to be a news item. I can only assist with verifying news."
        }), 200

   
    fact_check_results = search_claims(API_KEY_FACT_CHECK, query)

    if "error" in fact_check_results:
        return jsonify({"error": fact_check_results["error"], "details": fact_check_results["details"]}), 500

   
    fact_titles = extract_titles_from_fact_check_results(fact_check_results)

    if not fact_titles:

        return jsonify({
            "llama_response": "No fact-checking information found for the provided news. Unable to verify its authenticity."
        }), 200

    predefined_prompt = (
        f"Here are some fact-checked titles related to the query '{query}':\n" +
        "\n".join(fact_titles) +
        "\n\nBased on the above fact-checked titles and your own knowledge, "
        "determine whether the user's query is Real or Fake news. Respond with the following format:\n"
        "- 'The provided news is Real' or 'The provided news is Fake'\n"
        "- Provide a brief justification explaining your reasoning."
    )


    llama_response = generate_llama_response(predefined_prompt, API_KEY_LLAMA)


    return jsonify({"llama_response": llama_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)