import uvicorn


if __name__ == "__main__":
    uvicorn.run("src.cookdevmax:app", reload=True)