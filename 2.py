def rever_sentence(sentence):
	words = sentence.split()
	words.reverse()
	new_str = " ".join(words)
	return new_str
 
if __name__ == '__main__':
	f=open('1.txt')
	f.read()
	# print ('你输入的英文句子：{}'.format(sentence))
	# out_str = rever_sentence(sentence)
	# print ('倒序结果输出：{}'.format(out_str))
	# print ('倒序后全部大写输出：%s' % out_str.upper())
	# print ('倒序后首字母大小输出：%s' % out_str.capitalize())
