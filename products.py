products = []
while True:
	name = input('请输入商品名称： ')	
	if name == 'q':
		break
	price = input('请输入商品价格：')
	product = []
	product.append(name)
	product.append(price)
	products.append(product)
print(products)
print(products[0][0])