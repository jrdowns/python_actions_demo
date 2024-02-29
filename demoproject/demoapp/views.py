# Import the HttpResponse class from the django.http module.
from django.http import HttpResponse

def polo_view(request): # pylint: disable=unused-argument
    """
    A view function that returns a response with the text "Polo".

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The HTTP response object with the text "Polo".
    """
    return HttpResponse("Polo")
