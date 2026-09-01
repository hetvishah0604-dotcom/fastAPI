from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: str


products = []
id = 0


@app.get("/products")
def get_products(response: Response):
    response.status_code = 200
    return products


@app.post("/products")
def create_product(product: Product, response: Response):
    global id

    try:
        id += 1
        product.id = id
        products.append(product)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Product created successfully",
            "product": product
        }

    except Exception as e:
        print(f"Error creating product: {e}")
        response.status_code = 500

        return {
            "message": "Error creating product",
            "isSuccess": False
        }


@app.put("/products/{productid}")
def update_product(productid: int, product: Product, response: Response):
    try:
        for index in range(len(products)):

            if products[index].id == productid:
                product.id = productid
                products[index] = product

                response.status_code = 200

                return {
                    "isSuccess": True,
                    "message": "Product updated successfully",
                    "product": product
                }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Product not found"
        }

    except Exception as e:
        print(f"Error updating product: {e}")

        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "Error updating product"
        }