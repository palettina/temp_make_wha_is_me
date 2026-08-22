import time

def main():
    timestamp = int(time.time() * 1000)
    filename = f"{timestamp}.md"
    message = "まっさらなキャンバスに鮮やかな絵具を乗せて、夕暮れの黄金色の光の中で新しい色が生み出される瞬間がたまらなく大好きなの！どんな失敗も重ねれば深みになるわ、世界中を私の大好きな色彩で満たし続けましょう！\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(message)

    print(f"Created file: {filename}")
    print(f"Message length (without newline): {len(message) - 1}")

if __name__ == "__main__":
    main()
