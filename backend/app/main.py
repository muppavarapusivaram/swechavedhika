from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import engine
from app.routers.archive import router as archive_router
from app.routers.auth import router as auth_router
from app.routers.events import router as events_router
from app.routers.polls import router as polls_router
from app.routers.qa import router as qa_router
from app.routers.whatsapp import router as whatsapp_router

app = FastAPI(
    title="Swecha Vedika Backend",
    description="Bandwidth-frugal, bilingual live meeting and broadcast platform API",
    version="2.0.0",
)

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth_router)
app.include_router(events_router)
app.include_router(qa_router)
app.include_router(polls_router)
app.include_router(archive_router)
app.include_router(whatsapp_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Swecha Vedika API",
        "version": "2.0.0",
    }


@app.get("/health/db")
def db_health_check(response: Response):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            users_count = connection.execute(text("SELECT count(*) FROM users")).scalar() or 0
            events_count = connection.execute(text("SELECT count(*) FROM events")).scalar() or 0
            attendance_count = connection.execute(text("SELECT count(*) FROM attendance")).scalar() or 0
            questions_count = connection.execute(text("SELECT count(*) FROM questions")).scalar() or 0
            polls_count = connection.execute(text("SELECT count(*) FROM polls")).scalar() or 0

        return {
            "status": "ok",
            "db": "connected",
            "tables": {
                "users": users_count,
                "events": events_count,
                "attendance": attendance_count,
                "questions": questions_count,
                "polls": polls_count,
            },
        }
    except Exception as exc:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "error",
            "message": f"Database connection failed: {str(exc)}",
        }
