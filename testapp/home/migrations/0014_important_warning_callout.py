# Generated by Django 2.1.15 on 2021-01-15 13:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.field_block
import wagtail.core.fields
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Non-urgent'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('feature_card', wagtail.core.blocks.StructBlock([('feature_heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('visually_hidden_prefix', wagtail.core.blocks.BooleanBlock(help_text='If the title doesn\'t contain the word "Important" select this to add a visually hidden "Important", to aid screen readers.', label='Visually hidden prefix', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('feature_card', wagtail.core.blocks.StructBlock([('feature_heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('visually_hidden_prefix', wagtail.core.blocks.BooleanBlock(help_text='If the title doesn\'t contain the word "Important" select this to add a visually hidden "Important", to aid screen readers.', label='Visually hidden prefix', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('feature_card', wagtail.core.blocks.StructBlock([('feature_heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('visually_hidden_prefix', wagtail.core.blocks.BooleanBlock(help_text='If the title doesn\'t contain the word "Important" select this to add a visually hidden "Important", to aid screen readers.', label='Visually hidden prefix', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('do_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text='Adding a label here will overwrite the default of Do', label='Heading', required=False)), ('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('dont_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text="Adding a label here will overwrite the default of Don't", label='Heading', required=False)), ('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('feature_card', wagtail.core.blocks.StructBlock([('feature_heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('visually_hidden_prefix', wagtail.core.blocks.BooleanBlock(help_text='If the title doesn\'t contain the word "Important" select this to add a visually hidden "Important", to aid screen readers.', label='Visually hidden prefix', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('feature_card', wagtail.core.blocks.StructBlock([('feature_heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('visually_hidden_prefix', wagtail.core.blocks.BooleanBlock(help_text='If the title doesn\'t contain the word "Important" select this to add a visually hidden "Important", to aid screen readers.', label='Visually hidden prefix', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))]),
        ),
    ]
