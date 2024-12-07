# output_jsonl_comparer
ファインチューン結果の比較ツール

## 概要

- 2つのファインチューン結果の出力を簡単に比較できるツールです
- 比較できる出力の形式は`{"task_id": (id), "input": "(入力)", "output": "(出力)"}`のjsonl形式となります

## ライセンス

- MIT License

## 動作環境

- WSL, Linux, Windows, Macなど （CPU環境でも動作します）
- Google Colab → [Google Colabで動かすには](#googles-colabで動かすには)

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


## Googles Colabで動かすには

GPUは不要ですので、ランタイムメニューのランタイムのタイプを変更から、CPUを選択して、で動かしましょう。長く使えるようになります

1. `main.py`のコードを丸ごと１つのセルにコピペしたあと、以下の変更をします

    最初に gradioをインストール
    ```py
    %pip install gradio
    ```

    最後のmain()呼び出し部分はコメントアウトして、直接main()を呼び出す
    ```py
    # if __name__ == "__main__":
    #    main()
    main()
    ```

1. 比較したいJSONLファイルを２つアップロードし、ファイル名を正しく設定します。

1. Gradioの画面が表示されますが、狭いので、以下のように表示されているリンクを開くと大きな画面で開くことができます。

    ```sh
    Colab notebook detected. To show errors in colab notebook, set debug=True in launch()
    * Running on public URL: https://xxxxxxxxxxxxxxxxx.gradio.live

    This share link expires in 72 hours.  For free permanent hosting and GPU upgrades, …
    ```

## 変更履歴

- 2024/12/07 その他の小さな不具合修正および改良
- 2024/12/07 キーボードでタスク移動ができるようにした
- 2024/12/07 タスクID入力後の移動ができない不具合を修正
- 2024/11/30 初版リリース

以上