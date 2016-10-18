from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from short_app.models import Bookmark, Click
from django.urls import reverse_lazy
from random import choice
from string import ascii_letters, digits
from django.http import HttpResponseRedirect

class BookmarkCreateView(CreateView):
    model = Bookmark
    success_url = reverse_lazy("bookmark_create_view")
    fields = ('title', 'description', 'url')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.short_url = ''
        for i in range(10):
            instance.short_url += choice(ascii_letters + digits)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmark_list"] = Bookmark.objects.all()
        return context


class ShortView(View):
    def get(self, request, short_url):
        full = Bookmark.objects.get(short_url=short_url)
        Click.objects.create(bookmark=full)
        return HttpResponseRedirect(full.url)
