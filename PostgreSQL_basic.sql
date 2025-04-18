-- Tạo bảng
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Thêm dữ liệu
INSERT INTO users (username, email, age)
VALUES ('anhtuan', 'anhtuan@example.com', 22);

-- Truy vấn dữ liệu
SELECT * FROM users;

-- Cập nhật
UPDATE users SET age = 23 WHERE username = 'anhtuan';
