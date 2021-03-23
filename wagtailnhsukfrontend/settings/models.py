from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class HeaderSettings(ClusterableModel, BaseSetting):
    service_name = models.CharField(max_length=255, blank=True)
    service_long_name = models.BooleanField(default=False)
    service_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='service_link',
    )

    transactional = models.BooleanField(default=False)

    logo_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    logo_aria = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Aria label override for the NHS logo."
    )
    logo_custom = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    show_search = models.BooleanField(default=False)

    organisation_name = models.CharField(max_length=255, blank=True)
    organisation_split_name = models.CharField(max_length=255, blank=True)
    organisation_descriptor = models.CharField(max_length=255, blank=True)
    organisation_white = models.BooleanField(default=False)

    panels = [
        MultiFieldPanel([
            PageChooserPanel('logo_link'),
            FieldPanel('logo_aria'),
            ImageChooserPanel('logo_custom'),
            FieldPanel('show_search'),
        ], heading="General"),
        MultiFieldPanel([
            FieldPanel('service_name'),
            FieldPanel('service_long_name'),
            PageChooserPanel('service_link'),
            FieldPanel('transactional'),
        ], heading="Service header"),
        MultiFieldPanel([
            FieldPanel('organisation_name'),
            FieldPanel('organisation_split_name'),
            FieldPanel('organisation_descriptor'),
            FieldPanel('organisation_white'),
        ], heading="Organisational header"),
        InlinePanel('navigation_links', heading="Navigation"),
    ]


class NavigationLink(Orderable):
    setting = ParentalKey(
        HeaderSettings,
        on_delete=models.CASCADE,
        related_name='navigation_links',
    )
    label = models.CharField(max_length=255)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('label'),
        PageChooserPanel('page'),
    ]


@register_setting
class FooterSettings(ClusterableModel, BaseSetting):

    panels = [
        InlinePanel(
            'footer_links',
            label="Footer Links",
            help_text="There is a minimum of 1 link and a maximum of 9 ",
            min_num=1,
            max_num=9
        )
    ]


class FooterLinks(Orderable):

    setting = ParentalKey(
        FooterSettings,
        on_delete=models.CASCADE,
        related_name='footer_links',
    )
    link_url = models.URLField(blank=True)
    link_label = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('link_url'),
        FieldPanel('link_label'),
    ]
