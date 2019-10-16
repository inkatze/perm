import urllib.request
import json

def permutation(number: str):
    chars = list(number)
    if len(chars) < 2:
        return ''.join(chars)

    results = []
    for i in range(0, len(chars)):
        current = chars[:]
        result = [current.pop(i)]
        subperm = permutation(current)
        for s in subperm:
            result.append(s)
        results.append(result)
    return results


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='/perms'>Trigger</a>"


@app.route("/perms")
def perms():
    response = urllib.request.urlopen('https://csrng.net/csrng/csrng.php?min=0&max=10000')
    data = response.read().decode('utf-8')
    data = json.loads(data)
    value = str(data.pop()['random'])

    results = permutation(value)
    for r in results:
        print(r)
    return str(results)

if __name__ == "__main__":
    app.run()
