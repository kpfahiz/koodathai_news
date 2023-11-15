import dj_database_url
import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("SECRET_KEY")
# DEBUG = os.environ.get("DEBUG")
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")
# Application definition
ALLOWED_HOSTS=['*']
SECRET_KEY = '0#@yo_%tu!7rws4wixepzy@e&uc*z!+(1z82@_auy)x0+9ppz3'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'posts',
    'marketing',
    'tinymce',
    'ckeditor',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_social_share',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary',
]
# CLOUDINARY_URL=os.environ.get("CLOUDINARY_URL")
# cloudinary.config( 
#   cloud_name = os.environ.get("cloud_name"),
#   api_key = os.environ.get("api_key"),
#   api_secret = os.environ.get("api_secret")
# )
CLOUDINARY_URL="cloudinary://875546584995193:6Gl_H-gFVq_I2Nx3SKPqD0RF4Zk@drd1nudhu"
cloudinary.config( 
  cloud_name = "drd1nudhu", 
  api_key = "875546584995193", 
  api_secret = "6Gl_H-gFVq_I2Nx3SKPqD0RF4Zk" 
)

SITE_ID = 1


CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

LOGIN_REDIRECT_URL = '/'

#ACCOUNT_ADAPTER = 'project.users.allauth.AccountAdapter'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StarCake.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'posts.context_processors.seo'
            
            ],
        },
    },
]

# TinyMCE
# TINYMCE_DEFAULT_CONFIG = {
#     'height': 360,
#     'width': 800,
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'silver',
#     'plugins': '''
#             textcolor save link image media preview codesample contextmenu
#             table code lists fullscreen  insertdatetime  nonbreaking
#             contextmenu directionality searchreplace wordcount visualblocks
#             visualchars code fullscreen autolink lists  charmap print  hr
#             anchor pagebreak
#             ''',
#     'toolbar1': '''
#             fullscreen preview bold italic underline | fontselect,
#             fontsizeselect  | forecolor backcolor | alignleft alignright |
#             aligncenter alignjustify | indent outdent | bullist numlist table |
#             | link image media | codesample |
#             ''',
#     'toolbar2': '''
#             visualblocks visualchars |
#             charmap hr pagebreak nonbreaking anchor |  code |
#             ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
#     'deprecation_warnings': False,
#     }

WSGI_APPLICATION = 'StarCake.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_blog2',
        'USER': 'postgres',
        'PASSWORD': 'asd123'
    }
}

database_url = os.environ.get("DATBASE_URL")
#DATABASES["default"] = dj_database_url.parse(database_url)
DATABASES["default"] =dj_database_url.parse("postgres://news_blog2_user:l8iVBpNTSUAlJX6AQNbF4o6XSrYWkcHU@dpg-ck8pl1vq54js73d36f6g-a.oregon-postgres.render.com/news_blog2")

SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
VENV_PATH = os.path.dirname(BASE_DIR)
# if DEBUG:
#     STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_in_env')]
# else:
#     STATIC_ROOT = os.path.join(VENV_PATH,'static_root')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_in_env')]
STATIC_ROOT = os.path.join(VENV_PATH,'static_root')
MEDIA_ROOT = os.path.join(VENV_PATH,'media_root')
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "800px",
    "selector": "textarea",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": '''undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft 
    aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor 
    backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | 
    fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | 
    a11ycheck ltr rtl | showcomments addcomment code''',
    "custom_undo_redo_levels": 10,
    "language": "en",  # To force a specific language instead of the Django current language.
}

#CKEditor 
CKEDITOR_BASEPATH =  '/static/ckeditor/ckeditor/'
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}