from langchain.llms import OpenAI
from langchain.chains import APIChain

swapi_docs = """
API documentation:
Endpoint: https://swapi.dev/api

GET /people/?search={name}
This API is for searching Star Wars characters by their name.
The {name} param is the Star Wars character's name.

Response schema (JSON object):
results | JSON object | Object representing the Star Wars character/people attributes.

Every object in the "results" previous response has this schema (JSON object):
name | string | The character's name.
height | string | The character's height.
eye_color | string | The character's eye color.
"""

class IA():
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.chain = APIChain.from_llm_and_api_docs(self.llm, swapi_docs, verbose=True)

    def complete(self, prompt):
        response = self.chain.run(prompt)
        return response