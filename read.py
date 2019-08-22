data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

length = 0
x = 0
for i in range(len(data)):
	length += len(data[i])
	if len(data[i]) < 100:
		x += 1

avg = length / count

print('檔案讀取完了，總共有', len(data), '筆資料')
print('留言平均長度為', avg)
print('留言長度小於100，共有', x, "筆")


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