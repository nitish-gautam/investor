# backend/app/schemas.py
# ----------------------
# This module defines Pydantic schemas for data validation and serialization.
# Pydantic ensures data consistency and integrity when interacting with API requests/responses.

from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class CommitmentBase(BaseModel):
    """
    Base schema for investment commitments.

    Attributes:
        asset_class (str): Type of asset committed (e.g., real estate, private equity).
        amount (float): The monetary amount committed.
        currency (str): Currency of the commitment (e.g., GBP, USD).
    """
    asset_class: str
    amount: float
    currency: str


class CommitmentCreate(CommitmentBase):
    """
    Schema for creating a new commitment.
    Inherits fields from CommitmentBase.
    """
    pass


class CommitmentRead(CommitmentBase):
    """
    Schema for reading commitment data.
    Includes:
        - Unique commitment ID.
        - ORM mode enabled for database serialization.
    """
    id: int

    class Config:
        orm_mode = True


class InvestorBase(BaseModel):
    """
    Base schema for an investor.

    Attributes:
        name (str): Name of the investor.
        investor_type (str): Type of investor (e.g., fund manager, bank).
        country (str): Country of the investor.
        date_added (date): Date when the investor was added.
        last_updated (date): Last update timestamp.
    """
    name: str
    investor_type: str
    country: str
    date_added: date
    last_updated: date


class InvestorCreate(InvestorBase):
    """
    Schema for creating a new investor.
    Inherits fields from InvestorBase.
    """
    pass


class InvestorRead(InvestorBase):
    """
    Schema for reading investor data.
    Includes:
        - Unique investor ID.
        - Nested list of commitments.
        - ORM mode enabled for database serialization.
    """
    id: int
    commitments: List[CommitmentRead] = []

    class Config:
        orm_mode = True
