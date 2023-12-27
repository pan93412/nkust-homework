import httpx


class KkboxClient:
    access_token: str

    def __init__(self, client_id: str, client_secret: str):  # homework 1
        token_response = httpx.post(
            "https://account.kkbox.com/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        response_json = token_response.json()
        self.access_token = response_json["access_token"]

    def get_charts(self, territory: str = "TW") -> dict:  # homework 2
        response = httpx.get(
            "https://api.kkbox.com/v1.1/charts",
            headers={"Authorization": f"Bearer {self.access_token}"},
            params={"territory": territory},
        )

        return response.json()

    def get_track_from_chart(self, chart_id: str, territory: str = "TW") -> dict:  # homework 3
        response = httpx.get(
            f"https://api.kkbox.com/v1.1/charts/{chart_id}/tracks",
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            params={"territory": territory},
        )

        return response.json()
