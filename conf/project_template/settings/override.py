"""
override any swicth or config here, or declare a final variable here..
"""
def sort_by_weight(weighted_list):
    """ takes a weighted list and return list in order """
    sorted_list = []
    for entry in sorted(weighted_list):
        try:
            if len(entry):
                _, app_name = entry
                sorted_list.append(app_name)
        except ValueError as e:
            print("please define weighted_vaLues as =>> (3, 'value...') ")
            raise e
    return sorted_list




# now redefine installed apps.
INSTALLED_APPS = CORE_INSTALLED_APPS + sort_by_weight(WEIGHTED_INSTALLED_APPS) + INSTALLED_APPS

# now redefine installed apps.
MIDDLEWARE = CORE_MIDDLEWARE + sort_by_weight(WEIGHTED_MIDDLEWARE) + MIDDLEWARE
