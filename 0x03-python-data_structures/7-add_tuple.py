#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tupi = ()
    tupi1 = tuple_a + (0, 0)
    tupi2 = tuple_b + (0, 0)
    new_tupi = tupi1(0) + tupi2(0), tupi1(1) + tupi2(1)
    return(new_tupi)
