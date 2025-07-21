from os import environ
for key in ('DJANGO_SETTINGS_MODULE', 'SECRET_KEY'):
    print(f"{key:<25}  {environ.get(key)}")