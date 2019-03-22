class product(object):
    def __init__(self, price, id, quantity):
        self._price = price
        self._id = id
        self._quantity = quantity
    def getprice(self):
        return self._price
    def getid(self):
        return self._id
    def getqua(self):
        return self._quantity
    def addqua(self, quantity):
        print("You had {} before".format(self._quantity))
        self._quantity += quantity
        print("You have {} now".format(self._quantity))
    def __str__(self):
        return "id:{}\n".format(self._id) + "price:{}\n".format(self._price) + "quantity:{}\n".format(self._quantity)

class inventory(object):
    def __init__(self):
        self.productList = []

    @property
    def sumUp(self):
        sum = 0
        for product in self.productList:
            sum += product.getprice()

        return sum
    def addProduct(self, new):
        for product in self.productList:
            if product.getid() == new.getid():
                product.addqua(new.getqua())
                return "Successfully add quantity to a existing product"

        self.productList.append(new)

    def __str__(self):
        string = ''
        for product in self.productList:
            string +=str(product) + '\n'

        return string

if __name__ == '__main__':
    a = product(200,2,1)
    b = product(100,1,1)
    c = product(200,2,1)
    inven = inventory()
    inven.addProduct(a)
    inven.addProduct(b)
    inven.addProduct(c)
    print(inven)
    print(inven.sumUp)