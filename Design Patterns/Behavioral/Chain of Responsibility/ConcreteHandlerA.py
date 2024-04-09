
from Handler import Handler

class ConcreteHandlerA(Handler):
    
    def handle_request(self, request):
        if request == 'A':
            print("Handled by Handler A")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)