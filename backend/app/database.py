from sqlalchemy import create_engine, sessionmaker
from sqlalchemy.orm import scoped_session

# Database configurations
DATABASE_URL = 'sqlite:///your_database.db'

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}, echo=True)

# Session management
Session = scoped_session(sessionmaker(bind=engine))

# Initialize the database
def init_db():
    # Import your models here to create database tables
def close_db():
    Session.remove()  # Remove the session when done

# Foreign key pragma for SQLite
def enable_foreign_keys():
    engine.execute("PRAGMA foreign_keys = ON;")

# Usage example
if __name__ == '__main__':
    enable_foreign_keys()
    init_db()  # Initialize the database