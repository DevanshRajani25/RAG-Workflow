# load_data.py

def load_data(file_path: str) -> str:
    """
    Load data from any data source.
    """
    with open(file_path) as f:
        data = f.read()
    return data
