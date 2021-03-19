import importlib.util
import inspect
import sys


def _import_by_path(name: str, location: str):
    spec = importlib.util.spec_from_file_location(name, location)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _get_importer():
    for frameinfo in inspect.stack():
        if frameinfo.filename == __file__:
            continue

        module = inspect.getmodule(frameinfo.frame)
        if module:
            return module


importer = _get_importer()
if importer.__name__ == "__main__":
    main_module = _import_by_path("Import Main Again!", importer.__file__)
    main_function = getattr(main_module, "main", None)
    if not main_function:
        raise RuntimeError(f"Could not find main function.")

    sys.exit(main_function())
