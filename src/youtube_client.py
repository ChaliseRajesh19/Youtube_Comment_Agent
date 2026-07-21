import os
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request as GoogleRequest

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def get_session():
    creds = Credentials(
        token=None,
        refresh_token=os.environ["GOOGLE_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["GOOGLE_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        scopes=SCOPES,
    )

    # Get a fresh access token
    creds.refresh(GoogleRequest())

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {creds.token}"})

    return session


session = get_session()
BASE = "https://www.googleapis.com/youtube/v3"


def get_uploads_playlist_id():
    r = session.get(
        f"{BASE}/channels", params={"part": "contentDetails", "mine": "true"}
    )
    r.raise_for_status()
    return r.json()["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_channel_videos(playlist_id, max_results=10):
    r = session.get(
        f"{BASE}/playlistItems",
        params={
            "part": "snippet",
            "playlistId": playlist_id,
            "maxResults": max_results,
        },
    )
    r.raise_for_status()
    return [
        (i["snippet"]["resourceId"]["videoId"], i["snippet"]["title"])
        for i in r.json()["items"]
    ]


def get_new_comments(video_id):
    r = session.get(
        f"{BASE}/commentThreads",
        params={
            "part": "snippet",
            "videoId": video_id,
            "textFormat": "plainText",
            "order": "time",
        },
    )
    r.raise_for_status()
    return [
        (i["id"], i["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
        for i in r.json()["items"]
    ]


def reply_to_comment(comment_id, reply_text):
    body = {"snippet": {"parentId": comment_id, "textOriginal": reply_text}}
    r = session.post(f"{BASE}/comments", params={"part": "snippet"}, json=body)
    r.raise_for_status()
    print(f"Replied to comment {comment_id} with: {reply_text}")
