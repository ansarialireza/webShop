from django.shortcuts import render


#----------------------------------------------------------------------------------------------
def HomePage(request):
    print("--------------------------")
    return render(request,'facades/landing.html')
#----------------------------------------------------------------------------------------------
