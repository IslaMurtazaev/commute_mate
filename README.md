```
python manage.py shell
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.first()  # or get a specific user
token = Token.objects.create(user=user)
print(token.key)
```
