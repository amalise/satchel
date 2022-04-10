from django.db import models

from wagtail.core.models import Page


class TagIndexPage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        tag = request.GET.get('tag')
        blogposts = PostPage.objects.filter(tags__name=tag)
        context['blogposts'] = blogposts

        return context

