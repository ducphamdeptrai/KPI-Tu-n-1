import openai

# Đặt API Key của bạn
openai.api_key = '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'

def get_openai_response(prompt):
    # Gửi yêu cầu đến OpenAI API với cách gọi đúng
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Hoặc "gpt-4" tùy thuộc vào mô hình bạn muốn sử dụng
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Trả về kết quả text từ API
    return response['choices'][0]['message']['content']

# Nhập prompt từ người dùng
prompt = input("Nhập prompt của bạn: ")

# Gọi hàm với prompt người dùng nhập
response_text = get_openai_response(prompt)
print("Kết quả từ AI:", response_text)
