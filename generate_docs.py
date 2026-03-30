import os
from groq import Groq

api_key = os.getenv("GEMINI_API_KEY") 
client = Groq(api_key=api_key)

def generate_readme(code_content):
    prompt = f"""
    You are an expert technical writer. Write a clear, professional README.md 
    for the following code. Include a Title, Description, Prerequisites, 
    and How to Run sections. Here is the code:

    {code_content}
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant", 
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    with open("app.py", "r") as f:
        code = f.read()

    print("Generating documentation via Groq AI...")
    readme_content = generate_readme(code)

    with open("README.md", "w") as file:
        file.write(readme_content)

    print("README.md successfully updated!")