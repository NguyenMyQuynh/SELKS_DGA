# Kết hợp SELKS, DGA và TheHive
***Lưu ý: để mô hình hoạt động bình thường, cần khởi động SELKS và TheHive lên trước, 
sau đó chỉnh sửa giá trị của "SELKS_IP" trong config.py thành IP tương ứng với máy đang chạy SELKS và TheHive***

## Mô tả
Hệ thống sẽ giám sát các DNS, phân tích việc truy cập Inernet của các người dùng trong mạng. Qua đó, trích xuất được các domain mà người dùng truy cập và phân loại domain đó. Kết quả phân loại sẽ được gửi trả lên lại cho SELKS và TheHive

## Cách thức hoạt động
Hệ thống sẽ truy xuất đến `http://<SELKS_IP>:9200/logstash-dns-<current_date>/_search` để trích xuất thông tin domain. 
Khi vừa khởi động (khởi chạy file `selks_dga.py`) thì nó sẽ trích xuất các domains trong vòng 15' gần đây.
Các domains trích xuất được sẽ được phân loại và gửi trả kết quả lên elasticsearch_index `classifyDomain`. 
Nếu Hệ thống phát hiện được DGA domain, nó cũng sẽ gửi thêm cảnh báo lên TheHive.

## Cách dùng:
- Trước hết cần chỉnh sửa giá trị của "SELKS_IP" trong config.py thành IP tương ứng với máy đang chạy SELKS và TheHive
- Nếu đây là lần đầu khởi động mô hình, cần phải thực thi file entrypoint.sh để thêm index "classifyDomain" vào kibana:</br>
```
./entrypoint
```
- Thực thi câu lệnh bên dưới để tự động thực thi chu trình trích xuất và phân loại sau mỗi 15'
``` 
python3 selks_dga.py
```
- Vào kibana->discover->index "classifyDomain" và kiểm tra kết quả.
- Tương tự, vào TheHive để kiểm tra các cảnh báo
