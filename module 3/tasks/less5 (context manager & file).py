class MyFile:
    def __init__(self, filename, w_or_r_mode):
        self.filename = filename
        self.mode = w_or_r_mode
        self.encoding = 'utf-8'

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyFile('mytext.txt', 'w') as file:
    file.write('Hello World!!')
