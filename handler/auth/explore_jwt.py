import jwt
import datetime

base = {
    "exp": datetime.datetime.now() + datetime.timedelta(days=1),
    "iat": datetime.datetime.now(),
    "iss": "huangshan",
    "data": {
        "hello": "world"
    }
}

s = jwt.encode(base, "secret", algorithm="HS256")

print("s", s)

s = jwt.decode(s, "secret", issuer="huangshan", algorithms=["HS256"])

print(s)
print(type(s))
