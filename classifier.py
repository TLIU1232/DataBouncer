from openai import OpenAI
import json
import dotenv

dotenv.load_dotenv()

client = OpenAI()


def classify_columns(headers):

    prompt = f"""
    You are a corporate data security expert.

    Given these column headers, identify columns that should NOT
    be uploaded to public AI tools.

    Return JSON only.

    Categories:
    - personal_data
    - financial_data
    - confidential_business
    - harmless

    Headers:

    {headers}

    Format:

    {{
    "sensitive_columns": [
        {{
        "column":"salary",
        "category":"financial_data",
        "severity":"high"
        }}
    ]
    }}
    """


    response = client.responses.create(

        model="gpt-4.1-mini",

        input=prompt,

        text={

            "format": {

                "type": "json_object"

            }

        }

    )

    result = json.loads(response.output_text)

    return result