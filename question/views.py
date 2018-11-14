from django.shortcuts import render, resolve_url, redirect
from question.forms import QuestionForm, CommentForm
from .models import Question

# Create your views here.
def list(request):
    # 전체 목록을 보여주는 코드
    questions = Question.objects.all()
    return render(request,'question/list.html',{'questions':questions})
    
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
    
def detail(request,id):
    question = Question.objects.get(id=id)
    form = CommentForm()
    return render(request,'question/detail.html',{'question':question,'form':form})
    
def comment_create(request,id):
    if request.method == "POST":
        pass
    else:
        return redirect(resolve_url('question:detail',id))
    return render(request,'question/detail.html',{'form':form})