from datetime import datetime
from rich.console import Console
import logging
import os

def clear_screen():
    console = Console()
    console.clear()

def log():
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    log_filename = datetime.now().strftime("%Y%m%d_%H%M%S.log")
    log_filepath = os.path.join(log_folder, log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath, encoding='utf-8')
        ]
    )
    return logging.getLogger(__name__)