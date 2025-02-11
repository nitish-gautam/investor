import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database Configuration
# ----------------------
# This module sets up the database connection and ORM session handling.
#
# - Uses SQLite as the database (for demonstration purposes).
# - In production, replace SQLite with Postgres, MySQL, or other databases.
# - Reads connection settings from environment variables when needed.

# Define the database URL
# SQLite is a lightweight, file-based database.
# For larger applications, switch to a cloud database (e.g., PostgreSQL).
DB_URL = "sqlite:///./investors.db"

# Create the database engine
# The 'check_same_thread' setting is specific to SQLite to allow multiple threads.
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

# Create a session factory
# - autocommit=False: Transactions are explicitly committed or rolled back.
# - autoflush=False: Changes are not automatically written to the database.
# - bind=engine: Connects sessions to the database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for ORM models
# All database models should inherit from this base class.
Base = declarative_base()
