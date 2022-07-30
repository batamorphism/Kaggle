# AI4Code

https://www.kaggle.com/competitions/AI4Code/discussion

## Hint for a simple but stronger pairwise model baseline

* 事前トレーニングするとスコアが0.01上がった
* CLSを使うのは適していないので、average poolingを使うのが良い
* rankを生成するより良い方法を考えたい
* PairWiseモデルの場合、Global contextからの情報が不足する。
  * PairWiseモデル: 2つのBERTモデルをそれぞれ持たせたもの
  * Global context: markdownとpythonの2つを合わせた、全体の構造

https://www.kaggle.com/competitions/AI4Code/discussion/327197

## Ideas for Generating New Data

* Code -> Commentsに変換するにはDoclyが使える
* Comments -> Codeに変換するにはGitHub Copilotが使える

https://www.kaggle.com/competitions/AI4Code/discussion/324554

## Difference between 'ancestor' and 'parent'

* ancestorは1つ前の元となったブックを指す
* A -> B -> C
* A -> D -> E
* この場合、CとEの祖先はAとなる
* なお、テストデータには含まれていないので注意する（CVの分割のためにある）

https://www.kaggle.com/competitions/AI4Code/discussion/327905

## Dealing with multi languages in notebooks

* Markdownには様々な言語が含まれている
* 75%は英語
* それ以外は中国語、ヒンディー語、日本語等

https://www.kaggle.com/competitions/AI4Code/discussion/327626