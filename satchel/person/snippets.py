


"""
@register_snippet
class Person(index.Indexed, ClusterableModel):
    first_name = models.TextField("First name", max_length = 100)
    last_name = models.TextField("Last name", max_length = 100)
    job_title = models.TextField("Job title", max_length = 255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        related_name = '+',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ], "Name"),
        FieldPanel('job_title'),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    @property
    def thumbnail_image(self):
        if self.image:
            return self.image.get_rendition('fill-50x50').img_tag()
        return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
"""

"""
@register_snippet
class FooterText(models.Model):
    text = RichTextField()

    panels = [
        FieldPanel('text'),
    ]
"""
