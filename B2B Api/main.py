from flask import Flask, jsonify, request
from createTableOperation import createTables
from addOperation import create_User, create_Product, create_order_details, SalesHistory, User_Stock
from readOperation import authenticate_user, get_All_Users, get_specific_user, get_all_products, get_specific_product, get_all_order_details, get_specific_order, find_user_by_email
from updateOperation import update_User, update_Order, updateProductQuantity
from deleteOperation import delete_User

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Medical Shop"


@app.route('/createUser', methods = ['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        pincode = request.form['pincode']
        phone_number = request.form['phone_number']

        user = find_user_by_email(email=email)

        if user is not None:
            return jsonify({"message": "Email already in use", "status": 400})
        else:
            userid = create_User(name=name, email=email, password=password, address=address, pincode=pincode, phone_number=phone_number)
            return jsonify({"message": str(userid), "status": str(200)})

    except Exception as error:
        return jsonify({"message": str(error), "status": str(400)})


@app.route('/createProduct', methods = ['POST'])
def create_product():
    try:
        product_name = request.form['product_name']
        price = request.form['price']
        stock = request.form['stock']
        category = request.form['category']

        product = create_Product(product_name=product_name, price=price, stock=stock, category=category)

        return jsonify({"user_id": str(product), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error) })



@app.route('/createOrderDetails', methods = ['POST'])
def createorder_details():
    try:

        user_name = request.form['user_name']
        quantity = request.form['quantity']
        product_price = request.form['product_price']
        total_price = request.form['total_price']
        product_name = request.form['product_name']
        message = request.form['message']
        category = request.form['category']
        user_id = request.form['user_id']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone_number']
        product_id = request.form['product_id']

        orderdetails = create_order_details( user_name=user_name, quantity=quantity, product_price=product_price, total_price=total_price, product_name=product_name, message=message, category=category, user_id=user_id, email=email, address=address, phone_number=phone_number, product_id=product_id)
        return jsonify({"message": str(orderdetails), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error) })



@app.route('/logIn', methods = ['POST'])
def logIn():
    try:
        email = request.form['email']
        password = request.form['password']

        user = authenticate_user(email = email, password = password)

        if user is None:
            return jsonify({"message": "Invalid Credentials", "status": 400})
        (
            id,
            user_id,
            password,
            date_of_account_creation,
            block,
            is_approved,
            name,
            address,
            email,
            phone_number,
            pincode
        ) = user

        user_response = {
            "id": id,
            "user_id": user_id,
            "password": password,
            "date_of_acount_creation": date_of_account_creation,
            "block": block,
            "isApproved": is_approved,
            "name": name,
            "address": address,
            "email": email,
            "phone_number": phone_number,
            "pincode": pincode,
        }

        return jsonify(user_response)

    except Exception as error:
        return jsonify({"message": str(error) , "status": 400})




@app.route('/getAllUsers', methods=['GET'])
def get_all_users():
    try:
        users = get_All_Users()
        return jsonify(users)

    except Exception as error:
        return jsonify({"error": str(error), "message":str(400)})


@app.route('/getAllProducts', methods=['GET'])
def get_all_Products():
    try:
        allproducts = get_all_products()
        return jsonify(allproducts)

    except Exception as error:
        return jsonify({"error": str(error), "message":400})


@app.route('/getAllOrderDetails', methods=['GET'])
def get_all_Order_Details():
    try:
        allorders = get_all_order_details()
        return jsonify(allorders)

    except Exception as error:
        return jsonify({"error": str(error), "message":400})


@app.route('/getSpecificUser', methods=['POST'])
def getSpecificUser():
    try:
        userId = request.form['user_id']
        user = get_specific_user(userId = userId)

        return jsonify(user)

    except Exception as error:
        return jsonify({"message": str(error), "status": str(400)})



@app.route('/getSpecificProduct', methods=['POST'])
def getSpecificProduct():
    try:
        product_id = request.form['product_id']
        product = get_specific_product(product_id = product_id)
        return jsonify(product)

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})


@app.route('/getSpecificOrder', methods=['POST'])
def getSpecific_Order():
    try:
        order_id = request.form['order_id']
        order = get_specific_order(order_id = order_id)
        
        return jsonify(order)

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})


@app.route('/updateOrder', methods=['PATCH'])
def updateOrder():
    try:
        order_id = request.form['order_id']
        update_list = {}

        for key, value in request.form.items():
            if key != "order_id":
                update_list[key] = value

        update_Order(order_id=order_id, update_list=update_list)

        return jsonify({"order_id": str(order_id), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})



@app.route('/updateUser', methods=['PATCH'])
def updateUser():
    try:
        userid = request.form['user_id']
        update_list = {}

        for key, value in request.form.items():
            if key != "user_id":
                update_list[key] = value

        update_User(user_id=userid, update_list=update_list)

        return jsonify({"user_id": str(userid), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})
    


@app.route('/updateStock', methods=['PATCH'])
def updateStock():
    try:
        product_id = request.form['product_id']
        update_list = {}

        for key, value in request.form.items():
            if key != "user_id":
                update_list[key] = value

        updateProductQuantity(product_id=product_id, update_list=update_list)

        return jsonify({"product_id": str(product_id), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})



@app.route('/deleteUser', methods=['DELETE'])
def deleteUser():
    try:
        user_id = request.form['user_id']
        delete_User(user_id = user_id)
        return jsonify({"user_id": str(user_id), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})

@app.route('/SaleHistory', methods=['POST'])
def SaleHistory():
    try:
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        remaining_stock = request.form['remaining_stock']
        product_price = request.form['product_price']
        product_name = request.form['product_name']
        user_name = request.form['user_name']

        salehistory = SalesHistory(user_id=user_id, product_id=product_id, quantity=quantity, remaining_stock=remaining_stock, product_price=product_price, product_name=product_name, user_name=user_name)
        return jsonify({"user_id": str(salehistory), "message": 200})

    except Exception as error:
        return jsonify({"error": str(error), "message": 400})


@app.route('/UserStock', methods=['POST'])
def UserStock():
    try:
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        stock = request.form['stock']
        category = request.form['category']
        product_price = request.form['product_price']
        product_name = request.form['product_name']
        user_name = request.form['user_name']

        User_Stock(user_id=user_id, product_id=product_id, stock=stock, category=category, product_price=product_price, product_name=product_name, user_name=user_name)
        return jsonify({"user_id": str(product_id), "message": 200})


    except Exception as error:
        return jsonify({"error": str(error), "message": 400})



if __name__ == '__main__':
    createTables()
    app.run(debug=True)