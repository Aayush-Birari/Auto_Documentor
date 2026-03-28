import os
from google import genai # CHANGED: New library import

# Fetch the API key from the Jenkins environment
api_key = os.getenv("GEMINI_API_KEY")

# CHANGED: Initialize the new client
client = genai.Client(api_key=api_key)

def generate_readme(code_content):
    prompt = f"""
    You are an expert technical writer. Write a clear, professional README.md 
    for the following code. Include a Title, Description, Prerequisites, 
    and How to Run sections. Here is the code:

    {code_content}
    """
    
    # CHANGED: New syntax for generating content
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    # 1. Read the application code
    with open("app.py", "r") as f:
        code = f.read()

    # 2. Generate the documentation
    print("Generating documentation via AI...")
    readme_content = generate_readme(code)

    # 3. Save it to a markdown file
    with open("README.md", "w") as file:
        file.write(readme_content)

    print("README.md successfully updated!")