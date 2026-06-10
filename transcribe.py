import whisper
print("Đang tải mô hình Whisper...")
model = whisper.load_model("large")

# 2. Đưa file âm thanh vào và bắt AI "nghe" rồi dịch thành chữ
print("AI đang lắng nghe và dịch âm thanh...")
result = model.transcribe("audio.wav", language = "vi")

# 3. In kết quả văn bản thu được ra màn hình Terminal
print("\n--- KẾT QUẢ ---")
print(result["text"])