STV=800_000_000
THV=5
LS=0.12
TN=45_000_000
NC=10_000_000
CPSH=4_000_000
SN=3
DTI= ((STV/(THV*12)+STV*(LS/12))+NC)/ (TN-CPSH*SN)
print(DTI)
if DTI < 0.7:
  print("ĐƯỢC VAY")
else:
  print("KHÔNG ĐƯỢC VAY") Dựa vào code này, viết lại code chạy trên streamlit tính chỉ số DTI, người dùng sẽ nhập: số tiền vay, thời hạn vay (theo năm), lãi suất vay, thu nhập, nợ cũ, chi phí sinh hoạt, số người trong gia đình. Kết quả hiển thị chỉ số DTI và kết luận được vay hay không, nếu DTI < 70% là không được vay và ngược lại. Viết code hoàn chỉnh để copy vào file app.py
