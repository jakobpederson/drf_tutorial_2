# Using ModelSerializers
# Our SnippetSerializer class is replicating a lot of information that's also contained in the Snippet model. It would be
# nice if we could keep our code a bit more concise.

# In the same way that Django provides both Form classes and ModelForm classes, REST framework includes both Serializer
# classes, and ModelSerializer classes.

# Let's look at refactoring our serializer using the ModelSerializer class. Open the file snippets/serializers.py again,
# and replace the SnippetSerializer class with the following.

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


# One nice property that serializers have is that you can inspect all the fields in a serializer instance, by printing
# its representation. Open the Django shell with python manage.py shell, then try the following:

# It's important to remember that ModelSerializer classes don't do anything particularly magical, they are simply a
# shortcut for creating serializer classes:
#     * An automatically determined set of fields.
#     * Simple default implementations for the create() and update() methods.
