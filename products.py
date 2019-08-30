# 检查档案在不在
import os # orerating system

def read_file(filename):
	products = []
	# 读取档案
	with open (filename, 'r' ,encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue # 继续，跳到下一回，下面的不执行
			name,price = line.strip().split(',')
			products.append([name,price])
	return products

# 让使用者输入
def user_input(products):
	while True:
		name = input('请输入商品名称： ')	
		if name == 'q':
			break
		price = input('请输入商品价格：')
		price = int(price)
		# product = []
		# product.append(name)
		# product.append(price)
		# product = [name, price]
		products.append([name, price])
	print(products)
	return products

# 印出所有购买记录
def print_products(products):

	for p in products:
		print(p[0], '的价格是', p[1])

# 写入档案
def write_file(filename, products):

	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品' + ',' + '价格' + '\n')
		for p in products:	
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
			print('nice,找到档案了')
			products = read_file(filename)
	else:
			print('找不到档案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()