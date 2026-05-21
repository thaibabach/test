#de bai: nhập tên và điểm của học sinh của một lớp học, khi kết thúc nhập tên học sinh = 'stop',
#kết quả in ra là tên và số điểm của thủ khoa của lớp
#input: các dòng nhập tên học sinh và điểm của học sinh đó
hoc_sinh = {}
def nhap():
    while True:
        name = str(input("nhap ten hoc sinh: "))
        if (name.lower() == "stop"): break
        diem = float(input("nhap diem: "))
        hoc_sinh[name] = diem
nhap()
max = 0;
ten = "";
for name in hoc_sinh:
    if (hoc_sinh[name] > max):
        max = hoc_sinh[name]
        ten = name
print (ten, " ", max)