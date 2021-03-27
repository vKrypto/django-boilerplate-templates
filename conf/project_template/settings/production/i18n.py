# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
from django.utils.translation import gettext_lazy as _

CONTEXT_PROCESSORS +=['django.template.context_processors.i18n']

MIDDLEWARE +=['django.middleware.locale.LocaleMiddleware']

LANGUAGES = [
    ('bg', _('Bulgarian')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fa-ir', _('Persian (Iran)')),
    ('fr', _('French')),
    ('hu', _('Hungarian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('nb', _('Norwegian')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt-br', _('Portuguese (Brazil)')),
    ('ro', ('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('tr', _('Turkish')),
    ('uk', _('Ukrainian')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Chinese'))
]


LOCALE_PATHS = [BASE_DIR.joinpath('locale')]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

