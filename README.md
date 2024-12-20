# output_jsonl_comparer
ファインチューン結果の比較ツール

## 概要

- 2つのファインチューン結果の出力を簡単に比較できるツールです
- 比較できる出力の形式は`{"task_id": (id), "input": "(入力)", "output": "(出力)"}`のjsonl形式となります

## ライセンス

- MIT License

## 動作環境

- WSL, Linux, Windows, Macなど （GPU不要です）
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/TaroNakasendo/output_jsonl_comparer/blob/main/google_colab.ipynb)　← クリックするとGoogle Colabでノートブックが開きます

## インストール

```sh
# git clone
git clone https://github.com/TaroNakasendo/output_jsonl_comparer.git
cd output_jsonl_comparer

# 仮想環境作成 (WSL, Linuxの場合)
python3 -m venv .venv --upgrade-deps
. .venv/bin/activate
pip install -r requirements.txt
```

## 実行

### 比較するファイルの設定

- `main.py`のソースコード内で入力ファイルを2つ指定します

```py
# 比較したい2つの結果ファイルへのパスを指定してください
output_files = {
    "old": "20241129000000.jsonl",
    "now": "20241130140000.jsonl"
}
```

### 起動方法

```sh
python main.py
```

- 実行後、ブラウザで<http://localhost:7860>を開くと下記のような画面が開きます
- `前のタスク`および`次のタスク`ボタンをクリックして前、次のタスクに移動できます
- キーボードの`左矢印キー`および`右矢印キー`を押下しても前、次のタスクに移動できます
- `タスクID`を指定することで、そのタスクIDのタスクを表示できます
- 終了するには`Ctrl + C`キーを押下してください

### 実行例

![ファインチューン結果の比較ツール](image.png)


## 変更履歴

- 2024/12/07 Google Colab向けのノートブックを追加
- 2024/12/07 その他の小さな不具合修正および改良
- 2024/12/07 キーボードでタスク移動ができるようにした
- 2024/12/07 タスクID入力後の移動ができない不具合を修正
- 2024/11/30 初版リリース

以上