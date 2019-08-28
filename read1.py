data =[]
count = 0
with open('reviews.txt', 'r') as f:
	for all_review in f:
		data.append(all_review)
		count += 1
		if count%100000 == 0:
			print(count)
print('共有', count,'筆資料')
print(data[0])

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

listA = []
for d in data:
	if 'good' in d:
		listA.append(d)
print('一共有', len(listA), '筆留言提到good')
print(listA[0])


#文字計數
wc = {}   #word_count
for d in data:
	words = d.split()   #split預設是空字串
	for word in words:
		if word in wc:   #如果這個字有出現過
			wc[word] += 1
		else:
			wc[word] = 1   #新增新的key進wc字典

for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Vivi'])   #查找Vivi

while True:
	word = input('請輸入要查詢的字: ')
	if word == 'q':
		break
	if word in wc:
	    print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')


# 參考解答:
# data = []
# count = 0
# with open('reviews.txt', 'r') as f:
# 	for line in f:
# 		data.append(line)
# 		count += 1
# 		if count % 100000 == 0:
# 			print(len(data))

# print('檔案讀取完了，總共有', len(data), '筆資料')

# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('留言的平均為', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')