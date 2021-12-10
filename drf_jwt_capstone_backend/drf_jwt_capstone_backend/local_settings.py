# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-2#se2w2t^20h%7g6_6+(zztxlmz#99f*r(dgsri7@ip_8zov@'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'd3ilautsv8sm7d',
        'USER': 'hlqnsfwvgncvky',
        'PASSWORD': 'f20a67a1e4e85d9d388a7b2649fa3d9995c8b20b48509229c23e7bb40b051d4a',
        'HOST': 'ec2-44-193-111-218.compute-1.amazonaws.com',
        'PORT': '5432',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
