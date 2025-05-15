def read_file(filename):
    """Reads content from a file and returns it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")
        return None


def write_modified_file(new_filename, content):
    """Writes the modified content to a new file."""
    try:
        with open(new_filename, 'w') as file:
            file.write(content)
        print(f"✅ Modified content written to '{new_filename}'")
    except IOError:
        print(f"❌ Error: Could not write to the file '{new_filename}'.")


def main():
    input_filename = input("📄 Enter the name of the file to read: ")
    content = read_file(input_filename)

    if content is not None:
        # Modify the content (e.g., make it uppercase)
        modified_content = content.upper()
        
        output_filename = input("💾 Enter the name of the new file to save modified content: ")
        write_modified_file(output_filename, modified_content)


if __name__ == "__main__":
    main()
