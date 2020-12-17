import json
import urllib.parse
import hashlib

wiki_prefix = "https://en.wikipedia.org/wiki/"

class CountryIterator:
    def __init__(self, file_name, write_file):
        with open(file_name, encoding='utf-8') as fh:
            self.file_parsed = json.loads(fh.read())

        self.write_file = open(write_file, "wb")
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if (self.counter < len(self.file_parsed)):
            to_write = urllib.parse.quote(wiki_prefix + 
                self.file_parsed[self.counter]["name"]["common"])
            self.write_file.write(
                (self.file_parsed[self.counter]["name"]["common"] + " - " + to_write + "\n")
                .encode('utf-8'))
            return 
        else:
            raise StopIteration

def print_md5(file_name="md5.txt"):
    read_file = open(file_name, "rb")
    for line in read_file:
        yield hashlib.md5(line.rstrip()).hexdigest()



if (__name__=="__main__"):
    for i in CountryIterator("countries.json", "countries_links.txt"):
        pass

    md5_hashes = [md5 for md5 in print_md5("md5.txt")]
    print(md5_hashes)

