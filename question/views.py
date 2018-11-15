from django.shortcuts import render, resolve_url, redirect
from question.forms import QuestionForm, CommentForm
from .models import Question
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def list(request):
    # 전체 목록을 보여주는 코드
    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    # return render(request, 'list.html', {'contacts': contacts})
    
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
    # return render(request,'question/create.html',{'form':form})
    
def detail(request,id):
    question = Question.objects.get(id=id)
    form = CommentForm(initial={'question':id})
    A = question.comment_set.all().filter(answer="A")
    B = question.comment_set.all().filter(answer="B")
    
    if len(A)+len(B) == 0:
        A_per = 0
        B_per = 0
    else:
        A_per = len(A) / (len(A) + len(B))*100
        B_per = len(B) / (len(A) + len(B))*100
    return render(request,'question/detail.html',{
        'question':question,
        'form':form,
        'A':A,
        'B':B,
        'A_per':A_per,
        'B_per':B_per
    })
    
def comment_create(request,id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = Question.objects.get(id=id)
            comment.save()
            return redirect(resolve_url('question:detail',id))
        pass
    else:
        return redirect(resolve_url('question:detail',id))
    return render(request,'question/detail.html',{'form':form})
    
def update(request,id):
    question = Question.objects.get(id=id)
    
    if request.method=='POST':
        # 업데이트로직
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('question:detail',id ))
    else:
        # 폼 보여주기
        form = QuestionForm(instance=question)
    return render(request, 'question/update.html',{'form':form, 'question':question})
    