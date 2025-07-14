from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import os
import shutil

app = FastAPI()
os.makedirs("uploads", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <html>
        <body>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
