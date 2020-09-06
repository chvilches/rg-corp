from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imp = False
        self.data = []
        self.reset()

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.imp = True

    def handle_endtag(self, tag):
        if tag == "tr":
            self.imp = False

    def handle_data(self, data):
        if self.imp:
            self.data.append(data)

    def get_currency(self, currency):
        key_num = 0
        is_currency = False
        for value in self.data:
            key_num += 1
            if key_num == 2:
                if value == currency:
                    is_currency = True
            if key_num == 4:
                if is_currency:
                    return value

            if key_num == 7:

                key_num = 0

        return ''