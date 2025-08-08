import os
import nbformat

def update_kernel_in_notebook(notebook_path, kernel_name=".venv", display_name="Python (.venv)"):
    """
    Update the kernel specification in a Jupyter notebook.

    Parameters
    ----------
    notebook_path : str
        Path to the Jupyter notebook file (.ipynb).
    kernel_name : str, optional
        Name of the kernel to set in the notebook metadata (default is ".venv").
    display_name : str, optional
        Display name of the kernel to set in the notebook metadata (default is "Python (.venv)").
    """
    # Open the notebook file and read its contents
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    # Ensure the 'kernelspec' metadata exists
    if "kernelspec" not in nb["metadata"]:
        nb["metadata"]["kernelspec"] = {}

    # Update the kernel name and display name
    nb["metadata"]["kernelspec"]["name"] = kernel_name
    nb["metadata"]["kernelspec"]["display_name"] = display_name

    # Write the updated notebook back to disk
    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)


def find_notebooks(root_dir):
    """
    Recursively find all Jupyter notebook files in a directory.

    Parameters
    ----------
    root_dir : str
        Root directory to search for notebook files.

    Returns
    -------
    list of str
        List of paths to found notebook files.
    """
    notebooks = []
    # Walk through the directory tree
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check for .ipynb extension
            if filename.endswith(".ipynb"):
                notebooks.append(os.path.join(dirpath, filename))
    return notebooks


def main():
    """
    Main function to update the kernel specification in all notebooks
    found under the current script's directory.
    """
    # Get the directory where this script is located
    root = os.path.dirname(os.path.abspath(__file__))

    # Find all notebooks in the directory tree
    notebooks = find_notebooks(root)
    print(f"Found {len(notebooks)} notebooks.")

    # Update the kernel in each notebook
    for nb_path in notebooks:
        print(f"Updating {nb_path}")
        update_kernel_in_notebook(nb_path)

    print("Done updating kernels.")


if __name__ == "__main__":
    main()