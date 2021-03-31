DJDT = True

# checkout the configurat ion and settings: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

if DJDT:
    INSTALLED_APPS += ['debug_toolbar']
    INTERNAL_IPS = ['127.0.0.1']
    # add djdt middleware at top.
    WEIGHTED_MIDDLEWARE += [('0', 'debug_toolbar.middleware.DebugToolbarMiddleware')]