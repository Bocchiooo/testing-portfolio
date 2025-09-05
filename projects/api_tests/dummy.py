
# helper to create dummy Response-like objects for monkeypatching requests
class DummyResponse:
    def __init__(self, status_code=200, json_data=None, text_data=None):
        self.status_code = status_code
        self._json = json_data
        self.text = text_data or ""

    def json(self):
        if self._json is None:
            raise ValueError("No JSON")
        return self._json
