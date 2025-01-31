import os
import json
import sys
import nbformat
from nbconvert import HTMLExporter

def remove_fencing(notebook_file, temp_notebook_file):
    with open(notebook_file, "r") as f:
        notebook = json.load(f)

    for cell in notebook["cells"]:
        if cell["cell_type"] == "markdown":
            new_source = []
            in_admonition = False
            for line in cell["source"]:
                if line.startswith("::{admonition} SOLUTION :class: hint") or line.startswith("```"):
                    in_admonition = True
                elif line.startswith(":::") or line.startswith("```"):
                    in_admonition = False
                elif not in_admonition:
                    new_source.append(line)
            cell["source"] = new_source

    with open(temp_notebook_file, "w") as f:
        json.dump(notebook, f, indent=1)

def convert_to_html(temp_notebook_file, html_file):
    with open(temp_notebook_file, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    body, resources = html_exporter.from_notebook_node(notebook)

    with open(html_file, "w") as f:
        f.write(body)

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_solution.py <notebook-name-without-extension>")
        sys.exit(1)

    notebook_name = sys.argv[1]

    if notebook_name.endswith(".ipynb"):
        print("Warning: Removing .ipynb extension from input")
        notebook_name = notebook_name[:-6]

    notebook_file = f"{notebook_name}.ipynb"
    html_file = f"{notebook_name}.html"
    temp_notebook_file = f"{notebook_name}_temp.ipynb"

    if not os.path.isfile(notebook_file):
        print(f"Error: Notebook file '{notebook_file}' does not exist.")
        sys.exit(1)

    remove_fencing(notebook_file, temp_notebook_file)
    convert_to_html(temp_notebook_file, html_file)

    print(f"HTML conversion successful: '{html_file}' created.")
    os.remove(temp_notebook_file)

if __name__ == "__main__":
    main()