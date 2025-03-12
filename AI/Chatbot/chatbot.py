from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Agent, Crew, Task
from crewai.llm import LLM
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (change this later for security)
    allow_methods=["*"],   # Allow all HTTP methods
    allow_headers=["*"],   # Allow all headers
)

# ✅ Initialize local LLM (Ollama)
local_llm = LLM(
    model="ollama/phi",
    base_url="http://localhost:11434",
    litellm_provider="ollama"
)

# ✅ Define Agent
chat_agent = Agent(
    role="Chat Assistant",
    goal="Provide helpful answers to user queries.",
    backstory="An AI assistant that answers questions interactively.",
    llm=local_llm,
    verbose=True
)

# ✅ Define API Request Model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Create a task dynamically based on user input
        chat_task = Task(
            description=request.message,
            agent=chat_agent,
            expected_output="A helpful response to the query."
        )

        # Create Crew and execute task
        chat_crew = Crew(
            agents=[chat_agent],
            tasks=[chat_task],
            llm=local_llm,
            verbose=True
        )

        response = chat_crew.kickoff()
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Run the server (optional if running via command)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
