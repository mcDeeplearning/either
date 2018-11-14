from django.shortcuts import render, resolve_url, redirect
from question.forms import QuestionForm

# Create your views here.
def list(request):
    return render(request,'question/list.html')
    
def create(request):
    if request.method == "POST":
        # 데이터를 저장
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('question:list'))
    else:
        # 사용자에게 폼을 전달
        form = QuestionForm()
    return render(request,'question/create.html',{'form':form})
    
    