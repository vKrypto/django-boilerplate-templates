from split_settings.tools import optional, include

include(
    'project.py',
    
    # include project settings..
    'default.py',
    'production/*.py',
    'development/*.py',

    # include in app settings.
    optional('../apps/*/settings/default.py'),
    optional('../apps/*/settings/production.py'),
    optional('../apps/*/settings/development.py'),
    
    # temp settings.
    optional('local_settings.py')
)