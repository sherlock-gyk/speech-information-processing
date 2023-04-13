from dtw import *

path1="./yes1.wav"
path2="./no2.wav"
path3="./yes3.wav"

s1=mfcc(path1)
s2=mfcc(path2)
s3=mfcc(path3)
d12=DTWDistance(s1,s2)
d13=DTWDistance(s1,s3)
print("d12: %f,d13: %f",d12,d13)