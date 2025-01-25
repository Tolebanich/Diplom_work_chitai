import requests

token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjExMTM3LCJpYXQiOjE3Mzc3OTkzNDMsImV4cCI6MTczNzgwMjk0MywidHlwZSI6MjB9.MNlLKCZp5QsWatbzD3zVG0ID89ALQd_-X_5DtZGpbEg'


class CartApi:
    def __init__(self, url: str) -> None:
        self.url = url

    def add_to_cart(self, book_id) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": token
        }
        my_json = {
            "id": book_id, "adData": {"item_list_name": "search", "product_shelf": ""}
        }
        response = requests.post(self.url, json=my_json, headers=headers)
        return response

    def change_quantity(self, book_id, quantity) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": token
        }
        my_json = [{
            "id": book_id, "quantity": quantity
        }]
        response = requests.put(self.url, json=my_json, headers=headers)
        return response

    def delete_from_cart(self, book_id) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": token
        }
        response = requests.delete(f"{self.url}/product/{book_id}", headers=headers)
        return response

    def no_body(self) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": token
        }
        response = requests.post(self.url, headers=headers)
        return response
