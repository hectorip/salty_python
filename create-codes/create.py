import uuid
def create_codes(count=10, prefix=""):
    codes = set()
    while len(codes) < count:
        code = str(uuid.uuid4()).split("-")[0][:4]
        codes.add(f"{prefix}-{code}")

    return codes

with open("jenny-codes.csv", "w") as f:
    f.write(str(create_codes(310, "JNY")))