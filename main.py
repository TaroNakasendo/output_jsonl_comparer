import gradio as gr
import json
title = "ファインチューン結果の比較ツール"


# 比較したい2つの結果ファイルへのパスを指定してください
output_files = {
    "old": "20241129000000.jsonl",
    "now": "20241130140000.jsonl"
}


def main():

    # JSONL読込
    def load_jsonl(key):
        with open(output_files[key], "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f]

    # データ展開
    data = [(o["task_id"], o["input"], o["output"], n["output"])
            for o, n in zip(load_jsonl("old"), load_jsonl("now"))]

    with gr.Blocks(title=title) as demo:

        # 画面の配置
        gr.Markdown(f"# {title}")
        with gr.Row():
            task_id = gr.Textbox(label="タスクID")
            prev_button = gr.Button("前のタスク")
            next_button = gr.Button("次のタスク")
        input_text = gr.Textbox(label="入力", interactive=False)
        with gr.Row():
            output_old = gr.Textbox(label="昔の出力", interactive=False)
            output_now = gr.Textbox(label="今の出力", interactive=False)

        # データ取得
        idx = gr.State(0)

        def get_data(i):
            return data[i]

        def get_data_by_task_id(task_id):
            i = int(task_id) if task_id.isdigit(
            ) and 0 <= int(task_id) <= 100 else 0
            return data[i]

        # 動作の設定
        task_id.submit(get_data_by_task_id, task_id, [
                       task_id, input_text, output_old, output_now])

        prev_button.click(lambda x: max(0, x - 1), idx, idx).then(
            get_data, idx, [task_id, input_text, output_old, output_now])

        next_button.click(lambda x: min(len(data) - 1, x + 1), idx, idx).then(
            get_data, idx, [task_id, input_text, output_old, output_now])

        demo.load(get_data, idx, [task_id, input_text, output_old, output_now])

    demo.launch()


if __name__ == "__main__":
    main()
