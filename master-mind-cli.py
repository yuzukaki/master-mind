#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""数あてゲーム.

- 「答え」として3桁の数字をランダムで決定
- 各桁の数字は全部違う数字である
    - OK: 456
    - NG: 448
- 3桁の入力を行い、「答え」と比較する
- 比較して、桁も数字も一致していたらEATとする
- 桁が一致していない場合はBITEとする
- 比較結果のEATとBITEを返事する
    - 答え: 456 入力: 463  → 1EAT 1BITE
    - 答え: 456 入力: 671  → 0EAT 1BITE
"""
__author__ = 'uekiy'
__version__ = '0.01'
__date__ = '2019/11/01'


import random
import json


class Common:
    """ゲーム設定."""

    play_columns = 3
    is_debug = True

    def debug(self, obj):
        """Debug Print."""
        if self.is_debug is True:
            print(obj)


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


class MindLogic:
    """Mind Logic."""

    __lottery_box = None
    __answer_count = 0

    def __init__(self, lottery_box=None):
        """Constractor."""
        if lottery_box is None:
            lottery_box = LotteryBox()
        self.__lottery_box = lottery_box

    def answer_numbers(self, answer_numbers):
        """Answer logics."""
        self.__answer_count += 1
        play_columns = self.__lottery_box.get_play_columns()
        eat = 0
        bite = 0
        error = 0

        for i in range(play_columns):
            answer_number = answer_numbers[i]
            selected_numbers = self.__lottery_box.get_selected_numbers()
            if answer_number in selected_numbers:
                if selected_numbers.index(answer_number) == i:
                    eat += 1
                else:
                    bite += 1
            else:
                error += 1

        status = True
        if eat == play_columns:
            status = False

        return json.dumps({
            'count': self.__answer_count,
            'columns': play_columns,
            'eat': eat,
            'bite': bite,
            'error': error,
            'status': status,
        })

"""Main Logic."""
try:
    lottery_box = LotteryBox(Common.play_columns)
    mind_logic = MindLogic(lottery_box)
    loop_flag = True
    while loop_flag is True:
        input_answer = input("answer?:")
        return_hash = json.loads(mind_logic.answer_numbers(input_answer))
        print(return_hash)
        loop_flag = return_hash['status']
except Exception as e:
    print(e)
