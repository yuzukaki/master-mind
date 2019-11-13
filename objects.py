#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random

class LotteryBox:
    """抽選箱クラス."""

    __play_columns = 3
    __lottery_numbers = []
    __selected_numbers = []

    def __init__(self,
                 play_columns=3,
                 numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        """Constractor."""
        self.init_box(play_columns, numbers)

    def init_box(self,
                 play_columns=3,
                 numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        """Initialize Box."""
        self.__play_columns = play_columns
        self.__lottery_numbers = numbers
        self.__selected_numbers = []
        # loop in play columns.
        for i in range(self.__play_columns):
            self.__draw_lots()
        print(self.__selected_numbers)

    def __draw_lots(self):
        """Draw Lots."""
        lottery_index = random.randrange(len(self.__lottery_numbers))
        lottery_number = self.__lottery_numbers.pop(lottery_index)
        self.__selected_numbers.append(lottery_number)

    def get_selected_number(self, columns):
        """Get Selected Number."""
        return(self.__selected_numbers[columns])

    def get_play_columns(self):
        """Get Play Columns."""
        return(self.__play_columns)

    def get_selected_numbers(self):
        """Get Selected Numbers."""
        return(self.__selected_numbers)