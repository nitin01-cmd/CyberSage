import requests

# Function to check the phishing URL using Google Safe Browsing API
def check_phishing_url(url):
    # Hardcoded API key (replace with your actual API key)
    API_KEY = 'AIzaSyCHOotb9NvEoQSTPDEpYfGCaS4GHXbkp_Q'  # Replace with your actual API key

    # Google Safe Browsing API URL
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

    # Payload (the URL you want to check)
    payload = {
        "client": {
            "clientId": "your-client-id",  # Can be anything you want (it’s used for tracking)
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    # Send the request to the Google Safe Browsing API
    response = requests.post(api_url, json=payload)

    # Handle response
    if response.status_code == 200:
        data = response.json()
        if 'matches' in data:
            print(f"The URL {url} is a phishing link!")
            return True  # It is a phishing URL
        else:
            print(f"The URL {url} is safe.")
            return False  # It is safe
    else:
        print("Error with API request.")
        return False  # In case of error, assume safe

# Main function to take user input for URL
def main():
    # Get URL from the user
    url = input("Enter a URL to check: ")

    # Check if the URL is phishing
    check_phishing_url(url)

# Run the program
if __name__ == "__main__":
    main()
