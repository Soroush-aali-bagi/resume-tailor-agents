def read_context(filename: str) -> str:
    """
    Read content from a file in the context directory.
    
    Args:
        filename (str): Name of the file to read
        
    Returns:
        str: Content of the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def save_resume(profile_text: str, filename: str) -> None:
    """
    Write a profile text to a file in the resumes directory.

    Args:
        profile_text (str): The text content to write to the file
        filename (str): Name of the file (without .txt extension)

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(profile_text) 