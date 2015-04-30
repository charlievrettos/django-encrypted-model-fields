# About

`django-cryptographic-fields` is set of fields that wrap standard Django fields with encryption provided by the python cryptography library. These fields are much more compatible with a 12-factor design since they take their encryption key from the settings file instead of a file on disk used by `keyczar`.

While keyczar is an excellent for encryption, its not compatible with Python 3, and it requires, for hosts like Heroku, that you either check your key file into your git repository for deployment, or implement manual post-deployment processing to write the key stored in an environment variable into a file that keyczar can read.

# Getting Started

```shell
$ pip install django-cryptographic-fields
```

Add "cryptographic_fields" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = (
    ...
    'cryptographic_fields',
)
```

`django-cryptographic-fields` expects the encryption key to be specified using `FIELD_ENCRYPTION_KEY` in your project's `settings.py` file. For example, to load it from the local environment:

```python
import os

FIELD_ENCRYPTION_KEY = os.environ.get('FIELD_ENCRYPTION_KEY', '')
```

To use an encrypted field in a Django model, use one of the fields from the `cryptographic_fields` module:

```python
from cryptographic_fields.fields import EncryptedCharField

class EncryptedFieldModel(models.Model):
    encrypted_char_field = EncryptedCharField(max_length=100)
```

For fields that require `max_length` to be specified, the `Encrypted` variants of those fields will automatically increase the size of the database field to hold the encrypted form of the content. For example, a 3 character CharField will automatically specify a database field size of 100 characters when EncryptedCharField(`max_length=3`) is specified.

Due to the nature of the encrypted data, filtering by values contained in encrypted fields won't work properly. Sorting is also not supported.
