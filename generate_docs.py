import os
from groq import Groq

# Jenkins will inject the key we saved
api_key = os.getenv("GEMINI_API_KEY") 

# Initialize the Groq client
client = Groq(api_key=api_key)

def generate_readme(code_content):
    prompt = f"""
    You are an expert technical writer. Write a clear, professional README.md 
    for the following code. Include a Title, Description, Prerequisites, 
    and How to Run sections. Here is the code:

    {code_content}
    """
    
    # Using Meta's Llama 3 model via Groq (Super fast, no billing traps)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
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

<<<<<<< HEAD
    print("README.md successfully updated!")
=======
    print("README.md successfully updated!")
>>>>>>> 51ef4d2c03f2faa4476aa988884757f498ef2a95
