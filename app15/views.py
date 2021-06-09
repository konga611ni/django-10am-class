from django.shortcuts import render

def showIndex(request):
    return render(request,'index.html')

def loginCheck(request):
    user_name=request.POST.get("t1")
    password=request.POST.get("t2")
    if user_name == "pradeep" and password == "kumar":
        return render(request,"welcome.html")
    else :
        return render(request,"Error.html")
