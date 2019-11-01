#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
数あてゲーム

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
'''
__author__  = 'uekiy'
__version__ = '0.01'
__date__    = '2019/11/01'

import random

'''
ゲーム設定
'''
class GameSetting:
  playColumns = 3
  isDebug = True



'''
抽選箱とロジック

-
'''
class NumberBox:
  __lotteryNumberBox  = [0,1,2,3,4,5,6,7,8,9]
  __selectedNumbers = []
  __answerCount = 0

  # constractor
  def __init__(self):
    # loop in play columns.
    for i in range(GameSetting.playColumns):
      self.__drawLots()
    print(self.__selectedNumbers)

  # Draw Losts
  def __drawLots(self):
    lotteryIndex  = random.randrange(len(self.__lotteryNumberBox))
    lotteryNumber = self.__lotteryNumberBox.pop(lotteryIndex)
    self.__selectedNumbers.append(lotteryNumber)

  # Get Selected Number
  # @param columns.
  def getSelectedNumber(self, columns):
    return(self.__selectedNumbers[columns])

  def answerNumbers(self, answerNumbers):
    self.__answerCount += 1
    eat = 0
    bite = 0
    error = 0
    for i in range(GameSetting.playColumns):
      answerNumber = int(answerNumbers[i])
      if answerNumber in self.__selectedNumbers:
        if self.__selectedNumbers.index(answerNumber) == i:
          eat += 1
        else:
          bite += 1
      else:
        error += 1


    print("[" + str(self.__answerCount) + "] Eat:" + str(eat) + " Bite:" + str(bite) + " Error:" + str(error))

    if eat == GameSetting.playColumns:
      print("Comp!")
      return False
    else:
      return True

try:
  numberBox = NumberBox()
  loopFlag = True
  while loopFlag == True:
    inputAnswer = input("answer?:")
    loopFlag = numberBox.answerNumbers(inputAnswer)
except Exception as e:
  print(e)
  #GameLib.error(e)