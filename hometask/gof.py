from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.question import QuestionFinder
from app.student import UserFinder
from hometask.views import USER_COOKIE


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