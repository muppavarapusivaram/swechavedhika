from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import engine
from app.routers.auth import router as auth_router
from app.routers.events import router as events_router

app = FastAPI(title="Prototype Backend")

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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
def db_health_check(response: Response):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            users_count = (
                connection.execute(text("SELECT count(*) FROM users")).scalar()
                or 0
            )
            events_count = (
                connection.execute(text("SELECT count(*) FROM events")).scalar()
                or 0
            )
            attendance_count = (
                connection.execute(
                    text("SELECT count(*) FROM attendance")
                ).scalar()
                or 0
            )

        return {
            "status": "ok",
            "db": "connected",
            "tables": {
                "users": users_count,
                "events": events_count,
                "attendance": attendance_count,
            },
        }
    except Exception as exc:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "error",
            "message": f"Database connection failed: {str(exc)}",
        }
