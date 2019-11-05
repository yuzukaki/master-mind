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


class Common:
    """ゲーム設定."""

    playColumns = 3
    isDebug = True

    def debug(self, obj):
        """Debug Print."""
        if self.isDebug is True:
            print(obj)


class NumberBox:
    """抽選箱とロジック."""

    __playColumns = 3
    __lotteryNumberBox = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    __selectedNumbers = []

    def __init__(self, playColumns=3):
        """Constractor."""
        self.__playColumns = playColumns
        # loop in play columns.
        for i in range(self.__playColumns):
            self.__drawLots()
        print(self.__selectedNumbers)

    def __drawLots(self):
        """Draw Lots."""
        lotteryIndex = random.randrange(len(self.__lotteryNumberBox))
        lotteryNumber = self.__lotteryNumberBox.pop(lotteryIndex)
        self.__selectedNumbers.append(lotteryNumber)

    def getSelectedNumber(self, columns):
        """Get Selected Number."""
        return(self.__selectedNumbers[columns])

    def getPlayColumns(self):
        """Get Play Columns."""
        return(self.__playColumns)

    def getSelectedNumbers(self):
        """Get Selected Numbers."""
        return(self.__selectedNumbers)


class MindLogic:
    """Mind Logic."""

    __numberBox = None
    __answerCount = 0

    def __init__(self, numberBox=None):
        """Constractor."""
        if numberBox is None:
            numberBox = NumberBox()
        self.__numberBox = numberBox

    def answerNumbers(self, answerNumbers):
        """Answer logics."""
        self.__answerCount += 1
        playColumns = self.__numberBox.getPlayColumns()
        eat = 0
        bite = 0
        error = 0
        for i in range(playColumns):
            answerNumber = int(answerNumbers[i])
            selectedNumbers = self.__numberBox.getSelectedNumbers()
            if answerNumber in selectedNumbers:
                if selectedNumbers.index(answerNumber) == i:
                    eat += 1
                else:
                    bite += 1
            else:
                error += 1

        print("[" + str(self.__answerCount) + "] Eat:" + str(eat) +
              " Bite:" + str(bite) + " Error:" + str(error))

        if eat == playColumns:
            print("Comp!")
            return False
        else:
            return True


"""Main Logic."""
try:
    numberBox = NumberBox(Common.playColumns)
    mindLogic = MindLogic(numberBox)
    loopFlag = True
    while loopFlag is True:
        inputAnswer = input("answer?:")
        loopFlag = mindLogic.answerNumbers(inputAnswer)
except Exception as e:
    print(e)
