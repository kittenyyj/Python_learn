s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3={1,2}
s4={1,2,3,4,5,6}
s_1=s1.intersection(s2)
print(s_1)
s_2=s1.difference(s2)
print(s_2)
s_3=s1.union(s2)
print(s_3)
s_4=s1.issubset(s3)
s_5=s3.issubset(s1)
print(s_4)
print(s_5)
s_6=s1.issuperset(s3)
s_7=s3.issuperset(s1)
print(s_6)
print(s_7)
