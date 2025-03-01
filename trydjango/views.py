"""
To render html web pages
"""

from django.http import HttpResponse

name = "Sandman"

H1_STRING = f"""
<h1>Hello {name}</h1>
"""
P_STRING = f"""
<p>Hello {name}</p>
"""

HTML_STRING = H1_STRING + P_STRING

def home_view(request):
  """
  Take in a request (Django sends request)
  Return HTML as a response (We pick to return the response)
  """

  return HttpResponse(HTML_STRING)