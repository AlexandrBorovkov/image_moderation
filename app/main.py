from fastapi import FastAPI, UploadFile, HTTPException
import uvicorn
import httpx
import os
from dotenv import load_dotenv


app = FastAPI()

load_dotenv()

PICPURIFY_API_KEY = os.getenv("PICPURIFY_API_KEY")
PICPURIFY_API_URL = "https://www.picpurify.com/analyse/1.1"

@app.post("/moderate")
async def moderate_image(file: UploadFile):
    try:
        file_content = await file.read()
        async with httpx.AsyncClient() as client:
            response = await client.post(
                PICPURIFY_API_URL,
                files={
                    "file_image": (file.filename, file_content, file.content_type),
                    "API_KEY": (None, PICPURIFY_API_KEY),
                    "task": (None, "porn_moderation,drug_moderation,gore_moderation"),
                }
            )
            response.raise_for_status()
            data = response.json()
            if data.get("status") == "success":
                porn_found = data.get("porn_moderation").get("porn_content")
                if porn_found:
                    return {
                        "status": "REJECTED",
                        "reason": "NSFW content"
                    }
                else:
                    return {"status": "OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
