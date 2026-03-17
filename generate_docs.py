import os
import google.generativeai as genai

# Load the API key from the environment (Jenkins will provide this securely)
genai.configure(api_key=os.getenv("AIzaSyDtNINi4gzBXgCVywn4tK81jHmJ7Me6C7c"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_readme(code_content):
    prompt = f"""
    You are an expert technical writer. Write a clear, professional README.md 
    for the following code. Include a Title, Description, Prerequisites, 
    and How to Run sections. Here is the code:

    {code_content}
    """
    response = model.generate_content(prompt)
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
