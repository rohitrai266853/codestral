import requests

import json

class Codestral:

	api_key = ""

	base_url = "https://codestral.mistral.ai/v1/chat/completions"

	def get_response(self):

		messages = []

		while True:

			message = input("You: ").strip()

			if message == "exit":

				break

			messages.append({"role": "user", "content": message})

			data = {

				"model": "codestral-2501",

				"messages": messages
			}

			headers = {

				"Authorization": f"Bearer {self.api_key}",

				"Content-Type": "application/json"

			}

			response = requests.post(self.base_url, headers=headers, json=data)

			if response.status_code == 200:

				codestral_response = response.json()["choices"][0]["message"]["content"]

				messages.append({"role": "assistant", "content": codestral_response})

				print(f"Codestral: {codestral_response}")


			else:

				print("Error occured.")


codestral = Codestral()

codestral.get_response()
