import google.generativeai as genai

# Cấu hình API Key
genai.configure(api_key="AIzaSyDejTaqB5Xao9aTRxlf2O5l-Lahx2SqITM")

# Hàm để gửi yêu cầu và nhận phản hồi từ mô hình
def get_gemini_response(prompt):
    # Lấy mô hình Gemini 2.0 Flash 001
    model = genai.GenerativeModel('models/gemini-1.5-pro')  # Thêm mô hình mới vào đây
    
    # Gửi prompt và lấy phản hồi bằng phương thức 'generate_content'
    response = model.generate_content(prompt)  # Sử dụng phương thức 'generate_content'
    
    # Trả về văn bản phản hồi
    return response.text

# Phần chính của chương trình
if __name__ == "__main__":
    prompt = input("Nhập prompt của bạn: ")  # Nhập prompt từ người dùng
    print("Đang gửi yêu cầu tới Gemini...\n")
    result = get_gemini_response(prompt)
    print("Kết quả từ Gemini:\n", result)
