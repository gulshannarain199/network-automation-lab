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
    # 1. Initialize our auditor client
    auditor = NetworkAuditor("10.1.1.1", "admin", "Cisco123")
    
    # 2. Fetch the raw multi-interface JSON data container
    interface_data = auditor.fetch_operational_status()
    
    # 3. The Loop Engine: Process data if the router returned a valid response
    if interface_data and "ietf-interfaces:interfaces-state" in interface_data:
        # Dig into the JSON dictionary to grab the actual list array of interfaces
        interfaces_list = interface_data["ietf-interfaces:interfaces-state"]["interface"]
        
        print("\n=== 🔍 STARTING OPERATIONAL INTERFACE AUDIT ===")
        
        # Loop through the interfaces list one by one
        for interface in interfaces_list:
            name = interface.get("name")
            status = interface.get("oper-status")
            
            # Audit the state and filter the output
            if status == "down":
                print(f"🛑 Alert: Interface {name} is currently DOWN!")
            else:
                print(f"✅ Interface {name} is healthy (UP).")
                
        print("=== 🏁 AUDIT COMPLETE ===")