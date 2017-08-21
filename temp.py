text = ""

for i in range(7, 60):
    new_text = f"""
def prob_{i}():
    return 0


def test_{i}():
    assert soph.hash(prob_{i}()) == "bc0d0a22a7a46212135ed0ba77d22f3a"

"""
    text = text+new_text

print(text)

with open("test_project-euler.py","a") as f:
    f.write(text)
