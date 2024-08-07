from openai import AzureOpenAI
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def create_document(prompt, system_prompt):
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = "2024-05-01-preview"
    model = "gpt-4o-global"

    client = AzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        base_url=f"{api_base}/openai/deployments/{model}",
    )

    system_message = system_prompt

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            },
        ],
        max_tokens=2000,
        temperature=0.0,
    )

    return response

if __name__ == "__main__":

    prompt = ""

    try:
        result = create_document(prompt)
        print(f"Here's the abstract of the paper:\n")
        print(result.choices[0].message.content)
    except Exception as error:
        print(f"An error occurred: {error}")
        raise