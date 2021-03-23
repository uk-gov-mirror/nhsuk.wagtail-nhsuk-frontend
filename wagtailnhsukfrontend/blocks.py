from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    IntegerBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
    ListBlock,
    PageChooserBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class FlattenValueContext:
    """NHS.UK StructBlock mixin that flattens `value` for re-usability of templates"""

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context.update(value)
        return context


class ActionLinkBlock(FlattenValueContext, StructBlock):

    text = CharBlock(label="Link text", required=True)
    external_url = URLBlock(label="URL", required=False)
    new_window = BooleanBlock(required=False, label="Open in new window")
    internal_page = PageChooserBlock(label="Internal Page", required=False)

    class Meta:
        icon = 'link'
        template = 'wagtailnhsukfrontend/action_link.html'
        help_text = 'Enter a URL or select and Internal Page'

    def clean(self, value):

        errors = {}

        url_links = 0

        if value.get('external_url'):
            url_links += 1
        if value.get('internal_page'):
            url_links += 1

        if not url_links:
            errors['internal_page'] = ErrorList(['Please choose a page or enter a URL above.'])
            errors['external_url'] = ErrorList(['Please enter a URL or choose a page below.'])
        elif url_links > 1:
            errors['internal_page'] = ErrorList(['Please only enter a URL or choose a page.'])
            errors['external_url'] = ErrorList(['Please only enter a URL or choose a page.'])

        if errors:
            raise ValidationError('Validation error in ActionLinkBlock', params=errors)

        return super().clean(value)


class WarningCalloutBlock(FlattenValueContext, StructBlock):

    title = CharBlock(required=True, default='Important')
    visually_hidden_prefix = BooleanBlock(required=False, label='Visually hidden prefix', help_text='If the title doesn\'t contain the word \"Important\" select this to add a visually hidden \"Important\", to aid screen readers.')
    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'warning'
        template = 'wagtailnhsukfrontend/warning_callout.html'


class InsetTextBlock(FlattenValueContext, StructBlock):

    body = RichTextBlock(required=True)

    class Meta:
        icon = 'warning'
        template = 'wagtailnhsukfrontend/inset_text.html'


class PanelBlock(FlattenValueContext, StructBlock):

    label = CharBlock(required=False)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/panel.html'
        help_text = 'This component is now deprecated and will be removed from future versions, please use the feature card block'


class GreyPanelBlock(FlattenValueContext, StructBlock):

    label = CharBlock(label='heading', required=False)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=6.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'doc-full-inverse'
        template = 'wagtailnhsukfrontend/grey_panel.html'
        help_text = 'This component is now deprecated and will be removed from future versions, please use the feature card block'


class PanelListBlock(FlattenValueContext, StructBlock):

    panels = ListBlock(StructBlock([
        ('left_panel', PanelBlock()),
        ('right_panel', PanelBlock()),
    ]))

    class Meta:
        icon = 'list-ul'
        template = 'wagtailnhsukfrontend/panel_list.html'
        help_text = 'This component is now deprecated and will be removed from future versions, please use the card group block'


