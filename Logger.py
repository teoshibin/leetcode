class Logger:
    _instance = None

    @staticmethod 
    def getInstance():
        """Static access method."""
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        """Virtually private constructor."""
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def print_logs(self):
        print("\n".join(self.logs))
        self.logs.clear()
