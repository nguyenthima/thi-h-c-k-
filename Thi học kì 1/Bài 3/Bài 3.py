ten = input(" Nhập tên đầy đủ:  ")
print(ten)
n = len(ten)
def isThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input("NGUYEN THI MAI thi n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
m = int(input("NGUYEN THI MAI thi m = "));
print("Tổng các chữ số của", m , "là", isThuanNghich(m));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));