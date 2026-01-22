import os
import openai

# Use Environment Variables for security
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_job(description):
    # System Prompt based on your Validation Insights
    system_prompt = (
        "You are a Job Application Risk Analyzer. Identify 'Experience Creep' "
        "(requirements > 2 years for junior roles) and 'Senior Language' "
        "like 'proven track record'. Provide a Risk Score (1-10) and explain why."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Analyze this job: {description}"}
        ]
    )
    return response.choices[0].message.content

# For tonight's test, we paste a description here
if __name__ == "__main__":
    test_job = "Paste a real job description from your 305 applications here"
    print(analyze_job(test_job))
