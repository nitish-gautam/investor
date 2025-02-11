# backend/app/models.py
# ----------------------
# This module defines the database models for the Investors microservice.
# The models are used to map Python objects to database tables via SQLAlchemy ORM.

from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Investor(Base):
    """
    Represents an investor entity in the system.

    Attributes:
        id (int): Unique identifier for the investor.
        name (str): Name of the investor.
        investor_type (str): Type of investor (e.g., fund manager, bank).
        country (str): Country of the investor.
        date_added (Date): Date when the investor was added to the system.
        last_updated (Date): Last update timestamp.

    Relationships:
        commitments (list of Commitment): All commitments associated with this investor.
    """
    __tablename__ = "investors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    investor_type = Column(String)
    country = Column(String)
    date_added = Column(Date)
    last_updated = Column(Date)

    # Relationship to Commitment model
    commitments = relationship("Commitment", back_populates="investor")


class Commitment(Base):
    """
    Represents an investment commitment made by an investor.

    Attributes:
        id (int): Unique identifier for the commitment.
        investor_id (int): Foreign key reference to an Investor.
        asset_class (str): Type of asset committed (e.g., real estate, private equity).
        amount (float): The monetary amount committed.
        currency (str): Currency of the commitment (e.g., GBP, USD).

    Relationships:
        investor (Investor): Reference to the associated investor.
    """
    __tablename__ = "commitments"

    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey("investors.id"))
    asset_class = Column(String)
    amount = Column(Float)
    currency = Column(String)

    # Relationship to Investor model
    investor = relationship("Investor", back_populates="commitments")
