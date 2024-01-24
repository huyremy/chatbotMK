import markovify

# Đường dẫn đến file .txt chứa dữ liệu huấn luyện
file_path = "demofile2.txt"

# Đọc nội dung từ file .txt
with open(file_path, "r", encoding="utf-8") as file:
    text_data = file.read()

# Tạo mô hình Markov từ dữ liệu huấn luyện
text_model = markovify.Text(text_data)

# Hàm phản hồi của chatbot
def get_response(input_text):
    response = text_model.make_sentence()
    return response

# Giao tiếp với chatbot
print("Chatbot: Xin chào! Bạn cần giúp gì?")
while True:
    user_input = input("Bạn: ")
    if user_input.lower() == "kết thúc":
        print("Chatbot: Chào tạm biệt!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
