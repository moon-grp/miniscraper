import re
import requests
from flask import Flask

app = Flask(__name__)


url ="https://www.google.com/search?q=site%3Ainstagram.com+%22football%22+%22fifa%22+%22%40gmail.com%22&oq=site%3Ainstagram.com+%22football%22+%22fifa%22+%22%40gmail.com%22&aqs=chrome..69i57j69i58.78473j0j15&sourceid=chrome&ie=UTF-8"

e_rege= r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

for i in re.findall(e_rege, r.text):
    print(i)


if __name__ == "__main__":
    app.run(debug=True)
