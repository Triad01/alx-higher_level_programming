#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    
    try:

        print(value)

        return True

    except TypeError:   
            
        sys.stderr()
        
