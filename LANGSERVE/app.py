from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class EssayRequest(BaseModel):
    topic: str
    callback_url: str

@app.post("/generate-essay")
async def generate_essay(request: EssayRequest):
    # Placeholder for actual essay generation logic
    essay_content = f"Generated essay on the topic: {request.topic}"
    
    response_data = {"essay": {"content": essay_content}}
    
    try:
        forward_response = requests.post(request.callback_url, json=response_data)
        forward_response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to forward essay: {e}")

    return {"message": "Essay generated and forwarded successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
