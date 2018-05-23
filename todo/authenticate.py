from django.contrib.auth.models import User


# Two functions required to authenticate users with their email address instead of a username.
class EmailAuthenticationBackend(object):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)     # We ask the application to see if username entered = email
        except User.MultipleObjectsReturned:    # In case we have more than one email that is the same choose first one
            user = User.objects.filter(email=username).first()
        except User.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password): # If user is active and their password matches
            return user                                                  # return them to function caller
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
