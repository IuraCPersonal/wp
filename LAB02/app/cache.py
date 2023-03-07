class Cache:
    def __init__(self):
        self.history = []
        self.current_pos = -1

    def add_url(self, url):
        # Add the new URL to the end of the history list
        self.history.append(url)
        # Set the current position to the end of the list
        self.current_pos = len(self.history) - 1

    def back(self):
        if self.current_pos > 0:
            # If we're not already at the beginning of the history, move back one position
            self.current_pos -= 1
            return self.history[self.current_pos]
        else:
            # If we're already at the beginning, return the current URL
            return self.history[self.current_pos]

    def forward(self):
        if self.current_pos < len(self.history) - 1:
            # If we're not already at the end of the history, move forward one position
            self.current_pos += 1
            return self.history[self.current_pos]
        else:
            # If we're already at the end, return the current URL
            return self.history[self.current_pos]
