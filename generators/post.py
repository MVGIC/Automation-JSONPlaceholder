

class Post:

    def __init__(self):
        self.result = {}
        self.reset() # Можно не использовать reset(), тогда по умолчанию будет пустой объект возвращаться

    def set_user_id(self, user_id=13):
        self.result["userId"] = user_id
        return self

    def set_id(self, id=1337):
        self.result["id"] = id
        return self

    def set_title(self, title="new magic post"):
        self.result["title"] = title
        return self

    def set_body(self, body="test magic body"):
        self.result["body"] = body
        return self

    def reset(self):
        self.set_user_id()
        self.set_id()
        self.set_title()
        self.set_body()

    def build(self):
        return self.result
