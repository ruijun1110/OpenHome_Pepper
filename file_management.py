def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def write_to_file(filepath, content):
    """Write the given content to a file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        for entry in content:
            file.write(f"{entry['role']}: {entry['content']}\n")