products = []
while True:
	name = input('请输入商品名称： ')	
	if name == 'q':
		break
	price = input('请输入商品价格：')
	# product = []
	# product.append(name)
	# product.append(price)

	# product = [name, price]
	products.append([name, price])
print(products)

