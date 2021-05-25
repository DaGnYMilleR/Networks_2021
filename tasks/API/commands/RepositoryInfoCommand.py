from API.RequestHandler import RequestHandler
import json


class RepositoryInfoCommand:
    def __init__(self):
        self.name = "repinf"

    def execute(self, args):
        answer = RequestHandler().send_request_and_get_result(self.create_get_request(args[0], args[1]))
        b = json.loads(answer[answer.find("{")::])
        if "message" in b.keys():
            print(f"error: {b['message']}")
            return
        print(f"name: {b['name']}")
        print(f"owner: {b['owner']['login']}")
        print(f"description: {b['description']}")
        print(f"created: {b['created_at']}")
        print(f"last update: {b['updated_at']}")
        print(f"size: {b['size']}")
        print(f"language: {b['language']}")
        print(f"forks count: {b['forks_count']}")
        print(f"subscribers_count: {b['subscribers_count']}")

    def create_get_request(self, owner, repo):
        return f"""
GET /repos/{owner}/{repo} HTTP/1.1\r
Host: api.github.com\r
Connection: Keep-Alive\r
user-agent: 'python'\r
owner: "{owner}"\r
repo: "{repo}"\r
"""