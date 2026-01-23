import os
import google.generativeai as genai

# Pulling the key from your GitHub Secret
api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=api_key)

def analyze_job(description):
    # Updated model string to ensure compatibility
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    prompt = f"""
    You are a Job Application Risk Analyzer. 
    Analyze the following job description for 'Experience Creep' 
    (requirements > 2 years for junior roles) and 'Senior Language'.
    
    Provide a Risk Score (1-10) and a brief explanation of the red flags.
    
    Job Description:
    {description}
    """
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    test_job = "Software Engineer - Entry Level. 5+ years of experience required."
    print(analyze_job(test_job))


