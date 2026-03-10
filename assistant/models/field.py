class Field:
    def __init__(self, value):
        self.value = value.strip()
        self.validate()

    def validate(self):
        pass

    def __str__(self):
        return str(self.value)