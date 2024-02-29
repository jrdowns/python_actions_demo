"""
This module contains the views for the demoapp.

The views in this module handle the HTTP requests and return the corresponding HTTP responses.
"""

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
