from django.forms import Form, CharField, Textarea


class MethodFindForm(Form):
    method = CharField(max_length=255)


class AuthorizeForm(Form):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    password = CharField(max_length=64)


class AskForm(Form):
    text = CharField(widget=Textarea)
