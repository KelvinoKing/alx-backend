#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
You have to use this CSV file (same as the one presented at the top
of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset
correctly and return the appropriate page of the dataset (i.e.
the correct list of rows).
If the input arguments are out of range for the dataset, an empty
list should be returned.
"""
import math
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if end > (len(dataset)):
            return []
        return dataset[start:end]
