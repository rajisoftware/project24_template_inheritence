from django.shortcuts import render

# Create your views here.
def tem_inheritence_parent(request):
    return render(request,'tem_inheritence_parent.html')
def tem_inheritence_child(request):
    return render(request,'tem_inheritence_child.html')
