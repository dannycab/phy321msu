import os
import json

def update_kernel_metadata(notebook_path, kernel_name):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    notebook['metadata']['kernelspec'] = {
        "name": kernel_name,
        "display_name": f"Python 3 ({kernel_name})",
        "language": "python"
    }

    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)

def update_all_notebooks(directory, kernel_name):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                update_kernel_metadata(notebook_path, kernel_name)

# Update all notebooks in the specified directory
update_all_notebooks('/Users/caballero/repos/teaching/phy321msu', 'jbook')