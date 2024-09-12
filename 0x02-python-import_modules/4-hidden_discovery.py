#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    module_name = "hidden_4"
    spec = importlib.util.spec_from_file_location(module_name, "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
