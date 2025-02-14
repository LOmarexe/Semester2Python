import pkgutil

modules = [module.name for module in pkgutil.iter_modules()]
print(modules)
