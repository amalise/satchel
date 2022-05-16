from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

