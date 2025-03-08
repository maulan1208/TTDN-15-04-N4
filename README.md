---
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)


# 1. ĐỀ TÀI: QUẢN LÝ CHẤM CÔNG
Hệ thống quản lý chấm công giúp doanh nghiệp theo dõi và quản lý thời gian làm việc của nhân viên một cách chính xác và hiệu quả. Hệ thống này hỗ trợ ghi nhận giờ vào – giờ ra, kiểm soát đi trễ, quản lý lịch làm việc và xử lý đơn xin nghỉ của nhân viên.

Các chức năng trong Quản lý chấm công: Chấm công, Lịch làm việc nhân viên, Đơn xin nghỉ/muộn, Thống kê

1.1. Chấm công
![image](https://github.com/user-attachments/assets/856b245b-6946-46e3-a710-f7a20f7da9fc)
![image](https://github.com/user-attachments/assets/4bf49e18-a6d6-4e57-9b5e-c860775314ef)

2.1. Lịch làm nhân viên
![image](https://github.com/user-attachments/assets/5403b481-f7a2-47aa-8683-1d547f19f298)
![image](https://github.com/user-attachments/assets/300f138e-4fe1-4627-a0e5-daa8bbe0e4e1)

3.1. Đơn xin phép
![image](https://github.com/user-attachments/assets/780fcba2-0005-498c-84d2-8473521e4ec7)
![image](https://github.com/user-attachments/assets/d4a6c2eb-0e8f-4de7-abae-6745af1a9217)

4.1. Thống kê
(Bảng thống kê sẽ tự động cập nhật khi có thông tin mới) 
![image](https://github.com/user-attachments/assets/9c82bb88-ba6f-485f-a51e-833460165eae)

# 2. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 2.1. Clone project.
```
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
```
```
cd odoo-fitdnu
```

```
git checkout cntt15_04
```


## 2.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 2.3. khởi tạo môi trường ảo.

Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
python3.10 -m venv ./venv
```
```
source venv/bin/activate
```
```
pip3 install -r requirements.txt
```

# 3. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo apt install docker-compose
```
```
sudo docker-compose up -d
```

# 4. Setup tham số chạy cho hệ thống

## 4.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

# 5. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```


Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

Hoàn tất


