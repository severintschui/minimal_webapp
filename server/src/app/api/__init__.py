import importlib
import pkgutil
import typing as t

from flask import Blueprint, Flask


def register_blueprints(app: Flask) -> t.List[Blueprint]:
    """ Iterate over all modules inside api folder and register all Blueprint instances """
    blueprints = []
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f'{__name__}.{module_name}')
        for obj_name in dir(module):
            obj = getattr(module, obj_name)
            if isinstance(obj, Blueprint):
                app.register_blueprint(obj)
                blueprints.append(obj)
    return blueprints
