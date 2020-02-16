class Strip:
    def __init__(self, characters):
        self.characters = characters

    def __call__(self, string):
        return string.strip(self.characters)


strip_punctuation = Strip(characters=",;:.!?")
strip_punctuation("Land ahoy!")  # returns: 'Land ahoy'

# alternative for functors is closure


def make_strip_function(characters):
    def strip_function(string):
        return string.strip(characters)

    return strip_function


strip_punctuation = make_strip_function(",;:.!?")
strip_punctuation("Land ahoy!")  # returns: 'Land ahoy'
