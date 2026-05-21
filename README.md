```markdown
# AIO AIConquer: Churn Prediction 

Dự án Machine Learning dự đoán khả năng rời bỏ của khách hàng (Customer Churn Prediction), được phát triển bởi các thành viên trong đội ngũ team Newbie.

Mục tiêu của dự án là xây dựng một mô hình dự đoán chính xác tệp khách hàng có nguy cơ ngừng sử dụng dịch vụ, từ đó giúp doanh nghiệp đưa ra các chiến lược giữ chân khách hàng (retention strategies) kịp thời và hiệu quả.

## Cấu trúc dự án

Dự án được tổ chức theo cấu trúc chuẩn, giúp dễ dàng quản lý code và dữ liệu:


aio-aiconquer-churn-prediction/
├── data/                   # Chứa dữ liệu đầu vào và kết quả phân tích
│   ├── raw/                # Dữ liệu gốc chưa qua xử lý
│   ├── processed/          # Dữ liệu đã được làm sạch và chuẩn hóa
├── src/                    # Source code chính của dự án
│   ├── data-analysis       # Thư mục chứa code tiền xử lý và EDA
│   └── modeling/           # Thư mục chứa các mô hình học máy (XGBoost,...)
├── pyproject.toml          # File cấu hình dự án và danh sách thư viện (Dependencies)
├── uv.lock                 # File lock version thư viện (sử dụng uv)
├── .gitignore              # Các file/thư mục không đẩy lên Git
└── README.md               # Tài liệu hướng dẫn dự án

```

## Công nghệ & Mô hình sử dụng

* **Ngôn ngữ:** Python
* **Quản lý gói (Package Manager):** [uv](https://github.com/astral-sh/uv) 
* **Mô hình học máy:** * XGBoost, Random Forest, Decision Tree, Logistic Regression, Naive Bayes
* (Các mô hình khác sẽ được cập nhật trong tương lai)



