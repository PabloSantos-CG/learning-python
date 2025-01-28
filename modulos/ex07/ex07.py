import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

print(os.getenv('DB_PASSWORD'))
