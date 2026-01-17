# fetch a random user and print details like name, country, age, email and dob, gender

import requests
import datetime

ENDPOINT = "https://randomuser.me/api/"


try:
    response = requests.get(ENDPOINT)
    data = response.json()

    person = ((data["results"])[0])

    gender = person["gender"]
    name = (person["name"]).values()
    full_name = " ".join(i.capitalize() for i in name)
    country = (person["location"])["country"]
    email = person["email"]
    phone = person["phone"]

    dob = person["dob"]["date"]
    age = person["dob"]["age"]
    dob_obj = datetime.datetime.fromisoformat(dob.replace("Z", ""))
    formatted_date = dob_obj.strftime("%d %b %Y")

    print("\n" + "=" * 40)
    print("        RANDOM USER PROFILE")
    print("=" * 40)
    print(f"Name     : {full_name}")
    print(f"Gender   : {gender}")
    print(f"Age      : {age}")
    print(f"DOB      : {formatted_date}")
    print(f"Email    : {email}")
    print(f"Phone    : {phone}")
    print(f"Country  : {country}")
    print("=" * 40)

except requests.exceptions.RequestException as e:
    print("Network error:", e)

except KeyError as e:
    print("Unexpected API response. Missing key:", e)

except Exception as e:
    print("Something went wrong:", e)
 