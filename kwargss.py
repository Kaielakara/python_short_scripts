def print_user(**kwargs):
    print(kwargs)

    if 'city' in kwargs:
        print(f"This user stays in {kwargs['city']}")

print_user(city='Ontario')