#!/usr/bin/env python3
"""
Pagination helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Səhifə nömrəsi və səhifə ölçüsünə əsasən
    başlanğıc və bitiş indekslərini ehtiva edən tuple qaytarır.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    
    return (start_index, end_index)
