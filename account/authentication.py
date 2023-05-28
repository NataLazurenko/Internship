from django.contrib.auth.models import User
from account.models import Profile

def create_profile(backend, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:
    def authentication(self,request,username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNoExist, User.MultipleObjectReturned):
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNoExist:
            return None