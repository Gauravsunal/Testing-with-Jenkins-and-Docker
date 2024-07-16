from django.conf.urls import url
from django.http import HttpResponse

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__

def home(request):
    color = request.GET.get('color', '')
    return HttpResponse('<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>')

def about(request):
    title = webapp
    author = ‘xyz’
    html = '''<!DOCTYPE html>
    <html>
    <head>
      <title>''' + title + '''</title>
    </head>
    <body>
        <h1>About ''' + title + '''</h1>
        <p>This Website was developed by ''' + author + '''.</p>
    </body>
    </html>'''
    return HttpResponse(html)

urlpatterns = [
    url(r'^$', home),
    url(r'^about/$', about),
]

