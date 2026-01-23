import os
import google.generativeai as genai

# We are using the same secret name to save time
api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=api_key)

def analyze_job(description):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
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
    # Test it with one of your 305 applications!
    test_job = "Software Engineer - Entry Level. 5+ years of experience required."
    print(analyze_job(test_job))

