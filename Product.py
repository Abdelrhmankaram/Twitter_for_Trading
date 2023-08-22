class Product():
    product_id : int

    def __init__(self, user_id, product_name, category, picture, description, price, status) -> None:
        self.product_name = product_name
        self.status = status
        self.category = category
        self.picture = picture
        self.description = description
        self.price = price
        self.user_id = user_id

    @staticmethod
    def create_object(res: tuple) -> None:
        product = Product(user_id=res[1], product_name=res[2], category=res[3], status=res[4], picture=res[5], description=res[6], price=res[7])
        product.product_id = res[0]
        return product
    
    def __str__(self):
        return f"Product ID: {self.product_id}\nProduct Name: {self.product_name}\nCategory: {self.category}\nPrice: {self.price}\nStatus: {self.status}\nDescription: {self.description}\nPicture: {self.picture}\nUser ID: {self.user_id}"