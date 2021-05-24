import os
import sys

sys.path.append("library")
import nltk


#分かち書き，品詞の種類を取得←分析に必要
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")


#このスクリプト自身のパスを取得し，カレントディレクトリとして指定
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def word(num):
  sentence = open("data/outcontents_"+str(num)+".txt", "r", encoding="UTF-8")
  data = sentence.read()

  #形態素ごとにに分割
  tokens = nltk.word_tokenize(data)

  #品詞のタグ付け
  tagged = nltk.pos_tag(tokens)

  #形容詞，名詞，動詞のそれぞれのタグ
  parts_JJ=["JJ","JJR","JJS",#形容詞，形容詞：比較級，形容詞：最上級 
            ]
  parts_NN=["NN","NNS","NNP","NNPS",#名詞，名詞：複数形，固有名詞，固有名詞：複数形
           ]
  parts_VB=["VB","VBD","VBG","VBN","VBP","VBZ"#動詞原型，過去形，動名詞，過去分詞，三人称以外の現在形，三人称の単数形
            ]

  #形容詞の抽出
  tagged_JJ=[]

  for i in range(len(parts_JJ)):
    for j in range(len(tagged)):
      if tagged[j][1]==parts_JJ[i]:
        tagged_JJ.append(tagged[j])


  #名詞の抽出
  tagged_NN=[]

  for i in range(len(parts_NN)):
    for j in range(len(tagged)):
      if tagged[j][1]==parts_NN[i]:
        tagged_NN.append(tagged[j])


  #動詞の抽出
  tagged_VB=[]

  for i in range(len(parts_VB)):
    for j in range(len(tagged)):
      if tagged[j][1]==parts_VB[i]:
        tagged_VB.append(tagged[j])


  #外部に出力
  import csv

  with open("data/tagged"+str(num)+"_JJ.txt", "w", encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerows(tagged_JJ)

  with open("data/tagged"+str(num)+"_NN.txt", "w", encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerows(tagged_NN)

  with open("data/tagged"+str(num)+"_VB.txt", "w", encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerows(tagged_VB) 

  f.close()


for i in range(1,4):
  word(i)
