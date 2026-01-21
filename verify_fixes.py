# import requests
# import time

# base_url = "http://localhost:5000"

# def check_endpoint(endpoint):
#     try:
#         response = requests.get(f"{base_url}{endpoint}")
#         print(f"Checking {endpoint}: {response.status_code}")
#         # print(response.json())
#         return response.status_code == 200
#     except Exception as e:
#         print(f"Error checking {endpoint}: {e}")
#         return False

# print("Verifying Server and Admin APIs...")
# api_checks = [
#     "/api/dashboard-data",
#     "/api/admin/users",
#     "/api/admin/surveys",
#     "/api/admin/stats"
# ]

# all_passed = True
# for endpoint in api_checks:
#     if not check_endpoint(endpoint):
#         all_passed = False

# if all_passed:
#     print("✅ All verifications passed!")
# else:
#     print("❌ Some verifications failed.")
