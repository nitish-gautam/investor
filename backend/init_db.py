# backend/init_db.py

import os
import csv
from datetime import datetime
from app.database import Base, engine, SessionLocal
from app.models import Investor, Commitment

HERE = os.path.dirname(__file__)  # location of init_db.py
CSV_PATH = os.path.join(HERE, "..", "data", "data.csv")


def init_db():
    # Create DB tables
    Base.metadata.drop_all(bind=engine)  # For demo only, drops existing data
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        with open(CSV_PATH, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # e.g. row = {
                #   "Investor Name": "Ioo Gryffindor fund",
                #   "Investory Type": "fund manager",
                #   "Investor Country": "Singapore",
                #   "Investor Date Added": "2000-07-06",
                #   "Investor Last Updated": "2024-02-21",
                #   "Commitment Asset Class": "Infrastructure",
                #   "Commitment Amount": "15000000",
                #   "Commitment Currency": "GBP"
                # }

                name = row["Investor Name"]
                investor_type = row["Investory Type"]
                country = row["Investor Country"]
                date_added = datetime.strptime(
                    row["Investor Date Added"], "%Y-%m-%d").date()
                last_updated = datetime.strptime(
                    row["Investor Last Updated"], "%Y-%m-%d").date()
                asset_class = row["Commitment Asset Class"]
                amount = float(row["Commitment Amount"])
                currency = row["Commitment Currency"]

                # Get or create investor
                investor = (
                    session.query(Investor)
                    .filter_by(name=name)
                    .first()
                )
                if not investor:
                    investor = Investor(
                        name=name,
                        investor_type=investor_type,
                        country=country,
                        date_added=date_added,
                        last_updated=last_updated,
                    )
                    session.add(investor)
                    session.commit()
                    session.refresh(investor)

                # Create the commitment
                commitment = Commitment(
                    investor_id=investor.id,
                    asset_class=asset_class,
                    amount=amount,
                    currency=currency
                )
                session.add(commitment)

            session.commit()

    finally:
        session.close()


if __name__ == "__main__":
    init_db()
    print("Database has been initialized with data from data.csv.")
