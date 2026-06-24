import requests

# Your live production API gateway URL
API_URL = "https://drnwdjxrxj.execute-api.eu-central-1.amazonaws.com/counter"

def test_visitor_counter_lifecycle():
    print("🚀 Starting Serverless API Smoke Tests...\n")
    
    # -----------------------------------------------------------------
    # TEST 1: Standard Execution & Verification
    # -----------------------------------------------------------------
    print("[TEST 1] Sending a valid execution ping...")
    response1 = requests.post(API_URL)
    
    assert response1.status_code == 200, f"Expected HTTP 200, got {response1.status_code}"
    data1 = response1.json()
    assert "count" in data1, "Response structure missing 'count' variable."
    
    count_first = data1["count"]
    print(f"✅ Success! Base count retrieved: {count_first}")
    
    # -----------------------------------------------------------------
    # TEST 2: Verifying Database Mutation State
    # -----------------------------------------------------------------
    print("\n[TEST 2] Verifying database atomic increments...")
    response2 = requests.post(API_URL)
    count_second = response2.json()["count"]
    
    # The new count MUST be exactly 1 greater than the previous fetch
    assert count_second == count_first + 1, f"Database did not increment sequentially! {count_first} -> {count_second}"
    print(f"✅ Success! Database verified mutated from {count_first} to {count_second}")
    
    # -----------------------------------------------------------------
    # TEST 3: Robustness against Malformed Payloads
    # -----------------------------------------------------------------
    print("\n[TEST 3] Sending unexpected/malformed data payloads...")
    bad_payload = {"corrupted_key": "malicious_string_xyz", "number": -9999}
    
    response3 = requests.post(API_URL, json=bad_payload)
    assert response3.status_code == 200, "API crashed on malformed payload input!"
    
    count_third = response3.json()["count"]
    assert count_third == count_second + 1, "API failed to process normal sequence when receiving noise."
    print(f"✅ Success! API ignored bad payload input and processed cleanly. Counter is now: {count_third}")
    
    print("\n🎉 ALL SMOKE TESTS PASSED PERFECTLY!")

if __name__ == "__main__":
    test_visitor_counter_lifecycle()
