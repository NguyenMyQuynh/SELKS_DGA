# SELKS, DGA on Docker
## Mô tả
Repository này bao gồm việc phân loại "Các thuật toán tạo tên miền" (Domain generation algorithm - DGA) và triển khai SELKS cũng như kết hợp SELKS_DGA.

## Cách sử dụng
Trước hết cần đảm bảo đủ công cụ và thư viện hỗ trợ
```
apt install curl
apt install git
apt install python3
apt install pip
```
Tùy từng thư mục, ta có các tính năng khác nhau
- API: Hỗ trợ triển khai hệ thống phân loại DGA domain thông qua API.
- SELKS_DGA: Trích xuất, phân loại DGA domain từ elasticsearch và gửi trả kết quả cho SELKS và TheHive sau mỗi 15'.
- SELKS: Cài đặt SELKS, TheHive và các tính năng của SELKS_DGA một cách tự động.

***Lưu ý: Đọc kĩ file README.md trong từng thư mục cụ thể để hiểu rõ hơn cách hoạt động cũng như triển khai hệ thống***

## Tài liệu tham khảo
1. https://github.com/sudo-rushil/dga-intel-web
2. https://github.com/sudo-rushil/dgaintel
3. https://www.kaggle.com/datasets/hydrobloquant/dgas-detection
4. https://github.com/StamusNetworks/SELKS/ 
5. https://docs.thehive-project.org/thehive/ 

