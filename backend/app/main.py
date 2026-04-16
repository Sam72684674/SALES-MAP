from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.database import init_db
from app.routers import zones, dealers, uploads, pivots, filters, chat, exports, health

load_dotenv()

app = FastAPI(title="SalesMap API", description="South Gujarat Sales Intelligence Mapping", version="1.0.0")
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(CORSMiddleware, allow_origins=[o.strip() for o in cors_origins], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
async def startup():
    init_db()

app.include_router(health.router, tags=["health"])
app.include_router(zones.router, prefix="/api/zones", tags=["zones"])
app.include_router(dealers.router, prefix="/api/dealers", tags=["dealers"])
app.include_router(uploads.router, prefix="/api/uploads", tags=["uploads"])
app.include_router(pivots.router, prefix="/api/pivots", tags=["pivots"])
app.include_router(filters.router, prefix="/api/filters", tags=["filters"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(exports.router, prefix="/api/exports", tags=["exports"])

@app.get("/")
async def root():
    return {"message": "SalesMap API", "docs": "/docs", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)