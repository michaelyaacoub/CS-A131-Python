def box_string(contents:str) -> None :
    """prints roof over your top"""
    n = len(contents)
    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))    
#box_string("Hello")
