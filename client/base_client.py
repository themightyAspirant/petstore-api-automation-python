import requests


class BaseClient:
    def __init__(self, base_url: str):
        self._base_url = base_url

    def _make_request(self, method, endpoint: str, **kwargs):
        url = f"{self._base_url}/{endpoint.lstrip('/')}"

        self.logger.info(f"Making {method} request to {url} with kwargs: {kwargs}")
        
        try:
            response = requests.request(method, url, **kwargs)
            self.logger.info(f"Response: {response.status_code}")
            self.logger.debug(f"Response: {response.text}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error making {method} request to {url}: {e}")
            raise e

    def get(self, endpoint: str, **kwargs):
        return self._make_request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._make_request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._make_request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._make_request("DELETE", endpoint, **kwargs)