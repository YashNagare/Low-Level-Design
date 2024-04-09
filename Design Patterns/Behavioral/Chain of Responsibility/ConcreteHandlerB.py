
from Handler import Handler

class ConcreteHandlerB(Handler):
    
    def handle_request(self, request):
        if request == 'B':
            print("Handled by Handler B")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)