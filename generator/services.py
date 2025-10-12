import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

def generate_ad_copy(product_name, audience, tone):
    prompt = f"""
    Generate 3 short, engaging social media ad copies for:
    Product: {product_name}
    Audience: {audience}
    Tone: {tone}
    Each copy should include a call-to-action.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250
    )
    return response.choices[0].message["content"]
