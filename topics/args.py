# this is how we create an object in python
def save_user(**user):
    ali = ""
    print("user data :")
    print(f"id is {user['id']}")
    print(f"name is {user['name']}")
    print(f"phone is {user['phone']}")


save_user(id=54, name="alireza", phone="09117158746")
save_user(id=16, name="saman", phone="09116598777")
