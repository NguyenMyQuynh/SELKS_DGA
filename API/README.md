# Dự đoán DGA thông qua API
## Mô tả
Khi chạy file `API.py`, nó sẽ lắng nghe kết nối ở port 5000 và dự đoán xem domain từ người dùng gửi lên có phải là DGA hay không
thông qua mô hình được train từ https://github.com/Tuan164/DGA.</br>
Kết quả được trả về dưới dạng json với format:</br>
Domain (Input) -> IsDGA (Dự đoán có phải là DGA hay không) -> Probability (Xác suất domain đó là DGA)

## Cách dùng
### *Server*
- Cách 1: Clone from github
```
git clone https://github.com/Tuan164/SELKS_DGA.git
cd SELKS_DGA/API
python3 API.py
```
    
![image](https://user-images.githubusercontent.com/54493212/187583697-463c8a67-557e-4451-a9c9-728b6cdef077.png)

- Cách 2: Pull from dockerhub
```
docker pull 1642001/dga_detect
docker run -d -p 0.0.0.0:5000:5000 1642001/dga_detect
```

![image](https://user-images.githubusercontent.com/54493212/186911262-a8966e19-cd5b-4d70-a0ba-46ae644557fe.png)

### *Client*
    curl http://<Server_IP>:5000?domain=<Domain_name>
  
Kết quả khi truy cập với domain hợp lệ</br>
![image](https://user-images.githubusercontent.com/54493212/187583905-89bc0d1d-6502-4817-a76c-aa1544d97180.png)


Kết quả khi truy cập với DGA domain</br>
![image](https://user-images.githubusercontent.com/54493212/187583867-2a480b22-ebb6-4b56-addd-163d57c1f643.png)

