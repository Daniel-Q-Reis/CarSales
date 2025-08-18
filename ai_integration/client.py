import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the AI client on application startup
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("\nWARNING: GOOGLE_API_KEY not found in .env file.\n")
        model = None
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        print("\nINFO: AI Client configured successfully.\n")
except Exception as e:
    print(f"\nERROR: Could not configure AI client: {e}\n")
    model = None


def generate_car_bio(car_instance):
    """
    Generates a sales biography for a car instance using the Gemini API.
    """
    if not model:
        return None

    print(f"INFO: Generating AI bio for '{car_instance.model}'...")

    prompt = f"""
    You are a professional car sales assistant.
    Generate a short, exciting, and professional sales description in English, under 70 words,
    for the following vehicle. Focus on positive aspects and be creative.
    Do not include the price. Always describe some of each car specs like 0-60mph time, hp, number of doors, hidraulic wheel, etc

    - Model: {car_instance.model}
    - Brand: {car_instance.brand.name}
    - Model Year: {car_instance.model_year}
    """

    try:
        response = model.generate_content(prompt)
        print("INFO: AI bio generated successfully!")
        return response.text.strip()
    except Exception as e:
        print(f"--- ERROR CALLING AI API ---\n{e}\n--------------------------")
        # Return a standard fallback text in case of an API error
        return f"An elegant description for the {car_instance.factory_year} {car_instance.brand.name} {car_instance.model}."