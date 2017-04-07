from __future__ import unicode_literals

from django.db import models

# Create your models here.
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class BlogPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML'))
    ])

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body')
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        StreamFieldPanel('body')
    ]
class CodeBlock(blocks.TextBlock):
    class Meta:
        template = 'blocks/code.html'
        icon = 'code'
        label = 'Code'


class QuoteBlock(blocks.TextBlock):
    class Meta:
        template = 'blocks/quote.html'
        icon = 'openquote'
        label = 'Quote' body = StreamField([ ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('code', CodeBlock(icon='code')), ('quote', QuoteBlock(icon='openquote')), ('html', blocks.RawHTMLBlock(icon='site', label='HTML')) ])
