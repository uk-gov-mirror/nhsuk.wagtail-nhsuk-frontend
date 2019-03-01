from django import forms


class BigForm(forms.Form):
    """
    A form that can test each type of input in the frontend library.
    """

    # input
    national_insurance = forms.CharField(label="National Insurance number", max_length=7)

    # textarea
    more_detail = forms.CharField(label="Can you provide more detail?", widget=forms.Textarea)

    # radios
    name_changed = forms.ChoiceField(
        choices=[
            ('yes', 'Yes'),
            ('no', 'No')
        ],
        label="Have you changed your name?",
        widget=forms.RadioSelect,
    )

    # checkboxes
    nationality = forms.MultipleChoiceField(
        choices=[
            ('british', 'British'),
            ('irish', 'Irish'),
            ('other', 'Citizen of another country'),
        ],
        label="What is your nationality?",
        widget=forms.CheckboxSelectMultiple,
    )

    # select
    select = forms.ChoiceField(
        choices=[
            ('choice1', 'Choices 1'),
            ('choice2', 'Choice 2'),
            ('choice3', 'Choice 3'),
        ]
    )
