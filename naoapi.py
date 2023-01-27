'''
    pip install fastapi
    pip install "uvicorn[standard]"
    pip install typing-extensions
    
-------------------------------------------

    uvicorn naoapi:app --reload 
    OR
    import uvicorn
    uvicorn.run(app)
'''
from fastapi import FastAPI
import uvicorn 
from pydantic import BaseModel

app = FastAPI()

printInfo = {
    0: {
        "test":"ok"
    }
}

class Info(BaseModel):
    test: str

# uvicorn api:app --reload
@app.get('/')
def index():
    return printInfo[0]

@app.put('/change-info')
def change_info(info: Info):
    printInfo[0] = info
    return printInfo[0]

if __name__ == "__main__":
    uvicorn.run(app)