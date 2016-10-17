from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from short_app.models import Bookmark, Click
from django.urls import reverse_lazy


class URLCreateView(CreateView):
    model = Bookmark
    success_url = reverse_lazy("url_create_view")
    fields = ('title', 'description', 'url')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)
