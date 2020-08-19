scores=[]
name=[]
maxscores=0
minscores=100
total=0
for i in range(5):
    n=int(input('成績:'))
    na=str(input('name:'))
    scores.append(n)

    if n> maxscores:
        maxscores=n
        k=na
    if n< minscores:
        minscores=n
        j=na
        
    total=total+n

s=total/len(scores)
print('總分',total)
print('平均',s)
print('最高分',maxscores,k)
print('最低分',minscores,j)





  