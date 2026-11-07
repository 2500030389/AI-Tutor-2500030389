from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor PBL Project",
              version="1.0.0",)


@klu.get("/")
def home():
    return {"message": "Welcome to the AI Tutor Project!"}

@klu.get("/demo")
def demo():
    return {"message": "kl university!"}

@klu.get("/askquestion")
def ask():
    return {"message": "what is LLM","Answer":"large language problem"}
    