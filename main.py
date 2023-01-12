from fastapi import FastAPI, File, UploadFile
import os

directory = "./savefile"



app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Set the chunk size to 512 bytes
    chunk_size = 2*1024*1024
    filename = file.filename
    directory = "./savefile"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    # Open the file in write binary mode
    with open(file_path, "wb") as f:
        i = 0
        while True:
            
            # Read the chunk of data
            chunk = await file.read(chunk_size)
            if not chunk:
                i = 0
                break
            # Write the chunk of data to the file
            f.write(chunk)
            f.flush()
            i = i +1 
            print(f"number of chunk is : {i}")
    return {"filename": file.filename}