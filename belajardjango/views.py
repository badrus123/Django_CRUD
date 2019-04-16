from django.http import HttpResponse,HttpResponseRedirect

#class Home
# def home(request):
#     print(dir(request))
#     print(request.get_full_path())
#     return HttpResponse("<H1>Hello World</H1>")

def home(request):
    response = HttpResponse(content_type='application/json')
    response = HttpResponse(content_type='text/html')   
    response.content = ("<H1> Page not Found </H1>")
    #response.write("page not found")
    print (response.status_code)
    print (dir(response))
    response.status_code = 200
    
    return response

def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")