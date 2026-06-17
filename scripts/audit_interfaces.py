import requests
import json
import urllib3

# Suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class NetworkAuditor:
    def __init__(self, target_ip, username, password):
        # RESTful Architecture: Using a clean noun resource path
        self.base_url = f"https://{target_ip}/restconf/data/ietf-interfaces:interfaces-state"
        self.auth = (username, password)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def fetch_operational_status(self):
        try:
            print(f"📡 Sending GET request to resource noun: {self.base_url}")
            response = requests.get(
                self.base_url, 
                auth=self.auth, 
                headers=self.headers, 
                verify=False
            )
            
            # Verifying API constraints guardrails
            if response.status_code == 200:
                print("✅ Success! Data retrieved.")
                return response.json()
            elif response.status_code == 429:
                print("⚠️ HTTP 429: Rate limit hit.")
                return None
            elif response.status_code == 403:
                print("🛑 HTTP 403: Forbidden - Authorization failure.")
                return None
            else:
                print(f"❌ Unexpected HTTP code: {response.status_code}")
                return None
        except Exception as e:
            print(f"💥 Connection failed: {e}")
            return None

if __name__ == "__main__":
    auditor = NetworkAuditor("10.1.1.1", "admin", "Cisco123")
    interface_data = auditor.fetch_operational_status()