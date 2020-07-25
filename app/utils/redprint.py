"""
  *@ClassName redprint
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:26
  *@Version 1.0
 """
from flask import Blueprint

class RedPrint:

    def __init__(self, name):
        self.name = name
        self.param_list = []

    def route(self, rule, **options):
        """Like :meth:`Flask.route` but for a blueprint.  The endpoint for the
        :func:`url_for` function is prefixed with the name of the blueprint.
        """
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            self.param_list.append((rule, endpoint, f, options))
            return f
        return decorator

    def register_to(self, blueprint: Blueprint):
        for rule, endpoint, f, option in self.param_list:
            blueprint.add_url_rule(rule, endpoint, f, **option)