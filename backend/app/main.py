# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .database import SessionLocal
from . import models, schemas
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Investors Microservice",
    version="1.0.0",
    description="Provides endpoints to list investors and their commitments."
)

# Enable CORS to allow communication with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get database session
# Ensures database session is properly opened and closed per request


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/investors", response_model=List[schemas.InvestorRead])
def list_investors(db: Session = Depends(get_db)):
    """
    Retrieve all investors along with their nested commitments.
    Useful for displaying an investor overview in the frontend.
    """
    investors = db.query(models.Investor).all()
    return investors


@app.get("/investors/{investor_id}", response_model=schemas.InvestorRead)
def get_investor(
    investor_id: int,
    asset_class: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Retrieve details of a specific investor by ID.
    Allows optional filtering of commitments by asset class.
    """
    investor = db.query(models.Investor).filter(
        models.Investor.id == investor_id).first()
    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")

    # If filtering by asset class, update commitments list
    if asset_class:
        filtered_commitments = [
            c for c in investor.commitments if c.asset_class == asset_class
        ]
        investor.commitments = filtered_commitments

    return investor


@app.get("/investors/{investor_id}/total_commitments")
def get_investor_total_commitments(investor_id: int, db: Session = Depends(get_db)):
    """
    Calculate and return the total commitment amount for a specific investor in GBP.
    """
    investor = db.query(models.Investor).filter(
        models.Investor.id == investor_id).first()
    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    total = sum([c.amount for c in investor.commitments])
    return {"investor_id": investor_id, "total_commitments_gbp": total}


@app.get("/investors_with_totals")
def list_investors_with_totals(db: Session = Depends(get_db)):
    """
    Retrieve a list of investors, each with their total commitment amount.
    This endpoint is optimized for frontend display where only summarized investor data is needed.
    """
    results = []
    investors = db.query(models.Investor).all()
    for inv in investors:
        total = sum([c.amount for c in inv.commitments])
        results.append({
            "id": inv.id,
            "name": inv.name,
            "investor_type": inv.investor_type,
            "country": inv.country,
            "date_added": inv.date_added,
            "total_commitments_gbp": total
        })
    return results
