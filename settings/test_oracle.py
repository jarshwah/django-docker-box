DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'oracle-db:1521/xe',
        'USER': 'system',
        'PASSWORD': 'oracle',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
    'other': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'oracle-db:1521/xe',
        'USER': 'system',
        'PASSWORD': 'oracle',
        'TEST': {
            'USER': 'other_test',
            'TBLSPACE': 'other_test_tbls',
            'TBLSPACE_TMP': 'other_test_tbls_tmp',
        },
    },
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
