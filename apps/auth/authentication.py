from rest_framework.authentication import SessionAuthentication

class SessionCsrfExemptAuthentication(SessionAuthentication):
    
    def enforce_csrf(self, request):
        # return super().enforce_csrf(request)
        pass