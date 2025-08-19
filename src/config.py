from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    base_dir = Path(__file__).resolve().parent.parent
    # data
    raw_dir = base_dir/"data"/"raw"
    processed_dir = base_dir/"data"/"processed"
    # rebrickable
    rebrickable_base = "https://rebrickable.com/api/v3"
    rebrickable_key = os.getenv("REBRICKABLE_API_KEY")