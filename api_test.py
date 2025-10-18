import requests
import json

# --- CONFIGURATION ---
API_KEY = "8b184ee190msh17b8abd1ecd5741p15f4b7jsnc5c30ece4056" 

# This URL seems to be correct for sending requests, even if it returns a 404 for missing data.
API_URL = "https://vehicle-rc-information.p.rapidapi.com/"

API_HOST = "vehicle-rc-information.p.rapidapi.com"

# --- NEW SAMPLE PLATE ---
# Using a very common RTO (Mumbai) and vehicle type to increase the chance of a match.
SAMPLE_PLATE = "MH05DD9912" # A common format for a Bajaj Pulsar in Mumbai

def test_license_plate(plate_number):
    """
    Sends a request to the vehicle verification API and prints a clear verdict.
    """
    print(f"[*] Testing license plate: {plate_number}")

    payload = {"VehicleNumber": plate_number} 
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    
    print("[*] Sending request to API...")
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=15)
        
        # This is the most important check. A 200 status code means success.
        if response.status_code == 200:
            data = response.json()
            print("\n\033[92m--- API Response (Success!) ---\033[0m")
            print(json.dumps(data, indent=2))
            print("--------------------------------\n")
            print("\033[92m[+] VERDICT: Plate is GENUINE and details were successfully retrieved.\033[0m")
            return

        # Handle the "Data Not Found" case, which this API reports as a 404 error.
        elif response.status_code == 404:
            print("\n--- API Response (Data Not Found) ---")
            print(f"[-] Status Code: {response.status_code}")
            print(f"[-] Response Body: {response.text}\n")
            print("\033[93m[-] VERDICT: API connection is WORKING, but this plate number was NOT FOUND in the database. It is likely fake or invalid.\033[0m")
            return

        # Handle other errors like wrong API key (401/403) or server issues (5xx)
        else:
            response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"\n[!] An HTTP Error occurred: {http_err}")
        print(f"[-] Response Body: {response.text}\n")
        print("\033[91m[-] VERDICT: The API returned an unexpected error. Check your API subscription on RapidAPI.\033[0m")

    except requests.exceptions.RequestException as err:
        print(f"\n[!] A network or request error occurred: {err}")
        print("\033[91m[-] VERDICT: Failed to connect. Check your internet and the full API_URL (including https://).\033[0m")

# --- Run the test ---
if __name__ == "__main__":
    test_license_plate(SAMPLE_PLATE)





