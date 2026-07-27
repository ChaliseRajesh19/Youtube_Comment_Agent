import requests

API = "http://localhost:8000"


def get_comments():
    response = requests.post(f"{API}/poll")
    if response.status_code == 200:
        return response.json()
    else:
        return []


def approve_comment(thread_id, final_reply):
    response = requests.post(
        f"{API}/approve/{thread_id}", json={"edited_reply": final_reply}
    )
    return response.status_code == 200


def reject_comment(thread_id):
    response = requests.post(f"{API}/reject/{thread_id}")
    return response.status_code == 200
