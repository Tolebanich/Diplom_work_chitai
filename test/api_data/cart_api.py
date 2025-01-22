import requests
import json

class CartApi:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def add_to_cart(self, book_id) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjExMTM3LCJpYXQiOjE3Mzc1MjE4ODQsImV4cCI6MTczNzUyNTQ4NCwidHlwZSI6MjB9.boYplY3lU4qgPCyWH_QzID2eEI10yJs65DnM0x2C_UU"
        }
        my_json = {
            "book_id": book_id,
        }
        response = requests.post(self.url, json=my_json, headers=headers)
        return response

    def change_quantity(self, book_id, quantity) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjExMTM3LCJpYXQiOjE3Mzc1MjE4ODQsImV4cCI6MTczNzUyNTQ4NCwidHlwZSI6MjB9.boYplY3lU4qgPCyWH_QzID2eEI10yJs65DnM0x2C_UU"
        }
        my_json = {
            "book_id": book_id,
            "quantity": quantity
        }
        response = requests.put(self.url, json=my_json, headers=headers)
        return response

    def delete_from_cart(self, book_id) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjExMTM3LCJpYXQiOjE3Mzc1MjE4ODQsImV4cCI6MTczNzUyNTQ4NCwidHlwZSI6MjB9.boYplY3lU4qgPCyWH_QzID2eEI10yJs65DnM0x2C_UU"
        }
        response = requests.delete(f"{self.url}/product/{book_id}", headers=headers)
        return response

    def no_body(self) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjExMTM3LCJpYXQiOjE3Mzc1MjE4ODQsImV4cCI6MTczNzUyNTQ4NCwidHlwZSI6MjB9.boYplY3lU4qgPCyWH_QzID2eEI10yJs65DnM0x2C_UU"
        }
        response = requests.post(self.url, headers=headers)
        return response