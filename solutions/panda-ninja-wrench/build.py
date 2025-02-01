import os
import sys
import nbformat
from nbconvert import HTMLExporter, MarkdownExporter
import subprocess

def convert_notebook(base_name):
    # Remove extensions if they are passed
    if base_name.endswith('.ipynb') or base_name.endswith('.html') or base_name.endswith('.docx'):
        print(f"Warning: Extension provided in the base name. Removing extension and proceeding.")
        base_name = os.path.splitext(base_name)[0]

    notebook_path = f"{base_name}.ipynb"
    html_output_path = f"{base_name}.html"
    docx_output_path = f"{base_name}.docx"

    # Check if the notebook file exists
    if not os.path.exists(notebook_path):
        print(f"Error: The file {notebook_path} does not exist.")
        sys.exit(1)

    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Initialize the HTML exporter
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True  # Exclude input cells if desired

    # Convert the notebook to HTML
    (body, resources) = html_exporter.from_notebook_node(notebook)

    # Write the HTML output to a file
    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(body)

    print(f"Converted {notebook_path} to {html_output_path}")

    # Initialize the Markdown exporter
    md_exporter = MarkdownExporter()
    md_exporter.exclude_input = True  # Exclude input cells if desired

    # Convert the notebook to Markdown
    (md_body, md_resources) = md_exporter.from_notebook_node(notebook)

    # Write the Markdown output to a temporary file
    md_temp_path = f"{base_name}.md"
    with open(md_temp_path, 'w', encoding='utf-8') as f:
        f.write(md_body)

    # Convert the Markdown file to DOCX using pandoc
    try:
        subprocess.run(['pandoc', md_temp_path, '-o', docx_output_path], check=True)
        print(f"Converted {md_temp_path} to {docx_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Pandoc conversion failed with error: {e}")
        sys.exit(1)
    finally:
        # Clean up the temporary Markdown file
        os.remove(md_temp_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build.py <base_name>")
        sys.exit(1)

    base_name = sys.argv[1]
    convert_notebook(base_name)