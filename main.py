from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title = 'Shortening-URLs',
    description= 'A service for shortening links and redirecting users from a shortened link to an external address'
)




if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)



