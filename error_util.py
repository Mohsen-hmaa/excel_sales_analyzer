import os
def save_error(file,error,error_path):
    os.makedirs(os.path.dirname(error_path),exist_ok=True)
    with open(error_path, "a") as f:
        f.write(f"{file}: {error}\n")