class DoBlock(FlattenValueContext, StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.')
    label = CharBlock(label='Heading', required=False, help_text='Adding a label here will overwrite the default of Do')
    do = ListBlock(RichTextBlock)

    class Meta:
        icon = 'tick'
        template = 'wagtailnhsukfrontend/do_list.html'


class DontBlock(FlattenValueContext, StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.')
    label = CharBlock(label='Heading', required=False, help_text='Adding a label here will overwrite the default of Don\'t')
    dont = ListBlock(RichTextBlock, label="Don't")

    class Meta:
        icon = 'cross'
        template = 'wagtailnhsukfrontend/dont_list.html'


class ImageBlock(FlattenValueContext, StructBlock):

    content_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=False, help_text="Only leave this blank if the image is decorative.")
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'wagtailnhsukfrontend/image.html'


class BasePromoBlock(FlattenValueContext, StructBlock):

    url = URLBlock(label="URL", required=True)
    heading = CharBlock(required=True)
    description = CharBlock(required=False)
    content_image = ImageChooserBlock(label="Image", required=False)
    alt_text = CharBlock(required=False)

    class Meta:
        icon = 'pick'
        template = 'wagtailnhsukfrontend/promo.html'
        help_text = 'Promo requires a URL entered or an Internal Page selected.'


class PromoBlock(BasePromoBlock):

    size = ChoiceBlock([
        ('', 'Default'),
        ('small', 'Small'),
    ], required=False)

    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.')

    class Meta:
        template = 'wagtailnhsukfrontend/promo.html'
        help_text = 'This component is now deprecated and will be removed from future versions, please use the card block'


class PromoGroupBlock(FlattenValueContext, StructBlock):

    column = ChoiceBlock([
        ('one-half', 'One-half'),
        ('one-third', 'One-third'),
    ], default='one-half', required=True)

    size = ChoiceBlock([
        ('', 'Default'),
        ('small', 'Small'),
    ], required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['num_columns'] = {
            'one-half': 2,
            'one-third': 3,
        }[value['column']]
        return context

    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.')

    promos = ListBlock(BasePromoBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/promo_group.html'
        help_text = 'This component is now deprecated and will be removed from future versions, please use the card group block'


class SummaryListRowBlock(StructBlock):

    key = CharBlock()

    value = RichTextBlock()


class SummaryListBlock(FlattenValueContext, StructBlock):

    rows = ListBlock(SummaryListRowBlock)
    no_border = BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'form'
        template = 'wagtailnhsukfrontend/summary_list.html'


class CardBasicBlock(FlattenValueContext, StructBlock):

    heading = CharBlock(required=True)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.')
    heading_size = ChoiceBlock(
        [
            ('', 'Default'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        help_text='The heading size affects the visual size, this follows the front-end library\'s sizing.',
        required=False
    )

    body = RichTextBlock(required=False)

    class Meta:
        label = 'Basic card'
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/card.html'


class CardClickableBlock(CardBasicBlock):

    internal_page = PageChooserBlock(label="Internal Page", required=False, help_text='Interal Page Link for the card')
    url = URLBlock(label="URL", required=False, help_text='External Link for the card')

    class Meta:
        label = 'Clickable card'
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/card.html'
        help_text = 'Clickable card requires an Internal page selected or a URL entered'

    def clean(self, value):

        errors = {}

        url_links = 0

        if value.get('url'):
            url_links += 1
        if value.get('internal_page'):
            url_links += 1

        if not url_links:
            errors['internal_page'] = ErrorList(['Please choose a page or enter a URL below.'])
            errors['url'] = ErrorList(['Please enter a URL or choose a page above.'])
        elif url_links > 1:
            errors['internal_page'] = ErrorList(['Please only enter a URL or choose a page.'])
            errors['url'] = ErrorList(['Please only enter a URL or choose a page.'])

        if errors:
            raise ValidationError('Validation error in ActionLinkBlock', params=errors)

        return super().clean(value)


class CardImageBlock(CardBasicBlock):

    content_image = ImageChooserBlock(label='Image', required=True)
    alt_text = CharBlock(required=True)
    url = URLBlock(label="URL", required=False, help_text='Optional, if there is a link the entire card will be clickable.')
    internal_page = PageChooserBlock(label="Internal Page", required=False, help_text='Optional, if there is a link the entire card will be clickable.')

    class Meta:
        label = 'Card with an image'
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/card.html'

    def clean(self, value):

        errors = {}

        url_links = 0

        if value.get('url'):
            url_links += 1
        if value.get('internal_page'):
            url_links += 1

        if url_links > 1:
            errors['internal_page'] = ErrorList(['Please only enter a URL or choose a page.'])
            errors['url'] = ErrorList(['Please only enter a URL or choose a page.'])

        if errors:
            raise ValidationError('Validation error in ActionLinkBlock', params=errors)

        return super().clean(value)


class CardFeatureBlock(FlattenValueContext, StructBlock):

    feature_heading = CharBlock(required=True)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.')
    heading_size = ChoiceBlock(
        [
            ('', 'Default'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        help_text='The heading size affects the visual size, this follows the front-end library\'s sizing.',
        required=False
    )

    body = RichTextBlock(required=True)

    class Meta:
        label = 'Feature card'
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/card.html'


class CardGroupBlock(FlattenValueContext, StructBlock):

    column = ChoiceBlock([
        ('', 'Full-width'),
        ('one-half', 'One-half'),
        ('one-third', 'One-third'),
    ], default='', required=False)

    class BodyStreamBlock(StreamBlock):
        card_basic = CardBasicBlock()
        card_clickable = CardClickableBlock()
        card_image = CardImageBlock()
        card_feature = CardFeatureBlock()

    body = BodyStreamBlock(required=True)

    class Meta:
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/card_collection.html'


class DetailsBlock(FlattenValueContext, StructBlock):

    # Define a BodyStreamBlock class in this way to make it easier to subclass and add extra body blocks
    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        panel = PanelBlock()
        feature_card = CardFeatureBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    title = CharBlock(required=True)
    body = BodyStreamBlock(required=True)

    class Meta:
        icon = 'collapse-down'
        template = 'wagtailnhsukfrontend/details.html'


class ExpanderBlock(DetailsBlock):

    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        grey_panel = GreyPanelBlock()
        feature_card = CardFeatureBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    # We need to override the body since expanders can have grey_panels instead of regular panels
    body = BodyStreamBlock(required=True)

    class Meta:
        icon = 'plus-inverse'
        template = 'wagtailnhsukfrontend/expander.html'


class ExpanderGroupBlock(FlattenValueContext, StructBlock):

    expanders = ListBlock(ExpanderBlock)

    class Meta:
        icon = 'plus-inverse'
        template = 'wagtailnhsukfrontend/expander_group.html'


class CareCardBlock(FlattenValueContext, StructBlock):

    type = ChoiceBlock([
        ('primary', 'Non-urgent'),
        ('urgent', 'Urgent'),
        ('immediate', 'Immediate'),
    ], required=True, default='primary',)
    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    title = CharBlock(required=True)

    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        details = DetailsBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        grey_panel = GreyPanelBlock()
        feature_card = CardFeatureBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    body = BodyStreamBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['accessible_title_prefix'] = {
            'primary': 'Non-urgent advice: ',
            'urgent': 'Urgent advice:',
            'immediate': 'Immediate action required:',
        }[value['type']]
        return context

    class Meta:
        icon = 'help'
        template = 'wagtailnhsukfrontend/care_card.html'
