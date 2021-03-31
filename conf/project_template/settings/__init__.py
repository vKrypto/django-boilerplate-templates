from split_settings.tools import optional, include

include(
    'project.py',
    
    # include project settings..
    'default.py',
    'production/*.py',
    'development/*.py',

    # include in app settings.
    optional('../*/settings/default.py'),
    optional('../*/settings/production.py'),
    optional('../*/settings/development.py'),
    
    # temp settings.
    optional('local_settings.py')
)