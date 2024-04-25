from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    '''
        Security Warning: Don't use this in production environment.
        The class is aim to git rid of CSRF token during development and api test using different tools.
        We can ignore in production, coz, we dont need to SessionWiseAuthenitcation in production as we are using JWT.
        Strongly prohibitted..
    '''
    def enforce_csrf(self, request):
        pass