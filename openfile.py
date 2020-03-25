#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
from factoriel import factoriel
print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("content-type: text/html\n\n" )



e = open('tost.php')
content = e.read()
print(content)
print("<br><B>hello python on github</B>")
num = 4
print("The factorial of", num, "is", factoriel(num))