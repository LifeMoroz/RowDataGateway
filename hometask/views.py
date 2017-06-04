from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.method import MethodFinder
from app.news import NewsFinder
from app.question import Question, QuestionFinder
from app.student import UserFinder
from hometask.forms import MethodFindForm, AuthorizeForm, AskForm

USER_COOKIE = 'user_id'


def index(request):
    if request.COOKIES.get(USER_COOKIE):
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'index.html', {"form": AuthorizeForm()})


def auth(request):
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            user = UserFinder.find(first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   password=form.cleaned_data['password'])
            if not user:
                return render(request, 'fail.html', {'message': 'No such User'})
            redirect = HttpResponseRedirect(reverse('profile'))
            redirect.set_cookie(USER_COOKIE, user[0].id)
            return redirect
    else:
        form = AuthorizeForm()

    return render(request, 'index.html', {'form': form})


class ProfileController:
    @staticmethod
    def get(request):
        cookie = request.COOKIES.get(USER_COOKIE)
        user = None
        questions = None
        if cookie:
            users = UserFinder.find(id=cookie)
            if not users:
                return HttpResponseRedirect(reverse('index'))
            else:
                user = users[0]
            questions = QuestionFinder.find(student_id=user.id)
        return render(request, 'profile.html', {"user": user, "questions": questions})


def news_list(request):
    return render(request, 'news_list.html', {'news': NewsFinder.find()})


def method_list(request):
    object_list = None
    form = MethodFindForm()
    if request.GET.get('method'):
        form = MethodFindForm(data=request.GET)
        if form.is_valid():
            object_list = MethodFinder.find_by_title_part(form.cleaned_data['method'])
    if object_list is None:
        object_list = MethodFinder.find()

    return render(request, 'method_list.html', {"form": form, "object_list": object_list})


def ask(request):
    if request.method == 'GET':
        form = AskForm()
        return render(request, 'ask.html', {"form": form})
    elif request.method == 'POST':
        form = AskForm(data=request.POST)
        if form.is_valid():
            q = QuestionFinder.find()
            if q:
                new_id = max([x.id for x in q]) + 1
            else:
                new_id = 0
            Question(id=new_id, text=form.cleaned_data['text']).insert()
            return render(request, 'ask.html', {"message": 'Вопрос успешно зарегистрирован!'})
        return HttpResponseRedirect(reverse('ask'))