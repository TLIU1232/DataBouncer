from scanner import extract_headers
from sanitiser import anonymise
import dotenv
dotenv.load_dotenv()
from classifier import classify_columns
from roast import generate_roast

def main():

    input_file = "data.csv"

    print("Scanning file...")

    headers = extract_headers(
        input_file
    )

    print("Columns detected:")
    print(headers)

    result = classify_columns(
        headers
    )

    sensitive = [
        item["column"]
        for item in result["sensitive_columns"]
    ]
    print("\nSensitive columns:")
    print(sensitive)
    output = anonymise(
        input_file,
        sensitive
    )
    print(
        f"Done: {output}"
    )
    roast = generate_roast(result)

    print("\n DataBouncer says:")

    print(roast)

if __name__ == "__main__":
    main()