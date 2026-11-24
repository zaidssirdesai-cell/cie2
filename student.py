import sys


def calculate():
    total = n1+n2+n3
    avg = total/3
    per = (total/300)*100

if __name__=="__main__":
    n1=float(sys.argv[1])
    n2=float(sys.argv[2])
    n3=float(sys.argv[3])

total,avg,per=calculate(n1,n2,n3)
print("Total:")
print(total)
print("Avergae:")
print(avg)
print("Persentage:")
print(per)
