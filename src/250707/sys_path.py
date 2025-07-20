if __name__ == "__main__":
    import sys

    print("sys.builtin_module_names")
    for name in sys.builtin_module_names:
        print(f"  - {name}")
    
    print("")
    print("sys.path:")
    for path in sys.path:
        print(f"  - {path}")
    
    print("")
    print("dir(sys)")
    for name in dir(sys):
        print(f"  - {name}")