from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from app.method import MethodFinder
from app.news import NewsFinder
from app.student import StudentFinder
from hometask.forms import MethodFindForm, AuthorizeForm, AskForm

USER_COOKIE = 'user_id'


class Index(generic.TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get(USER_COOKIE):
            return HttpResponseRedirect(reverse('profile'))
        return super(Index, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return {
            'form': AuthorizeForm()
        }


def auth(request):
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            user = StudentFinder.find(first_name=form.cleaned_data['first_name'],
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


def profile(request):
    cookie = request.COOKIES.get(USER_COOKIE)
    user = None
    if cookie:
        users = StudentFinder.find(id=cookie)
        if not users:
            return HttpResponseRedirect(reverse('index'))
        else:
            user = users[0]
    return render(request, 'profile.html', {"user": user})


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
    form = AskForm()
    if request.method == 'GET':
        return render(request, 'ask.html', {"form": form})
    elif request.method == 'POST':
        return render(request, 'ask.html', {"message": 'Вопрос успешно зарегистрирован!'})
