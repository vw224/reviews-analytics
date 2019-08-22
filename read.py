#1. 每100000筆，印出狀態
#2. 印出 共有幾筆資料?
#3. 印出 留言平均長度?
#4. 印出 留言長度<100，共有幾筆?
#5. 印出 隨機一筆留言長度<100的留言

data =[]
count = 0
with open('reviews.txt', 'r') as f:
	for all_review in f:
		data.append(all_review)
		count += 1
		if count%100000 == 0:
			print(count)
print('共有', count,'筆資料')

sum_review = 0

for d in data:
	sum_review += len(d)
#print('留言長度共', sum_review)
print('留言平均長度為', sum_review/len(data))

under100 = []
for x in data:
	if len(x) < 100:
		under100.append(x)
print('留言長度小於100的，共有', len(under100), '筆')
print(under100[0])
print(under100[1])


"""
參考解答:
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
"""