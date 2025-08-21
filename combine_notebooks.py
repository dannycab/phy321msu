import nbformat

# Paths to your source notebooks
notebook1 = "lecture-notes/05_notes.ipynb"
notebook2 = "lecture-notes/week6/06_notes_2.ipynb"
output_notebook = "lecture-notes/05_notes_2.ipynb"

# Read both notebooks
with open(notebook1, "r", encoding="utf-8") as f1:
    nb1 = nbformat.read(f1, as_version=4)
with open(notebook2, "r", encoding="utf-8") as f2:
    nb2 = nbformat.read(f2, as_version=4)

# Combine cells
combined = nbformat.v4.new_notebook()
combined.cells = nb1.cells + nb2.cells

# Optionally, merge metadata (here we just use the first notebook's metadata)
combined.metadata = nb1.metadata

# Write the combined notebook
with open(output_notebook, "w", encoding="utf-8") as f_out:
    nbformat.write(combined, f_out)

print(f"Combined notebook written to {output_notebook}")