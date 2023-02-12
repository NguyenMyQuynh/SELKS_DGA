-  Sửa đổi compose name thành HCRiffinwDGA
  <br>`sed -i “s|container_name: SELKS_DGA|container_name: HCRiffinwDGA|g” docker-compose.yml`
-  Build lại các image docker lên docker hub 
<br>`docker build -t HCRiffinwDGA . `
<br>`docker login`
<br>`docker push 1642001/ hcriffinwdga`
- Sửa lại tên và logo Stamus + Scirius, panel giới thiệu Stamus SELKS
<br>`containers-data/html/:/opt/scirius/rules/ `

-  Cấu hình tự động retention log ( khi disk đầy phải tự xoá log cũ)
  <br> **Tắt lưu file pcap**
<br> `Sửa pcap-log enable thành no trong file ./containers-data/suricata/etc/selks6-addin.yaml`

-  Log-retention:

```PUT _ilm/policy/log-retention
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_age": "7d"
          }
        }
      },
      "delete": {
        "min_age": "30d",
        "actions": {
          "delete": {} 
        }
      }
    }
  }
}

curl -X PUT "localhost:9200/_ilm/policy/log-retention" -H 'Content-Type: application/json' -d' { "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_age": "15m"
          }
        }
      },
      "delete": {
        "min_age": "30m",
        "actions": {
          "delete": {} 
        }
      }
    }
  } } '

curl -X PUT "localhost:9200/classify_domains/_settings" -H 'Content-Type: application/json' -d' 
{
  "index": {
    "lifecycle": {
      "name": "log-retention"
    }
  }
} '

```
