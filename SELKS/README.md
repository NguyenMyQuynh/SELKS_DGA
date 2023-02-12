# Quy trình xây dựng hệ thống SELKS_DGA
## Mô tả
Phần này bao gồm các cài đặt và triển khai tự động mô hình SELKS_DGA 

## Yêu cầu tối thiểu
- 2 cores
- 9 GB RAM trống
- Dung lượng ổ đĩa trống tối thiểu 10 GB (dung lượng ổ đĩa thực tế sẽ chủ yếu phụ thuộc vào số lượng quy tắc và lưu lượng truy cập trên mạng). Nên dùng loại 200GB + SSD.
- git,curl
- docker > 17.06.0 (sẽ được cài đặt trong quá trình thiết lập ban đầu SELKS)
- docker-compose > 1.27.0 (sẽ được cài đặt trong quá trình thiết lập ban đầu SELKS)

## Cách sử dụng
```
git clone https://github.com/Tuan164/SELKS_DGA.git
cd SELKS_DGA
pip install -r requirements.txt
cd SELKS/docker/containers-data
mkdir thehive
chmod 777 thehive
cd DGA
sed -ie 's/172.16.60.10/<Your_machine's_IP>/g' config.py # (change SELKS_IP to your machine's IP)
chmod +x *
cd ../../
./easy-setup.sh
docker-compose up -d 
```

## Kiểm tra kết quả
- SELKS
    - Url: https://<Your_machine's_IP>
    - Username: selks-user
    - Password: selks-user
- Portainer
    - Url: https://<Your_machine's_IP>:9443
    - Username: admin
    - Password: quynhquynh0405        
- TheHive
    - Url: http://<Your_machine's_IP>:9000
    - Admin:
        - Username: admin@thehive.local
        - Password: secret
    - User:  
        - Username: hpt@gmail.com   
        - Password: hpt
