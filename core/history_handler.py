
import json
import os


class HistoryHandler:
    def __init__(self, json_file="history.json"):
        self.json_file = json_file
        self.last_problem = None
        self.last_solution = None
        self.last_type = None
        self._load()

    def _save(self):
        data = {
            "last_problem": self.last_problem,
            "last_solution": self.last_solution,
            "last_type": self.last_type,
        }
        with open(self.json_file, "w") as file:
            json.dump(data, file)

    def _load(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                data = json.load(file)
                self.last_problem = data.get("last_problem")
                self.last_solution = data.get("last_solution")
                self.last_type = data.get("last_type")

    def update(self, type, problem, solution):
        self.last_problem = problem
        self.last_solution = solution
        self.last_type = type
        self._save()
