#flask boilerpalte
from flask import Flask, request, jsonify, render_template, url_for ,redirect, session, make_response, flash
#sql
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#migration
from flask_migrate import Migrate
import os
import jwt

from werkzeug.utils import secure_filename
import requests, json
import pyimgur
import jwt 

import uuid
from werkzeug.security import generate_password_hash, check_password_hash

import datetime

from functools import wraps

import time
import random

import xlrd


from flask_cors import CORS
app = Flask(__name__)
CORS(app,origins=['http://localhost:5173','https://kenzfood.onrender.com'])
# app.secret_key = 'asdasdasdasdasdasdasaasdasdasdasd12312312daveqvq34c'
app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasaasdasdasdasd12312312daveqvq34c'

UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




counter = 0

def generate_order_id():
    global counter
    counter += 1
    return str(int(time.time())) + str(counter).zfill(3)

CLIENT_ID = "2d3158d36137249"
im = pyimgur.Imgur(CLIENT_ID)


# ENV = 'prod'
ENV = 'dev'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'
    # PATH = "C:/Users/USER/Desktop/Hash IT/kenz-food-api/kenz-food-api/kenz-api/static/img/uploads/"

else:
    app.debug = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    
SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)



# class Users(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     ip_address = db.Column(db.String(100))
#     # last_login_ip = db.Column(db.String(100))
#     public_id = db.Column(db.String(100), unique=True)
#     user_type = db.Column(db.String(100), nullable=False)
#     username = db.Column(db.String(100), nullable=False)    
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     phone = db.Column(db.String(100), nullable=False, unique=True)
#     profile_url = db.Column(db.String(100), nullable=True)
#     verified_user = db.Column(db.Boolean, nullable=True , default=False)
#     active_user = db.Column(db.String(100), nullable=True)
#     created_at = db.Column(db.String(100), nullable=True)
#     last_login = db.Column(db.String(100), nullable=True)
#     fcm_id = db.Column(db.String(100), nullable=True)
#     latitude = db.Column(db.String(100), nullable=True)
#     longitude = db.Column(db.String(100), nullable=True)
#     # session_id = db.Column(db.String(100), nullable=True)

#     # prod_cat = db.relationship('ProductCategory', backref='prod_cat')
#     user_type_db = db.relationship('UserType', backref='user_type_db')
#     user_address = db.relationship('UserAddress', backref='user_address')
#     user_whishlist_br = db.relationship('UserWhishlist', backref='user_whishlist_br')
#     user_cart_br = db.relationship('CartItem', backref='user_cart_br')
#     order_br = db.relationship('Order', backref='order_br')
#     # order_details_br = db.relationship('OrderDetails', backref='order_details_br')
#     # payment_details_br = db.relationship('PaymentDetails', backref='payment_details_br')



# dev2
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100), nullable=True)
    # last_login_ip = db.Column(db.String(100))
    public_id = db.Column(db.String(100), unique=True)
    user_type = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), nullable=True)    
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    profile_url = db.Column(db.String(100), nullable=True)
    verified_user = db.Column(db.Boolean, nullable=True , default=False)
    active_user = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.String(100), nullable=True)
    last_login = db.Column(db.String(100), nullable=True)
    fcm_id = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.String(100), nullable=True)
    longitude = db.Column(db.String(100), nullable=True)
    # session_id = db.Column(db.String(100), nullable=True)
    is_wholesale = db.Column(db.Boolean, default=False)

    # prod_cat = db.relationship('ProductCategory', backref='prod_cat')
    user_type_db = db.relationship('UserType', backref='user_type_db')
    user_address = db.relationship('UserAddress', backref='user_address')
    user_whishlist_br = db.relationship('UserWhishlist', backref='user_whishlist_br')
    user_cart_br = db.relationship('CartItem', backref='user_cart_br')
    order_br = db.relationship('Order', backref='order_br')
    # order_details_br = db.relationship('OrderDetails', backref='order_details_br')
    # payment_details_br = db.relationship('PaymentDetails', backref='payment_details_br')



class Notifications(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    notification_image = db.Column(db.String(100), nullable=True)
    notification_url = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.String(100), nullable=True)
    # status = db.Column(db.Boolean, nullable=True, default=False)
    product = db.relationship('Products', backref='product_not')




class BannerSection(db.Model):
    __tablename__ = 'bannersection'
    id = db.Column(db.Integer, primary_key=True)
    banner_name_en = db.Column(db.String(100), nullable=False)
    banner_name_ar = db.Column(db.String(100), nullable=True)
    banner_order = db.Column(db.String(100), nullable=True)
    banner_image_url = db.Column(db.String(100), nullable=False)
    banner_desc_en = db.Column(db.String(5000), nullable=True)
    banner_desc_ar = db.Column(db.String(5000), nullable=True)
    status = db.Column(db.String(100), nullable=True)

class SecondaryBanner(db.Model):
    __tablename__ = 'secondarybanner'
    id = db.Column(db.Integer, primary_key=True)
    banner_name_en = db.Column(db.String(100), nullable=False)
    banner_name_ar = db.Column(db.String(100), nullable=True)
    banner_order = db.Column(db.String(100), nullable=True)
    banner_image_url = db.Column(db.String(100), nullable=False)
    banner_desc_en = db.Column(db.String(5000), nullable=True)
    banner_desc_ar = db.Column(db.String(5000), nullable=True)
    status = db.Column(db.String(100), nullable=True)



class ProductCategory(db.Model):
    __tablename__ = 'productcategory'
    id = db.Column(db.Integer, primary_key=True)
    category_name_en = db.Column(db.String(100), nullable=False)
    category_name_ar = db.Column(db.String(100), nullable=True)
    category_order = db.Column(db.String(100), nullable=True)
    category_image_url = db.Column(db.String(100), nullable=True)
    category_desc_en = db.Column(db.String(5000), nullable=True)
    category_desc_ar = db.Column(db.String(5000), nullable=True)
    active = db.Column(db.String(100), nullable=True)

    cat_product = db.relationship('Products', backref='product')

    sub_cat = db.relationship('ProductSubCategory', backref='sub_cat')
    # fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class ProductSubCategory(db.Model):
    __tablename__ = 'productsubcategory'
    id = db.Column(db.Integer, primary_key=True)
    subcategory_name_en = db.Column(db.String(100), nullable=False)
    subcategory_name_ar = db.Column(db.String(100), nullable=True)
    subcategory_order = db.Column(db.String(100), nullable=True)
    subcategory_image_url = db.Column(db.String(100), nullable=True)
    subcategory_desc_en = db.Column(db.String(5000), nullable=True)
    subcategory_desc_ar = db.Column(db.String(5000), nullable=True)
    active = db.Column(db.String(100), nullable=True)

    # fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sub_product = db.relationship('Products', backref='products')
    
    fk_prod_cat_id = db.Column(db.Integer, db.ForeignKey('productcategory.id'))


# class Products(db.Model):
#     __tablename__ = 'products'
#     id = db.Column(db.Integer, primary_key=True)
#     product_name_en = db.Column(db.String(100), nullable=False)
#     product_name_ar = db.Column(db.String(100), nullable=True)
#     product_desc_en = db.Column(db.String(5000), nullable=True)
#     product_desc_ar = db.Column(db.String(5000), nullable=True)
#     unit_id = db.Column(db.String(100), nullable=True)
#     unit_quantity = db.Column(db.String(100), nullable=True)
#     product_code = db.Column(db.String(100), nullable=True)
#     produc_barcode = db.Column(db.String(100), nullable=True)
#     other_title_en = db.Column(db.String(100), nullable=True)
#     other_title_ar = db.Column(db.String(100), nullable=True)
#     other_desc_en = db.Column(db.String(5000), nullable=True)
#     other_desc_ar = db.Column(db.String(5000), nullable=True)
#     status = db.Column(db.String(100), nullable=True)
#     fast_delivery = db.Column(db.String(100), nullable=True)
#     featured = db.Column(db.String(100), nullable=True)
#     fresh = db.Column(db.String(100), nullable=True)
#     offer = db.Column(db.String(100), nullable=True)

#     cat = db.Column(db.Integer,  db.ForeignKey('productcategory.id'),)
#     subcat = db.Column(db.Integer, db.ForeignKey('productsubcategory.id'))

#     user_whishlist = db.relationship('UserWhishlist', backref='user_whishlist')
#     cart_item = db.relationship('CartItem', backref='cart_item')
#     # order_item = db.relationship('OrderItem', backref='order_item')
#     order_details = db.relationship('OrderDetails', backref='order_details')
#     # payment_details = db.relationship('PaymentDetails', backref='payment_details')
    

#     product_image = db.relationship('ProductImages', backref='product_image')
#     product_stock = db.relationship('ProductStock', backref='product_stock')
    

# dev2
class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name_en = db.Column(db.String(100), nullable=False)
    product_name_ar = db.Column(db.String(100), nullable=True)
    product_desc_en = db.Column(db.String(5000), nullable=True)
    product_desc_ar = db.Column(db.String(5000), nullable=True)
    unit_id = db.Column(db.String(100), nullable=True)
    unit_quantity = db.Column(db.String(100), nullable=True)
    product_code = db.Column(db.String(100), nullable=True)
    produc_barcode = db.Column(db.String(100), nullable=True)
    other_title_en = db.Column(db.String(100), nullable=True)
    other_title_ar = db.Column(db.String(100), nullable=True)
    other_desc_en = db.Column(db.String(5000), nullable=True)
    other_desc_ar = db.Column(db.String(5000), nullable=True)
    status = db.Column(db.String(100), nullable=True)
    fast_delivery = db.Column(db.String(100), nullable=True)
    featured = db.Column(db.String(100), nullable=True)
    fresh = db.Column(db.String(100), nullable=True)
    offer = db.Column(db.String(100), nullable=True)

    # cat = db.Column(db.Integer,  db.ForeignKey('productcategory.id'))
    cat = db.Column(db.Integer, db.ForeignKey('productcategory.id'), nullable=True)
    subcat = db.Column(db.Integer, db.ForeignKey('productsubcategory.id'), nullable=True)

    user_whishlist = db.relationship('UserWhishlist', backref='user_whishlist')
    cart_item = db.relationship('CartItem', backref='cart_item')
    # order_item = db.relationship('OrderItem', backref='order_item')
    order_details = db.relationship('OrderDetails', backref='order_details')
    # payment_details = db.relationship('PaymentDetails', backref='payment_details')
    

    product_image = db.relationship('ProductImages', backref='product_image')
    product_stock = db.relationship('ProductStock', backref='product_stock')

class ProductImages(db.Model):
    __tablename__ = 'productimages'
    id = db.Column(db.Integer, primary_key=True)
    product_image_url = db.Column(db.String(100), nullable=True)
    product_image_desc_en = db.Column(db.String(5000), nullable=True)
    product_image_desc_ar = db.Column(db.String(5000), nullable=True)

    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class ProductStock(db.Model):
    __tablename__ = 'productstock'
    id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.String(100), nullable=True)
    product_offer_price = db.Column(db.String(100), nullable=True)
    product_purchase_price = db.Column(db.String(100), nullable=True)
    opening_stock = db.Column(db.String(100), nullable=True)
    min_stock = db.Column(db.String(100), nullable=True)
    max_stock = db.Column(db.String(100), nullable=True)
    main_rack_no = db.Column(db.String(100), nullable=True)
    sub_rack_no = db.Column(db.String(100), nullable=True)


    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class ProductUnit(db.Model):
    __tablename__ = 'productunit'
    id = db.Column(db.Integer, primary_key=True)
    unit_name_en = db.Column(db.String(100), nullable=False)
    unit_name_ar = db.Column(db.String(100), nullable=True)
    unit_desc_en = db.Column(db.String(100), nullable=True)
    unit_desc_ar = db.Column(db.String(100), nullable=True)
    unit_short_form_en = db.Column(db.String(100), nullable=True)
    unit_short_form_ar = db.Column(db.String(100), nullable=True)
    active = db.Column(db.String(100), nullable=True)


class UserType(db.Model):
    __tablename__ = 'usertype'
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(100))
    user_name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 


class UserAddress(db.Model):
    __tablename__ = 'useraddress'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(5000), nullable=True)
    address_line1 = db.Column(db.String(5000), nullable=True)
    address_line2 = db.Column(db.String(5000), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    telephone = db.Column(db.String(100), nullable=True)
    mobile = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.String(100), nullable=True)
    longitude = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    modified_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

class UserWhishlist(db.Model):
    __tablename__ = 'userwhishlist'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=True)
    modified_at = db.Column(db.DateTime, nullable=True)

    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

class CartItem(db.Model):
    __tablename__ = 'cartitem'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=True)
    # payment_method = db.Column(db.String(100), nullable=False)

    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))



class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_quantity = db.Column(db.String(100), nullable=False)
    total_price = db.Column(db.String(100), nullable=False)
    # payment_method = db.Column(db.String(100), nullable=False)
    address_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    modified_at = db.Column(db.DateTime, nullable=True)
    delivery_time=db.Column(db.DateTime, nullable=True)
    delivery_type=db.Column(db.String(100), nullable=True)
    
    ord = db.relationship('OrderDetails', backref='ord')
    pay_ord = db.relationship('PaymentDetails', backref='pay_ord')


class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    id = db.Column(db.Integer, primary_key=True)
    fk_order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    item_quantity = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, nullable=True)
    delivery_mode = db.Column(db.DateTime, nullable=True) 
    transaction_id = db.Column(db.String(100), nullable=True)
    fk_product_id = db.Column(db.Integer, db.ForeignKey('products.id'))



class PaymentDetails(db.Model):
    __tablename__ = 'paymentdetails'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100), nullable=True)
    payment_id = db.Column(db.String(100), nullable=True)
    payment_type = db.Column(db.String(100), nullable=True)
    payment_status = db.Column(db.String(100), nullable=True)
    payment_amount = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    modified_at = db.Column(db.DateTime, nullable=True)

    fk_order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

# dev2
class country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100), nullable=False)
    country_image_url = db.Column(db.String(100), nullable=False)
    country_code=db.Column(db.String(100), nullable=False)

# dev2

class delivery_charges(db.Model):
    __tablename__ = 'delivery_charges'
    charge_id = db.Column(db.Integer, primary_key=True)
    location_name=db.Column(db.String(50), nullable=False)
    location_zipcode=db.Column(db.Integer(), nullable=False)
    normal_charge=db.Column(db.Integer(), nullable=False)
    fast_charge=db.Column(db.Integer(), nullable=False)
    active_status=db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)


class Coupon(db.Model):
    __tablename__ = 'coupons'
    coupon_id = db.Column(db.Integer, primary_key=True)
    coupon_name = db.Column(db.String(50), nullable=False)
    coupon_code = db.Column(db.String(20), nullable=False, unique=True)
    reduction_amount = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    active_status = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    price_reduction = db.Column(db.Float, nullable=False)









def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            jwt_current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(jwt_current_user, *args, **kwargs)

    return decorated






login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')





@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    productCategory = ProductCategory.query.all()
    # render the index.html template
    return render_template('index.html', user=current_user, productCategory=productCategory)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)




## ------------------------------------------------------------------- APIs ------------------------------------------------------------------- ##

@app.route('/insert_users', methods=['POST'])
def insert_users():
    if request.method == 'POST':
        content = request.json
        print(content)
        try: 
            with app.app_context():
                user = Users(ip_address=request.remote_addr, 
                    user_type=content['user_type'],
                    public_id=str(uuid.uuid4()),
                    username=content['username'],
                    firstname=content['firstname'],
                    lastname=content['lastname'],
                    password=generate_password_hash(content['password'], method='sha256'),
                    email=content['email'],
                    phone=content['phone'],
                    created_at=datetime.datetime.now()
                )
                db.session.add(user)
                db.session.commit()
                current_user = Users.query.filter_by(email=content['email']).first()
            return jsonify({'return': 'user added successfully',
                            'user_id': current_user.id,
                            'user_type': current_user.user_type,
                            'public_id': current_user.public_id,
                            'username': current_user.username,
                            'firstname': current_user.firstname,
                            'lastname': current_user.lastname,
                            'email': current_user.email,
                            'phone': current_user.phone,
                            'created_at': current_user.created_at})
        except Exception as e:
            return jsonify({'return': 'error adding user'+str(e)})
    return jsonify({'return': 'no POST request'})

# dev2
# @app.route('/insert_users', methods=['POST'])
# def insert_users():
#     if request.method == 'POST':
#         content = request.json
#         print(content)
#         try: 
#             with app.app_context():
#                 user = Users(
#                     # ip_address=request.remote_addr, 
#                     # user_type=content['user_type'],
#                     # public_id=str(uuid.uuid4()),
#                     # username=content['username'],
#                     # firstname=content['firstname'],
#                     # lastname=content['lastname'],
#                     # password=generate_password_hash(content['password'], method='sha256'),
#                     # email=content['email'],
#                     phone=content['phone'],
#                     created_at=datetime.datetime.now()
#                 )
#                 db.session.add(user)
#                 db.session.commit()
#                 current_user = Users.query.filter_by(phone=content['phone']).first()
#             return jsonify({'return': 'user added successfully',
#                             'phone': current_user.phone,})
#         except Exception as e:
#             return jsonify({'return': 'error adding user'+str(e)})
#     return jsonify({'return': 'no POST request'})




@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    
    if request.method == 'POST':
        content = request.json
        if not content or not content['email'] or not content['password']:
            return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        user = Users.query.filter_by(email=content['email']).first()

        if not user:
            return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if check_password_hash(user.password, content['password']):
            token = jwt.encode({'public_id': user.public_id}, app.config['SECRET_KEY'])
            user.ip_address = request.remote_addr
            db.session.commit()

            return jsonify({'token' : token.decode('UTF-8'), 'user_id': user.id, 'phone' : user.phone, 'is_verified' : user.verified_user}) 
    
        return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    else:
        return jsonify({'return': 'no POST request'})




@app.route('/sign_out', methods=['GET'])
@token_required
def sign_out():
    logout_user()
    return jsonify({'return': 'success'})



@app.route('/update_password/<int:user_id>', methods=['PUT'])
def update_password(user_id):
    if request.method == 'PUT':
        content = request.json
        user = Users.query.filter_by(id=user_id).first()
        if user:
            user.password = generate_password_hash(content['new_password'], method='sha256')
            db.session.commit()
            return jsonify({'return': 'success',
                            'user_id': user.id,
                            'user_type': user.user_type,
                            'public_id': user.public_id,
                            'username': user.username,
                            'firstname': user.firstname,
                            'lastname': user.lastname,
                            'email': user.email,
                            'phone': user.phone,
                            'created_at': user.created_at})
        else:
            return jsonify({'return': 'user not found'})
    else:
        return jsonify({'return': 'no PUT request'})






@app.route('/verify/<int:user_id>', methods=['GET'])
def isVerified(user_id):
    user = Users.query.filter_by(id=user_id).first()
    if user:
        return jsonify({'return': 'success', 'user_verification_status': user.verified_user})
    else:
        return jsonify({'return': 'user not found'})

@app.route('/verify/<int:user_id>', methods=['PUT'])
def verify(user_id):
    if request.method == 'PUT':
        user = Users.query.filter_by(id=user_id).first()
        if user:
            user.verified_user = True
            db.session.commit()
            return jsonify({'return': 'success'})
        else:
            return jsonify({'return': 'user not found'})
    else:
        return jsonify({'return': 'no PUT request'})



@app.route('/update_user', methods=['PUT'])
@token_required
def update_user(current_user):
    if request.method == 'PUT':
        # content = request.json
        user = Users.query.filter_by(id=current_user.id).first()
        if user:
            user.firstname = request.form['firstname']
            user.lastname = request.form['lastname']
            user.email = request.form['email']
            user.phone = request.form['phone']
            user_image = request.files.get('user_image')
            if user_image:
                img_filename = secure_filename(user_image.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                user_image.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))   
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                user.profile_url = upload_image.link
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

            return jsonify({'return': 'success'})
        else:
            return jsonify({'return': 'user not found'})
    else:
        return jsonify({'return': 'no PUT request'})



@app.route('/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    if request.method == 'DELETE':
        user = Users.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'return': 'success'})
        else:
            return jsonify({'return': 'user not found'})
    else:
        return jsonify({'return': 'no DELETE request'})


@app.route('/user_deactivate', methods=['PUT'])
@token_required
def user_deactivate(current_user):
    if request.method == 'PUT':
        content = request.json
        user = Users.query.filter_by(id=current_user.id).first()
        #check password
        if user:
            if check_password_hash(user.password, content['password']):
                user.verified_user = False
                user.active_user = 'deactivated'
                user.username = user.username + '#000'
                user.email = user.email + '#000'
                user.phone = user.phone + '#000'
                db.session.commit()
                return jsonify({'return': 'success'})
            else:
                return jsonify({'return': 'incorrect password'})
        else:
            return jsonify({'return': 'user not found'})
    else:
        return jsonify({'return': 'no PUT request'})






@app.route('/get_users/<parm>', methods=['GET'])
def get_users(parm):

    # if not jwt_current_user:
    #     return jsonify({'return': 'user not logged in'})

    def get_USER_query(user):
        user_json = {
                    'return': 'success', 
                    'id': user.id,
                    'publci_id': user.public_id,
                    'user': user.username,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password,
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'user_type': user.user_type,
                    'ip_address': user.ip_address,
                    'profile_url': user.profile_url,
                    'verified_user': user.verified_user,
                    'active_user': user.active_user,
                    'created_at': user.created_at,
                    'last_login': user.last_login,
                    'fcm_id': user.fcm_id,
                    'latitude': user.latitude,
                    'longitude': user.longitude,
                    }
        return user_json

    #check user 


    if request.method == 'GET': 
        try:    
            if parm == 'email':
                email = request.args.get('email')
                try:
                    user = Users.query.filter_by(email=email).first()
                    return jsonify(get_USER_query(user))
                except Exception as e:
                    return jsonify({'return': 'no user found'})

            elif parm == 'username':
                username = request.args.get('username')
                try:
                    user = Users.query.filter_by(username=username).first()
                    return jsonify(get_USER_query(user))
                except Exception as e:
                    return jsonify({'return': 'no user found'})
            
            elif parm == 'phone':
                phone = request.args.get('phone')
                try:
                    user = Users.query.filter_by(phone=phone).first()
                    return jsonify(get_USER_query(user))
                except Exception as e:
                    return jsonify({'return': 'no user found'})
            else:
                return jsonify({'return': 'no such parameter'})
        except Exception as e:
            return jsonify({'return': 'error getting users : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_user/current', methods=['GET'])
@token_required
def get_user_current(jwt_current_user):
    if request.method == 'GET':
        try:
            user = Users.query.filter_by(id=jwt_current_user.id).first()
            user_json = {
                    'return': 'success', 
                    'id': user.id,
                    'publci_id': user.public_id,
                    'user': user.username,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password,
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'user_type': user.user_type,
                    'ip_address': user.ip_address,
                    'profile_url': user.profile_url,
                    'verified_user': user.verified_user,
                    'active_user': user.active_user,
                    'created_at': user.created_at,
                    'last_login': user.last_login,
                    'fcm_id': user.fcm_id,
                    'latitude': user.latitude,
                    'longitude': user.longitude,
                    }
            return jsonify(user_json)
        except Exception as e:
            return jsonify({'return': 'error getting users : '+ str(e)})
    return jsonify({'return': 'no GET request'})
    


@app.route('/user_addr', methods=['POST'])
@token_required
def user_addr(jwt_current_user):
    if request.method == 'POST':
        try:
            data = request.get_json()
            user_addr = UserAddress(
                name=data['name'],
                address_line1=data['address_line1'],
                address_line2=data['address_line2'],
                city=data['city'],
                postal_code=data['postal_code'],
                country=data['country'],
                telephone=data['telephone'],
                mobile=data['mobile'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                created_at=datetime.datetime.now(),
                modified_at=datetime.datetime.now(),
                user_id=jwt_current_user.id
            )
            db.session.add(user_addr)
            db.session.commit()
            return jsonify({'return': 'success', 'message': 'address added'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error adding address : '+ str(e)})
    return jsonify({'return': 'no POST request'})

@app.route('/user_addr', methods=['GET'])
@token_required
def get_user_addr(jwt_current_user):
    if request.method == 'GET':
        try:
            user_addr = UserAddress.query.filter_by(user_id=jwt_current_user.id).all()
            if user_addr:
                user_addr_list = []
                for item in user_addr:
                    user_addr_list.append({
                        'name':item.name,
                        'id': item.id,
                        'address_line1': item.address_line1,
                        'address_line2': item.address_line2,
                        'city': item.city,
                        'postal_code': item.postal_code,
                        'country': item.country,
                        'telephone': item.telephone,
                        'mobile': item.mobile,
                        'latitude': item.latitude,
                        'longitude': item.longitude,
                        'created_at': item.created_at,
                        'modified_at': item.modified_at,
                        'user_id': item.user_id
                    })
                return jsonify({'return': 'success', 'message': 'address fetched', 'data': user_addr_list})
            else:
                return jsonify({'return': 'error', 'message': 'address not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching address : '+ str(e)})
    return jsonify({'return': 'no GET request'})

@app.route('/user_addr/<id>', methods=['GET'])
@token_required
def get_user_addr_by_id(jwt_current_user, id):
    if request.method == 'GET':
        try:
            user_addr = UserAddress.query.filter_by(user_id=jwt_current_user.id,id=id).first()
            if user_addr:
                return jsonify({'return': 'success', 'message': 'address fetched', 'data': {
                    'id': user_addr.id,
                    'address_line1': user_addr.address_line1,
                    'address_line2': user_addr.address_line2,
                    'city': user_addr.city,
                    'postal_code': user_addr.postal_code,
                    'country': user_addr.country,
                    'telephone': user_addr.telephone,
                    'mobile': user_addr.mobile,
                    'latitude': user_addr.latitude,
                    'longitude': user_addr.longitude,
                    'created_at': user_addr.created_at,
                    'modified_at': user_addr.modified_at,
                    'user_id': user_addr.user_id
                }})
            else:
                return jsonify({'return': 'error', 'message': 'address not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching address : '+ str(e)})
    return jsonify({'return': 'no GET request'})

@app.route('/user_addr/<id>', methods=['PUT'])
@token_required
def update_user_addr(jwt_current_user, id):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            user_addr = UserAddress.query.filter_by(user_id=jwt_current_user.id,id=id).first()
            if user_addr:
                user_addr.address_line1 = data['address_line1']
                user_addr.address_line2 = data['address_line2']
                user_addr.city = data['city']
                user_addr.postal_code = data['postal_code']
                user_addr.country = data['country']
                user_addr.telephone = data['telephone']
                user_addr.mobile = data['mobile']
                user_addr.latitude = data['latitude']
                user_addr.longitude = data['longitude']
                user_addr.modified_at = datetime.datetime.now()
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'address updated'})
            else:
                return jsonify({'return': 'error', 'message': 'address not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error updating address : '+ str(e)})
    return jsonify({'return': 'no PUT request'})

@app.route('/user_addr/<id>', methods=['DELETE'])
@token_required
def delete_user_addr(jwt_current_user, id):
    if request.method == 'DELETE':
        try:
            user_addr = UserAddress.query.filter_by(user_id=jwt_current_user.id,id=id).first()
            if user_addr:
                db.session.delete(user_addr)
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'address deleted'})
            else:
                return jsonify({'return': 'error', 'message': 'address not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error deleting address : '+ str(e)})
    return jsonify({'return': 'no DELETE request'})





@app.route('/banner', methods=['GET'])
def banner():
    if request.method == 'GET':
        try:
            get_banner = BannerSection.query.all()
            if get_banner:
                banner = []
                for item in get_banner:
                    banner.append({
                        'id': item.id,
                        'banner_name_en': item.banner_name_en,
                        'banner_image_url': item.banner_image_url,
                        'status': item.status,
                        'banner_desc_en': item.banner_desc_en
                    })
                return jsonify({'return': 'success', 'message': 'banner fetched', 'data': banner})
            else:
                return jsonify({'return': 'error', 'message': 'banner not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching banner : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})




@app.route('/secondary_banner', methods=['GET'])
def secondary_banner():
    if request.method == 'GET':
        try:
            get_banner = SecondaryBanner.query.all()
            if get_banner:
                banner = []
                for item in get_banner:
                    banner.append({
                        'id': item.id,
                        'banner_name_en': item.banner_name_en,
                        'banner_image_url': item.banner_image_url,
                        'status': item.status,
                        'banner_desc_en': item.banner_desc_en
                    })
                return jsonify({'return': 'success', 'message': 'banner fetched', 'data': banner})
            else:
                return jsonify({'return': 'error', 'message': 'banner not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching banner : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


# @app.route('/notifications', methods=['GET'])
# def notifications():
#     if request.method == 'GET':
#         try:
#             get_notifications = Notifications.query.all()
#             if get_notifications:
#                 notifications = []
#                 for item in get_notifications:
#                     notifications.append({
#                         'id': item.id,
#                         'title': item.title,
#                         'message': item.message,
#                         'image_url': item.notification_image,
                        
#                     })
#                 return jsonify({'return': 'success', 'message': 'notifications fetched', 'data': notifications})
#             else:
#                 return jsonify({'return': 'error', 'message': 'notifications not found'})
#         except Exception as e:
#             return jsonify({'return': 'error', 'message': 'error fetching notifications : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})


# dev 2
@app.route('/notifications', methods=['GET'])
def notifications():
    if request.method == 'GET':
        try:
            get_notifications = Notifications.query.all()
            if get_notifications:
                notifications = []
                for item in get_notifications:
                    notifications.append({
                        'id': item.id,
                        'product_id':item.fk_product_id,
                        'title': item.title,
                        'message': item.message,
                        'image_url': item.notification_image,
                        
                    })
                return jsonify({'return': 'success', 'message': 'notifications fetched', 'data': notifications})
            else:
                return jsonify({'return': 'error', 'message': 'notifications not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching notifications : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})






@app.route('/get_categories', methods=['GET'])
def get_categories():
    if request.method == 'GET':
        try:
            categories = ProductCategory.query.all()
            categories_json = []
            for category in categories:
                category_json = {
                    'id': category.id,
                    'category_name_en': category.category_name_en,
                    'category_name_ar': category.category_name_ar,
                    'category_desc_en': category.category_desc_en,
                    'category_desc_ar': category.category_desc_ar,
                    'category_image_url': category.category_image_url,
                    'category_order': category.category_order,
                    'active': category.active,
                }
                categories_json.append(category_json)
            return jsonify({'return': 'success', 'categories': categories_json})
        except Exception as e:
            return jsonify({'return': 'error getting categories : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_subcategory', methods=['GET'])
def get_subcategory():
    if request.method == 'GET':
        try:
            get_subcategory = ProductSubCategory.query.filter_by(fk_prod_cat_id=request.args.get('category_id')).all()
            subcategories_json = []
            for subcategory in get_subcategory:
                subcategory_json = {
                    'id': subcategory.id,
                    'subcategory_name_en': subcategory.subcategory_name_en,
                    'subcategory_name_ar': subcategory.subcategory_name_ar,
                    'subcategory_desc_en': subcategory.subcategory_desc_en,
                    'subcategory_desc_ar': subcategory.subcategory_desc_ar,
                    'subcategory_image_url': subcategory.subcategory_image_url,
                    'subcategory_order': subcategory.subcategory_order,
                    'active': subcategory.active,
                }
                subcategories_json.append(subcategory_json)
            return jsonify({'return': 'success', 'subcategories': subcategories_json})
        except Exception as e:
            return jsonify({'return': 'error getting subcategories : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_products_images', methods=['GET'])
def get_products_images():
    if request.method == 'GET':
        try:
            get_products_images = ProductImages.query.filter_by(fk_product_id=request.args.get('product_id')).all()
            if get_products_images:
                products_images_json = []
                for product_image in get_products_images:
                    product_image_json = {
                        'id': product_image.id,
                        'image_url': product_image.product_image_url,
                    }
                    products_images_json.append(product_image_json)
                return jsonify({'return': 'success', 'product_images': products_images_json})
            else:
                return jsonify({'return': 'no product images found'})
        except Exception as e:
            return jsonify({'return': 'error getting product images : '+ str(e)})
    return jsonify({'return': 'no GET request'})


@app.route('/get_product_stocks', methods=['GET'])
def get_product_stocks():
    if request.method == 'GET':
        try:
            get_product_stocks = ProductStock.query.filter_by(fk_product_id=request.args.get('product_id')).all()
            if get_product_stocks:
                product_stocks_json = []
                for product_stock in get_product_stocks:
                    product_stock_json = {
                        'id': product_stock.id,
                        'product_price': product_stock.product_price,
                        'product_offer_price': product_stock.product_offer_price,
                        'product_purchase_price': product_stock.product_purchase_price,
                        'opening_stock': product_stock.opening_stock,
                        'min_stock': product_stock.min_stock,
                        'max_stock': product_stock.max_stock,
                        'main_rack_no': product_stock.main_rack_no,
                        'sub_rack_no': product_stock.sub_rack_no
                    }
                    product_stocks_json.append(product_stock_json)
                return jsonify({'return': 'success', 'product_stocks': product_stocks_json})
            else:
                return jsonify({'return': 'no product stocks found'})
        except Exception as e:
            return jsonify({'return': 'error getting product stocks : '+ str(e)})
    return jsonify({'return': 'no GET request'})


# @app.route('/get_product', methods=['GET'])
# def get_product():
#     if request.method == 'GET':
#         if request.args.get('parm') ==  'product_id':
#             try:
#                 get_product = Products.query.filter_by(id=request.args.get('id')).first()
#                 # get_product_stocks = ProductStock.query.filter_by(fk_product_id=request.args.get('id')).all()
#                 if get_product:
#                     product_json = {
#                         # 'id': get_product.id,
#                         'product_name_en': get_product.product_name_en,
#                         'product_name_ar': get_product.product_name_ar,
#                         'product_desc_en': get_product.product_desc_en,
#                         'product_desc_ar': get_product.product_desc_ar,

#                     }
#                     return jsonify({'return': 'success', 'product': product_json})
#                 else:
#                     return jsonify({'return': 'no product found'})
#             except Exception as e:
#                 return jsonify({'return': 'error getting product : '+ str(e)})
#         elif request.args.get('parm') ==  'category_id':
#             try:
#                 get_products = Products.query.filter_by(cat=int(request.args.get('id'))).all()
#                 if get_products:
#                     products_json = []
#                     products_stocks_json = []
#                     products_images_json = []
#                     for product in get_products: 
#                         product_json = {
#                             'id': product.id,
#                             'product_name_en': product.product_name_en,
#                             'product_name_ar': product.product_name_ar,
#                             'product_desc_en': product.product_desc_en,
#                             'product_desc_ar': product.product_desc_ar,
#                             'unit_quantity': product.unit_quantity,
#                             'product_code': product.product_code,
#                             'product_barcode': product.produc_barcode,
#                             'other_title_en': product.other_title_en,
#                             'other_title_ar': product.other_title_ar, 
#                             'status': product.status,
#                             'fast_delivery': product.fast_delivery,
#                             'featured': product.featured,
#                             'fresh': product.fresh,
#                             'offer': product.offer,
#                             'product_cat_id': product.cat,
#                             'product_subcat_id': product.subcat,
#                             'cat_id': product.cat,
#                             'subcat_id': product.subcat,
#                             'product_stock': [],
#                             'product_images': []
#                             # 'product_price': product.product_stock,
#                         }
#                         for product_stock in product.product_stock:
#                             product_stock_json = {
#                                 'id': product_stock.id,
#                                 'product_price': product_stock.product_price,
#                                 'product_offer_price': product_stock.product_offer_price,
#                                 'product_purchase_price': product_stock.product_purchase_price,
#                                 'opening_stock': product_stock.opening_stock,
#                                 'min_stock': product_stock.min_stock,
#                                 'max_stock': product_stock.max_stock,
#                                 'main_rack_no': product_stock.main_rack_no,
#                                 'sub_rack_no': product_stock.sub_rack_no,
#                                 'product_id': product_stock.fk_product_id,
#                             }
#                             products_stocks_json.append(product_stock_json)
#                             product_json['product_stock'] = products_stocks_json
#                         for product_image in product.product_image:
#                             product_image_json = {
#                                 'id': product_image.id,
#                                 'product_image_url': product_image.product_image_url,
#                                 'product_id': product_image.fk_product_id,
#                             }
#                             products_images_json.append(product_image_json)
#                             product_json['product_images'] = products_images_json

#                         products_images_json = []
#                         products_stocks_json = []
#                         products_json.append(product_json)
#                     return jsonify({'return': 'success', 'products': products_json})
#                 else:
#                     return jsonify({'return': 'no products'})
#             except Exception as e:
#                 return jsonify({'return': 'error getting products : '+ str(e)})
#         elif request.args.get('parm') ==  'subcategory_id':
#             try:
#                 get_products = Products.query.filter_by(subcat=request.args.get('id')).all()
#                 if get_products:
#                     products_json = []
#                     products_stocks_json = []
#                     products_images_json = []
#                     for product in get_products: 
#                         product_json = {
#                             'id': product.id,
#                             'product_name_en': product.product_name_en,
#                             'product_name_ar': product.product_name_ar,
#                             'product_desc_en': product.product_desc_en,
#                             'product_desc_ar': product.product_desc_ar,
#                             'unit_quantity': product.unit_quantity,
#                             'product_code': product.product_code,
#                             'product_barcode': product.produc_barcode,
#                             'other_title_en': product.other_title_en,
#                             'other_title_ar': product.other_title_ar, 
#                             'status': product.status,
#                             'fast_delivery': product.fast_delivery,
#                             'featured': product.featured,
#                             'fresh': product.fresh,
#                             'offer': product.offer,
#                             'product_cat_id': product.cat,
#                             'product_subcat_id': product.subcat,
#                             'cat_id': product.cat,
#                             'subcat_id': product.subcat,
#                             'product_stock': [],
#                             'product_images': []
#                             # 'product_price': product.product_stock,
#                         }
#                         for product_stock in product.product_stock:
#                             product_stock_json = {
#                                 'id': product_stock.id,
#                                 'product_price': product_stock.product_price,
#                                 'product_offer_price': product_stock.product_offer_price,
#                                 'product_purchase_price': product_stock.product_purchase_price,
#                                 'opening_stock': product_stock.opening_stock,
#                                 'min_stock': product_stock.min_stock,
#                                 'max_stock': product_stock.max_stock,
#                                 'main_rack_no': product_stock.main_rack_no,
#                                 'sub_rack_no': product_stock.sub_rack_no,
#                                 'product_id': product_stock.fk_product_id,
#                             }
#                             products_stocks_json.append(product_stock_json)
#                             product_json['product_stock'] = products_stocks_json
#                         for product_image in product.product_image:
#                             product_image_json = {
#                                 'id': product_image.id,
#                                 'product_image_url': product_image.product_image_url,
#                                 'product_id': product_image.fk_product_id,
#                             }
#                             products_images_json.append(product_image_json)
#                             product_json['product_images'] = products_images_json

#                         products_images_json = []
#                         products_stocks_json = []
#                         products_json.append(product_json)
#                     return jsonify({'return': 'success', 'products': products_json})
#                 else:
#                     return jsonify({'return': 'no products'})
#             except Exception as e:
#                 return jsonify({'return': 'error getting products : '+ str(e)})
            
        


        




#         elif request.args.get('parm') ==  'all':
#             try:
#                 get_products = Products.query.all()
#                 if get_products:
#                     products_json = []
#                     products_stocks_json = []
#                     products_images_json = []
#                     for product in get_products: 
#                         product_json = {
#                             'id': product.id,
#                             'product_name_en': product.product_name_en,
#                             'product_name_ar': product.product_name_ar,
#                             'product_desc_en': product.product_desc_en,
#                             'product_desc_ar': product.product_desc_ar,
#                             'unit_quantity': product.unit_quantity,
#                             'product_code': product.product_code,
#                             'product_barcode': product.produc_barcode,
#                             'other_title_en': product.other_title_en,
#                             'other_title_ar': product.other_title_ar, 
#                             'status': product.status,
#                             'fast_delivery': product.fast_delivery,
#                             'featured': product.featured,
#                             'fresh': product.fresh,
#                             'offer': product.offer,
#                             'product_cat_id': product.cat,
#                             'product_subcat_id': product.subcat,
#                             'cat_id': product.cat,
#                             'subcat_id': product.subcat,
#                             'product_stock': [],
#                             'product_images': []
#                             # 'product_price': product.product_stock,
#                         }
#                         for product_stock in product.product_stock:
#                             product_stock_json = {
#                                 'id': product_stock.id,
#                                 'product_price': product_stock.product_price,
#                                 'product_offer_price': product_stock.product_offer_price,
#                                 'product_purchase_price': product_stock.product_purchase_price,
#                                 'opening_stock': product_stock.opening_stock,
#                                 'min_stock': product_stock.min_stock,
#                                 'max_stock': product_stock.max_stock,
#                                 'main_rack_no': product_stock.main_rack_no,
#                                 'sub_rack_no': product_stock.sub_rack_no,
#                                 'product_id': product_stock.fk_product_id,
#                             }
#                             products_stocks_json.append(product_stock_json)
#                             product_json['product_stock'] = products_stocks_json
#                         for product_image in product.product_image:
#                             product_image_json = {
#                                 'id': product_image.id,
#                                 'product_image_url': product_image.product_image_url,
#                                 'product_id': product_image.fk_product_id,
#                             }
#                             products_images_json.append(product_image_json)
#                             product_json['product_images'] = products_images_json

#                         products_images_json = []
#                         products_stocks_json = []
#                         products_json.append(product_json)
#                     return jsonify({'return': 'success', 'products': products_json})
#                 else:
#                     return jsonify({'return': 'no products'})
#             except Exception as e:
#                 return jsonify({'return': 'error getting products : '+ str(e)})

# @app.route('/get_products/fast_delivery', methods=['GET'])
# def get_fast_delivery_products():
#     if request.method == 'GET':
#         try:
#             get_products = Products.query.filter_by(fast_delivery="1").all()
#             if get_products:
#                 products_json = []
#                 products_stocks_json = []
#                 products_images_json = []
#                 for product in get_products: 
#                     product_json = {
#                         'id': product.id,
#                         'product_name_en': product.product_name_en,
#                         'product_name_ar': product.product_name_ar,
#                         'product_desc_en': product.product_desc_en,
#                         'product_desc_ar': product.product_desc_ar,
#                         'unit_quantity': product.unit_quantity,
#                         'product_code': product.product_code,
#                         'product_barcode': product.produc_barcode,
#                         'other_title_en': product.other_title_en,
#                         'other_title_ar': product.other_title_ar, 
#                         'status': product.status,
#                         'fast_delivery': product.fast_delivery,
#                         'featured': product.featured,
#                         'fresh': product.fresh,
#                         'offer': product.offer,
#                         'product_cat_id': product.cat,
#                         'product_subcat_id': product.subcat,
#                         'cat_id': product.cat,
#                         'subcat_id': product.subcat,
#                         'product_stock': [],
#                         'product_images': []
#                         # 'product_price': product.product_stock,
#                     }
#                     for product_stock in product.product_stock:
#                         product_stock_json = {
#                             'id': product_stock.id,
#                             'product_price': product_stock.product_price,
#                             'product_offer_price': product_stock.product_offer_price,
#                             'product_purchase_price': product_stock.product_purchase_price,
#                             'opening_stock': product_stock.opening_stock,
#                             'min_stock': product_stock.min_stock,
#                             'max_stock': product_stock.max_stock,
#                             'main_rack_no': product_stock.main_rack_no,
#                             'sub_rack_no': product_stock.sub_rack_no,
#                             'product_id': product_stock.fk_product_id,
#                         }
#                         products_stocks_json.append(product_stock_json)
#                         product_json['product_stock'] = products_stocks_json
#                     for product_image in product.product_image:
#                         product_image_json = {
#                             'id': product_image.id,
#                             'product_image_url': product_image.product_image_url,
#                             'product_id': product_image.fk_product_id,
#                         }
#                         products_images_json.append(product_image_json)
#                         product_json['product_images'] = products_images_json

#                     products_images_json = []
#                     products_stocks_json = []
#                     products_json.append(product_json)
#                 return jsonify({'return': 'success', 'products': products_json})
#             else:
#                 return jsonify({'return': 'no products'})
#         except Exception as e:
#             return jsonify({'return': 'error getting products : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})

# @app.route('/get_products/normal_delivery', methods=['GET'])
# def get_normal_delivery_products():
#     if request.method == 'GET':
#         try:
#             get_products = Products.query.filter_by(fast_delivery="0").all()
#             if get_products:
#                 products_json = []
#                 products_stocks_json = []
#                 products_images_json = []
#                 for product in get_products: 
#                     product_json = {
#                         'id': product.id,
#                         'product_name_en': product.product_name_en,
#                         'product_name_ar': product.product_name_ar,
#                         'product_desc_en': product.product_desc_en,
#                         'product_desc_ar': product.product_desc_ar,
#                         'unit_quantity': product.unit_quantity,
#                         'product_code': product.product_code,
#                         'product_barcode': product.produc_barcode,
#                         'other_title_en': product.other_title_en,
#                         'other_title_ar': product.other_title_ar, 
#                         'status': product.status,
#                         'fast_delivery': product.fast_delivery,
#                         'featured': product.featured,
#                         'fresh': product.fresh,
#                         'offer': product.offer,
#                         'product_cat_id': product.cat,
#                         'product_subcat_id': product.subcat,
#                         'cat_id': product.cat,
#                         'subcat_id': product.subcat,
#                         'product_stock': [],
#                         'product_images': []
#                         # 'product_price': product.product_stock,
#                     }
#                     for product_stock in product.product_stock:
#                         product_stock_json = {
#                             'id': product_stock.id,
#                             'product_price': product_stock.product_price,
#                             'product_offer_price': product_stock.product_offer_price,
#                             'product_purchase_price': product_stock.product_purchase_price,
#                             'opening_stock': product_stock.opening_stock,
#                             'min_stock': product_stock.min_stock,
#                             'max_stock': product_stock.max_stock,
#                             'main_rack_no': product_stock.main_rack_no,
#                             'sub_rack_no': product_stock.sub_rack_no,
#                             'product_id': product_stock.fk_product_id,
#                         }
#                         products_stocks_json.append(product_stock_json)
#                         product_json['product_stock'] = products_stocks_json
#                     for product_image in product.product_image:
#                         product_image_json = {
#                             'id': product_image.id,
#                             'product_image_url': product_image.product_image_url,
#                             'product_id': product_image.fk_product_id,
#                         }
#                         products_images_json.append(product_image_json)
#                         product_json['product_images'] = products_images_json

#                     products_images_json = []
#                     products_stocks_json = []
#                     products_json.append(product_json)
#                 return jsonify({'return': 'success', 'products': products_json})
#             else:
#                 return jsonify({'return': 'no products'})
#         except Exception as e:
#             return jsonify({'return': 'error getting products : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})



# dev2
@app.route('/get_products', methods=['GET'])
def get_products():
    if request.method == 'GET':
        try:
            # Get request parameters
            category_id = request.args.get('category_id')
            subcategory_id = request.args.get('subcategory_id')
            delivery_type = request.args.get('delivery_type')

            # Query products based on parameters
            query = Products.query
            if category_id:
                query = query.filter_by(cat=category_id)
            if subcategory_id:
                query = query.filter_by(subcat=subcategory_id)
            if delivery_type == 'fast':
                query = query.filter_by(fast_delivery="1")
            elif delivery_type == 'normal':
                query = query.filter_by(fast_delivery="0")

            products = query.all()

            # Format products into JSON response
            if products:
                products_json = []
                for product in products:
                    product_json = {
                        'id': product.id,
                        'product_name_en': product.product_name_en,
                        'product_name_ar': product.product_name_ar,
                        'product_desc_en': product.product_desc_en,
                        'product_desc_ar': product.product_desc_ar,
                        'unit_quantity': product.unit_quantity,
                        'product_code': product.product_code,
                        'product_barcode': product.produc_barcode,
                        'other_title_en': product.other_title_en,
                        'other_title_ar': product.other_title_ar, 
                        'status': product.status,
                        'fast_delivery': product.fast_delivery,
                        'featured': product.featured,
                        'fresh': product.fresh,
                        'offer': product.offer,
                        'product_cat_id': product.cat,
                        'product_subcat_id': product.subcat,
                        'cat_id': product.cat,
                        'subcat_id': product.subcat,
                        'product_stock': [],
                        'product_images': []
                    }
                    for product_stock in product.product_stock:
                        product_stock_json = {
                            'id': product_stock.id,
                            'product_price': product_stock.product_price,
                            'product_offer_price': product_stock.product_offer_price,
                            'product_purchase_price': product_stock.product_purchase_price,
                            'opening_stock': product_stock.opening_stock,
                            'min_stock': product_stock.min_stock,
                            'max_stock': product_stock.max_stock,
                            'main_rack_no': product_stock.main_rack_no,
                            'sub_rack_no': product_stock.sub_rack_no,
                            'product_id': product_stock.fk_product_id,
                        }
                        product_json['product_stock'].append(product_stock_json)
                    for product_image in product.product_image:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        product_json['product_images'].append(product_image_json)
                    products_json.append(product_json)

                return jsonify({'return': 'success', 'products': products_json})
            else:
                return jsonify({'return': 'no products'})
        except Exception as e:
            return jsonify({'return': 'error getting products : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})



@app.route('/products', methods=['GET'])
def search_products():
    if request.method == 'GET':
        key = request.args.get('search')

        try:
            get_products = Products.query.filter(Products.product_name_en.ilike('%'+key+'%')).all()
            if get_products:
                products_json = []
                products_stocks_json = []
                products_images_json = []
                for product in get_products: 
                    product_json = {
                        'id': product.id,
                        'product_name_en': product.product_name_en,
                        'product_name_ar': product.product_name_ar,
                        'product_desc_en': product.product_desc_en,
                        'product_desc_ar': product.product_desc_ar,
                        'unit_quantity': product.unit_quantity,
                        'product_code': product.product_code,
                        'product_barcode': product.produc_barcode,
                        'other_title_en': product.other_title_en,
                        'other_title_ar': product.other_title_ar, 
                        'status': product.status,
                        'fast_delivery': product.fast_delivery,
                        'featured': product.featured,
                        'fresh': product.fresh,
                        'offer': product.offer,
                        'product_cat_id': product.cat,
                        'product_subcat_id': product.subcat,
                        'cat_id': product.cat,
                        'subcat_id': product.subcat,
                        'product_stock': [],
                        'product_images': []
                        # 'product_price': product.product_stock,
                    }
                    for product_stock in product.product_stock:
                        product_stock_json = {
                            'id': product_stock.id,
                            'product_price': product_stock.product_price,
                            'product_offer_price': product_stock.product_offer_price,
                            'product_purchase_price': product_stock.product_purchase_price,
                            'opening_stock': product_stock.opening_stock,
                            'min_stock': product_stock.min_stock,
                            'max_stock': product_stock.max_stock,
                            'main_rack_no': product_stock.main_rack_no,
                            'sub_rack_no': product_stock.sub_rack_no,
                            'product_id': product_stock.fk_product_id,
                        }
                        products_stocks_json.append(product_stock_json)
                        product_json['product_stock'] = products_stocks_json
                    for product_image in product.product_image:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        products_images_json.append(product_image_json)
                        product_json['product_images'] = products_images_json

                    products_images_json = []
                    products_stocks_json = []
                    products_json.append(product_json)
                return jsonify({'return': 'success', 'products': products_json})
            else:
                return jsonify({'return': 'no products'})
        except Exception as e:
            return jsonify({'return': 'error getting products : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'invalid request method'})
        


@app.route('/changeProductStatus/<status>')
def changeProductStatus(status):
    if request.method == 'GET':
        try:
            get_product = Products.query.filter_by(id=request.args.get('id')).first()
            if get_product:
                if status == 'check':
                    return jsonify({'return': 'success', 'status': get_product.status})
                else:
                    get_product.status = status
                    db.session.commit()
                    return jsonify({'return': 'success', 'message': 'product status changed'})
            else:
                return jsonify({'return': 'error', 'message': 'product not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error changing product status : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})








@app.route('/get_products/featured', methods=['GET'])
def get_featured_products():
    if request.method == 'GET':
        try:
            get_products = Products.query.filter_by(featured='yes').all()
            if get_products:
                products_json = []
                products_stocks_json = []
                products_images_json = []
                for product in get_products: 
                    product_json = {
                        'id': product.id,
                        'product_name_en': product.product_name_en,
                        'product_name_ar': product.product_name_ar,
                        'product_desc_en': product.product_desc_en,
                        'product_desc_ar': product.product_desc_ar,
                        'unit_quantity': product.unit_quantity,
                        'product_code': product.product_code,
                        'product_barcode': product.produc_barcode,
                        'other_title_en': product.other_title_en,
                        'other_title_ar': product.other_title_ar, 
                        'status': product.status,
                        'fast_delivery': product.fast_delivery,
                        'featured': product.featured,
                        'fresh': product.fresh,
                        'offer': product.offer,
                        'product_cat_id': product.cat,
                        'product_subcat_id': product.subcat,
                        'cat_id': product.cat,
                        'subcat_id': product.subcat,
                        'product_stock': [],
                        'product_images': []
                        # 'product_price': product.product_stock,
                    }
                    for product_stock in product.product_stock:
                        product_stock_json = {
                            'id': product_stock.id,
                            'product_price': product_stock.product_price,
                            'product_offer_price': product_stock.product_offer_price,
                            'product_purchase_price': product_stock.product_purchase_price,
                            'opening_stock': product_stock.opening_stock,
                            'min_stock': product_stock.min_stock,
                            'max_stock': product_stock.max_stock,
                            'main_rack_no': product_stock.main_rack_no,
                            'sub_rack_no': product_stock.sub_rack_no,
                            'product_id': product_stock.fk_product_id,
                        }
                        products_stocks_json.append(product_stock_json)
                        product_json['product_stock'] = products_stocks_json
                    for product_image in product.product_image:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        products_images_json.append(product_image_json)
                        product_json['product_images'] = products_images_json

                    products_images_json = []
                    products_stocks_json = []
                    products_json.append(product_json)
                return jsonify({'return': 'success', 'products': products_json})
            else:
                return jsonify({'return': 'no products'})
        except Exception as e:
            return jsonify({'return': 'error getting products : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})







@app.route('/cart/<product_id>', methods=['POST'])
@token_required
def addToCart(jwt_current_user, product_id):
    if request.method == 'POST':
        content=request.get_json()
        checkcartitem = CartItem.query.filter_by(fk_product_id=product_id).first()
        try:
           
            if checkcartitem:
                checkcartitem.quantity = int(float(checkcartitem.quantity)) + int(content['quantity'])
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'product quantity updated'})
        
            get_product = Products.query.filter_by(id=product_id).first()
            if get_product:
                # if int(content['quantity']) < int(checkcartitem.quantity):
                #     return jsonify({'return': 'error', 'message': 'Requested Product stock is not available, Available stock is '+ str(checkcartitem.quantity)})

                addtoCart =  CartItem(fk_user_id=jwt_current_user.id, 
                                        fk_product_id=get_product.id, 
                                        quantity=content['quantity'],
                                        created_at=datetime.datetime.now(),
                                        modified_at=datetime.datetime.now())
                db.session.add(addtoCart)
                db.session.commit()
                return jsonify({'return': 'success', 'message': get_product.product_name_en + 'product added to cart'})
            else:
                return jsonify({'return': 'error', 'message': 'product not found'})
        except Exception as e: 
            return jsonify({'return': 'error', 'message': 'error adding product to cart : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/cart', methods=['GET'])
@token_required
def getCartItems(jwt_current_user):
    if request.method == 'GET':
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id).all()
            
            if get_cart:
                cart_json = []
                products_stocks_json = []
                products_images_json = []
                for cart in get_cart:
                    get_product_stocks = ProductStock.query.filter_by(fk_product_id=cart.fk_product_id).all()
                    for product_stock in get_product_stocks:
                        product_stock_json = {
                            'id': product_stock.id,
                            'product_price': product_stock.product_price,
                            'product_offer_price': product_stock.product_offer_price,
                            'product_purchase_price': product_stock.product_purchase_price,
                            'opening_stock': product_stock.opening_stock,
                            'min_stock': product_stock.min_stock,
                            'max_stock': product_stock.max_stock,
                            'main_rack_no': product_stock.main_rack_no,
                            'sub_rack_no': product_stock.sub_rack_no,
                            'product_id': product_stock.fk_product_id,
                        }
                        products_stocks_json.append(product_stock_json)
                    get_product_images = ProductImages.query.filter_by(fk_product_id=cart.fk_product_id).all()
                    for product_image in get_product_images:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        products_images_json.append(product_image_json)
                    cart_json.append({
                        'id': cart.id,
                        'user_id': cart.fk_user_id,
                        'product_id': cart.fk_product_id,
                        'product_name_en': cart.cart_item.product_name_en,
                        'product_name_ar': cart.cart_item.product_name_ar,
                        'product_desc_en': cart.cart_item.product_desc_en,
                        'product_desc_ar': cart.cart_item.product_desc_ar,
                        'unit_quantity': cart.cart_item.unit_quantity,
                        'product_code': cart.cart_item.product_code,
                        'product_barcode': cart.cart_item.produc_barcode,
                        'other_title_en': cart.cart_item.other_title_en,
                        'other_title_ar': cart.cart_item.other_title_ar, 
                        'status': cart.cart_item.status,
                        'fast_delivery': cart.cart_item.fast_delivery,
                        'featured': cart.cart_item.featured,
                        'fresh': cart.cart_item.fresh,
                        'offer': cart.cart_item.offer,
                        'product_cat_id': cart.cart_item.cat,
                        'product_subcat_id': cart.cart_item.subcat,
                        'cat_id': cart.cart_item.cat,
                        'subcat_id': cart.cart_item.subcat,
                        'product_stock': product_stock_json,
                        'product_images': products_images_json,
                        'quantity': cart.quantity,
                        'created_at': cart.created_at,
                        'modified_at': cart.modified_at
                    })
                    products_stocks_json = []
                    products_images_json = []
                    
                return jsonify({'return': 'success', 'cart_items': cart_json})
            else:
                return jsonify({'return': 'error', 'message': 'cart is empty'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error getting cart items : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})

               
@app.route('/cart/itemDelete/<product_id>', methods=['DELETE'])
@token_required
def deleteCartItem(jwt_current_user, product_id):
    if request.method == 'DELETE':
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            # if int(get_cart.unit_quantity) < 1:
            #     return jsonify({'return': 'error', 'message': 'unit quantity must be greater than 0'})
            if get_cart:
                get_cart.modified_at = datetime.datetime.now()
                db.session.delete(get_cart)
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'cart item deleted'})
            else:
                return jsonify({'return': 'error', 'message': 'cart item not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error deleting cart item : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/cart/clear', methods=['DELETE'])
@token_required
def clearCart(jwt_current_user):
    if request.method == 'DELETE':
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id).all()
            if get_cart:
                for cart in get_cart:
                    db.session.delete(cart)
                    db.session.commit()
                return jsonify({'return': 'success', 'message': 'cart cleared'})
            else:
                return jsonify({'return': 'error', 'message': 'cart is empty'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error clearing cart : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/cart/incQty/<product_id>', methods=['PUT'])
@token_required
def incQty(jwt_current_user, product_id):
    if request.method == 'PUT':
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            product_stock = ProductStock.query.filter_by(fk_product_id=product_id).first()
            # if int(float(get_cart.quantity)) >= int(float(product_stock.min_stock)):
            #     return jsonify({'return': 'error', 'message': 'quantity must be less than min stock'})
            if get_cart:
                get_cart.quantity = int(float(get_cart.quantity)) + 1
                get_cart.modified_at = datetime.datetime.now()
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'quantity increased'})
            else:
                return jsonify({'return': 'error', 'message': 'cart item not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error increasing quantity : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/cart/decQty/<product_id>', methods=['PUT'])
@token_required
def decQty(jwt_current_user, product_id):
    if request.method == 'PUT':
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            product_stock = ProductStock.query.filter_by(fk_product_id=product_id).first()
            if get_cart:
                if int(float(get_cart.quantity)) > 1:
                    get_cart.quantity = int(float(get_cart.quantity)) - 1
                    get_cart.modified_at = datetime.datetime.now()
                    db.session.commit()
                    return jsonify({'return': 'success', 'message': 'quantity decreased'})
                else:
                    db.session.delete(get_cart)
                    db.session.commit()
                    return jsonify({'return': 'success', 'message': 'cart item deleted'})
                    
            else:
                return jsonify({'return': 'error', 'message': 'cart item not found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error decreasing quantity : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})





@app.route('/wishlist/<product_id>', methods=['POST'])
@token_required
def addWishlist(jwt_current_user, product_id):
    if request.method == 'POST':
        try:
            get_wishlist = UserWhishlist.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            if get_wishlist:
                return jsonify({'return': 'error', 'message': 'product already in wishlist'})
            else:
                new_wishlist = UserWhishlist(fk_user_id=jwt_current_user.id, fk_product_id=product_id, created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
                db.session.add(new_wishlist)
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'product added to wishlist'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error adding product to wishlist : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})

@app.route('/wishlist', methods=['GET'])
@token_required
def getWishlist(jwt_current_user):
    if request.method == 'GET':
        try:
            get_wishlist = UserWhishlist.query.filter_by(fk_user_id=jwt_current_user.id).all()
            if get_wishlist:
                wishlist = []
                products_stocks_json = []
                products_images_json = []
                for item in get_wishlist:
                    # get_product = Products.query.filter_by(id=item.fk_product_id).first()
                    get_product_stocks = ProductStock.query.filter_by(fk_product_id=item.fk_product_id).all()
                    for product_stock in get_product_stocks:
                        product_stock_json = {
                            'id': product_stock.id,
                            'product_price': product_stock.product_price,
                            'product_offer_price': product_stock.product_offer_price,
                            'product_purchase_price': product_stock.product_purchase_price,
                            'opening_stock': product_stock.opening_stock,
                            'min_stock': product_stock.min_stock,
                            'max_stock': product_stock.max_stock,
                            'main_rack_no': product_stock.main_rack_no,
                            'sub_rack_no': product_stock.sub_rack_no,
                            'product_id': product_stock.fk_product_id,
                        }
                        products_stocks_json.append(product_stock_json)
                    get_product_images = ProductImages.query.filter_by(fk_product_id=item.fk_product_id).all()
                    for product_image in get_product_images:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        products_images_json.append(product_image_json)
                    wishlist.append({
                        'id': item.id,
                        'user_id': item.fk_user_id,
                        'product_id': item.fk_product_id,
                        'product_name_en': item.user_whishlist.product_name_en,
                        'product_name_ar': item.user_whishlist.product_name_ar,
                        'product_desc_en': item.user_whishlist.product_desc_en,
                        'product_desc_ar': item.user_whishlist.product_desc_ar,
                        'unit_quantity': item.user_whishlist.unit_quantity,
                        'product_code': item.user_whishlist.product_code,
                        'product_barcode': item.user_whishlist.produc_barcode,
                        'other_title_en': item.user_whishlist.other_title_en,
                        'other_title_ar': item.user_whishlist.other_title_ar, 
                        'status': item.user_whishlist.status,
                        'fast_delivery': item.user_whishlist.fast_delivery,
                        'featured': item.user_whishlist.featured,
                        'fresh': item.user_whishlist.fresh,
                        'offer': item.user_whishlist.offer,
                        'product_cat_id': item.user_whishlist.cat,
                        'product_subcat_id': item.user_whishlist.subcat,
                        'cat_id': item.user_whishlist.cat,
                        'subcat_id': item.user_whishlist.subcat,
                        'product_stock': product_stock_json,
                        'product_images': products_images_json,
                        'created_at': item.created_at,
                        'modified_at': item.modified_at
                    })
                    products_stocks_json = []
                    products_images_json = []
                return jsonify({'return': 'success', 'message': 'wishlist fetched', 'data': wishlist})
            else:
                return jsonify({'return': 'error', 'message': 'wishlist is empty'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error fetching wishlist : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})

@app.route('/wishlist/<product_id>', methods=['DELETE'])
@token_required
def deleteWishlist(jwt_current_user, product_id):
    if request.method == 'DELETE':
        try:
            get_wishlist = UserWhishlist.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            if get_wishlist:
                db.session.delete(get_wishlist)
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'product removed from wishlist'})
            else:
                return jsonify({'return': 'error', 'message': 'product not found in wishlist'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error removing product from wishlist : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})

@app.route('/wishlist/clear', methods=['DELETE'])
@token_required
def clearWishlist(jwt_current_user):
    if request.method == 'DELETE':
        try:
            get_wishlist = UserWhishlist.query.filter_by(fk_user_id=jwt_current_user.id).all()
            if get_wishlist:
                for item in get_wishlist:
                    db.session.delete(item)
                    db.session.commit()
                return jsonify({'return': 'success', 'message': 'wishlist cleared'})
            else:
                return jsonify({'return': 'error', 'message': 'wishlist is empty'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error clearing wishlist : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})

@app.route('/wishlist/check/<product_id>', methods=['GET'])
@token_required
def checkWishlist(jwt_current_user, product_id):
    if request.method == 'GET':
        try:
            get_wishlist = UserWhishlist.query.filter_by(fk_user_id=jwt_current_user.id, fk_product_id=product_id).first()
            if get_wishlist:
                return jsonify({'return': 'True', 'message': 'product found in wishlist'})
            else:
                return jsonify({'return': 'False', 'message': 'product not found in wishlist'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error checking wishlist : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})





@app.route('/order/<addr_id>', methods=['POST'])
@token_required
def cartToOrder(jwt_current_user, addr_id):
    if request.method == 'POST':
        content = request.get_json()
        try:
            get_cart = CartItem.query.filter_by(fk_user_id=jwt_current_user.id).all()
            # get_cart_items = Products.query.filter_by(id=get_cart.fk_product_id).all()
            # get_item_stocks = ProductStock.query.filter_by(fk_product_id=get_cart.fk_product_id1).all()
            if get_cart:
                total_price = 0
                total_quantity = 0
                for item in get_cart:
                    get_item_stocks = ProductStock.query.filter_by(fk_product_id=item.fk_product_id).first()
                    total_price += int(float(get_item_stocks.product_offer_price)) * int(float(item.quantity))
                    total_quantity = total_quantity + 1
                delivery_type = content.get('delivery_type')
                delivery_time = content.get('delivery_time')

                order = Order(
                    fk_user_id=jwt_current_user.id,
                    total_price=total_price,
                    total_quantity=total_quantity,
                    address_id=addr_id,
                    # payment_method= get_cart,
                    status='pending',
                    created_at=datetime.datetime.now(),
                    modified_at=datetime.datetime.now(),
                    delivery_type=delivery_type,
                    delivery_time=delivery_time
                )
                db.session.add(order)
                db.session.commit()

                for item in get_cart:   
                    order_item = OrderDetails(
                        fk_order_id=order.id,
                        fk_product_id=item.fk_product_id,
                        item_quantity=item.quantity,
                        transaction_id=content['transaction_id'],
                        order_date=datetime.datetime.now()
                
                    )
                    db.session.add(order_item)
                    db.session.commit()

                #clear cart
                for item in get_cart:
                    db.session.delete(item)
                    db.session.commit()
                
                return jsonify({'return': 'success', 'message': 'order placed'})
        
            return jsonify({'return': 'error', 'message': 'No Cart found'})
                    
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error placing order : '+ str(e)})
            
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/order', methods=['GET'])
@token_required
def getOrders(jwt_current_user):
    if request.method == 'GET':
        try:
            get_orders = Order.query.filter_by(fk_user_id=jwt_current_user.id).all()
            if get_orders:
                orders = []
                for item in get_orders:
                    orders.append({
                        'id': item.id,
                        'total_price': item.total_price,
                        'total_quantity': item.total_quantity,
                        'address_id': item.address_id,
                        'status': item.status,
                        'created_at': item.created_at,
                        'modified_at': item.modified_at,
                        'delivery_time': item.delivery_time,
                        'delivery_type': item.delivery_type
                    })
                return jsonify({'return': 'success', 'orders': orders})
            else:
                return jsonify({'return': 'error', 'message': 'No Orders found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error getting orders : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/order/<order_id>', methods=['GET'])
@token_required
def getOrderDetails(jwt_current_user, order_id):
    if request.method == 'GET':
        try:
            get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id, id=order_id).first()
            if get_order:
                order_details = {
                        'id': get_order.id,
                        'total_price': get_order.total_price,
                        'total_quantity': get_order.total_quantity,
                        'address_id': get_order.address_id,
                        'status': get_order.status,
                        'created_at': get_order.created_at,
                        'modified_at': get_order.modified_at,
                        'delivery_time': get_order.delivery_time,
                        'delivery_type': get_order.delivery_type
                    }

                return jsonify({'return': 'success', 'order_details': order_details})
            else:
                return jsonify({'return': 'error', 'message': 'No Order found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error getting order details : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})



# # @app.route('/order/details', methods=['GET'])
# # @token_required
# # def getAllOrderDetailsWithProduct(jwt_current_user):
#     if request.method == 'GET':
#         try:
#             get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id).all()
#             if get_order:
#                 order_details = []
#                 for item in get_order:
#                     get_order_details = OrderDetails.query.filter_by(fk_order_id=item.id).all()
#                     for item in get_order_details:
#                         get_product = Products.query.filter_by(id=item.fk_product_id).first()
#                         order_details.append({
#                             'id': item.id,
#                             'fk_order_id': item.fk_order_id,
#                             'fk_product_id': item.fk_product_id,
#                             'order_date': item.order_date,
                           
#                         })
#                 return jsonify({'return': 'success', 'order_details': order_details})
#             else:
#                 return jsonify({'return': 'error', 'message': 'No Order found'})
#         except Exception as e:
#             return jsonify({'return': 'error', 'message': 'error getting order details : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/order/<order_id>', methods=['DELETE'])
@token_required
def cancelOrder(jwt_current_user, order_id):
    if request.method == 'DELETE':
        try:
            get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id, id=order_id).first()
            if get_order:
                get_order.status = 'cancelled'
                db.session.commit()
                return jsonify({'return': 'success', 'message': 'order cancelled'})
            else:
                return jsonify({'return': 'error', 'message': 'No Order found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error cancelling order : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


@app.route('/order/details/<order_id>', methods=['GET'])
@token_required
def getOrderDetailsWithProduct(jwt_current_user, order_id):
    if request.method == 'GET':
        try:
            get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id, id=order_id).first()
            if get_order:
                get_order_details = OrderDetails.query.filter_by(fk_order_id=get_order.id).all()
                order_details = []
                products_images_json = []
                products_stocks_json = []

                for item in get_order_details:
                    product = Products.query.filter_by(id=item.fk_product_id).first()
                    get_product_stocks = ProductStock.query.filter_by(fk_product_id=product.id).all()
                    for product_stock in get_product_stocks:
                            product_stock_json = {
                                'id': product_stock.id,
                                'product_price': product_stock.product_price,
                                'product_offer_price': product_stock.product_offer_price,
                                'product_purchase_price': product_stock.product_purchase_price,
                                'opening_stock': product_stock.opening_stock,
                                'min_stock': product_stock.min_stock,
                                'max_stock': product_stock.max_stock,
                                'main_rack_no': product_stock.main_rack_no,
                                'sub_rack_no': product_stock.sub_rack_no,
                                'product_id': product_stock.fk_product_id,
                            }
                            products_stocks_json.append(product_stock_json)
                            # order_details['product_stock'] = products_stocks_json
                    get_product_images = ProductImages.query.filter_by(fk_product_id=product.id).all()
                    for product_image in get_product_images:
                        product_image_json = {
                            'id': product_image.id,
                            'product_image_url': product_image.product_image_url,
                            'product_id': product_image.fk_product_id,
                        }
                        products_images_json.append(product_image_json)
                        # order_details['product_images'] = products_images_json

                    order_details.append({
                        'order_id': item.id,
                        'fk_order_id': item.fk_order_id,
                        'fk_product_id': item.fk_product_id,
                        'item_quantity': item.item_quantity,
                        'address_id': get_order.address_id,
                        'order_date': item.order_date,
                        'product_id': product.id,
                        'product_name_en': product.product_name_en,
                        'product_name_ar': product.product_name_ar,
                        'product_desc_en': product.product_desc_en,
                        'product_desc_ar': product.product_desc_ar,
                        'unit_quantity': product.unit_quantity,
                        'product_code': product.product_code,
                        'product_barcode': product.produc_barcode,
                        'other_title_en': product.other_title_en,
                        'other_title_ar': product.other_title_ar, 
                        'status': product.status,
                        'fast_delivery': product.fast_delivery,
                        'featured': product.featured,
                        'fresh': product.fresh,
                        'offer': product.offer,
                        'product_cat_id': product.cat,
                        'product_subcat_id': product.subcat,
                        'cat_id': product.cat,
                        'subcat_id': product.subcat,
                        'product_stock': product_stock_json,
                        'product_images': products_images_json
                    })
                    products_images_json = []
                    products_stocks_json = []
                return jsonify({'return': 'success', 'order_details': order_details})
            else:
                return jsonify({'return': 'error', 'message': 'No Order found'})
        except Exception as e:
            return jsonify({'return': 'error', 'message': 'error getting order details : '+ str(e)})
    else:
        return jsonify({'return': 'error', 'message': 'method not allowed'})


# @app.route('/order', methods=['DELETE'])
# @token_required
# def deleteAllOrder(jwt_current_user):
#     if request.method == 'DELETE':
#         try:
#             get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id).all()
#             if get_order:
#                 for item in get_order:
#                     db.session.delete(item)
#                     db.session.commit()
#                 return jsonify({'return': 'success', 'message': 'Order deleted successfully'})
#             else:
#                 return jsonify({'return': 'error', 'message': 'No Order found'})
#         except Exception as e:
#             return jsonify({'return': 'error', 'message': 'error deleting order : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})

# @app.route('/order/details', methods=['DELETE'])
# @token_required
# def deleteAllOrderDetails(jwt_current_user):
#     if request.method == 'DELETE':
#         try:
#             get_order = Order.query.filter_by(fk_user_id=jwt_current_user.id).all()
#             if get_order:
#                 for item in get_order:
#                     get_order_details = OrderDetails.query.filter_by(fk_order_id=item.id).all()
#                     for item in get_order_details:
#                         db.session.delete(item)
#                         db.session.commit()
#                 return jsonify({'return': 'success', 'message': 'Order deleted successfully'})
#             else:
#                 return jsonify({'return': 'error', 'message': 'No Order found'})
#         except Exception as e:
#             return jsonify({'return': 'error', 'message': 'error deleting order : '+ str(e)})
#     else:
#         return jsonify({'return': 'error', 'message': 'method not allowed'})
    

# @app.route('/order/<id>', methods=['PUT'])
# @token_required
# def updateOrder(jwt_current_user, id):



















## ------------------------------------------------------------------- APIs ------------------------------------------------------------------- ##
















































@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
        flash('Invalid username or password')
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


                                            #-----Porduct category-----#

@app.route('/addProductCategory', methods=['POST', 'GET'])
# @login_required
def addProductCategory():
    
    if request.method == 'POST':
        try: 
            with app.app_context():
                img = request.files.get('category_image_url')
                img_filename = secure_filename(request.files['category_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                prod_cat = ProductCategory(category_name_en=request.form['category_name_en'], 
                    category_name_ar=request.form['category_name_ar'],
                    category_image_url=upload_image.link,
                    category_desc_en=request.form['category_desc_en'],
                    category_desc_ar=request.form['category_desc_ar']  
                )
                db.session.add(prod_cat)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            return redirect(url_for('viewProductCategory'))
        except Exception as e:
            return jsonify({'return': 'error adding product category :- '+str(e)})
    return render_template('addProductCategory.html')


@app.route('/viewProductCategory', methods=['GET', 'POST'])
@login_required
def viewProductCategory():
    if request.method == 'GET':
        try:
            with app.app_context():
                prod_cat = ProductCategory.query.all()
                return render_template('viewProductCategory.html', prod_cat=prod_cat)
        except Exception as e:
            return jsonify({'return': 'error getting product category :- '+str(e)})
    return render_template('viewProductCategory.html')

@app.route('/editProductCategory/<id>', methods=['GET', 'POST'])
@login_required
def editProductCategory(id):
    prod_cat = ProductCategory.query.get_or_404(id)
    if request.method == 'POST':
        print(prod_cat)
        try:
            # with app.app_context():
            img = request.files.get('category_image_url')
            img_filename = secure_filename(request.files['category_image_url'].filename)
            basedir = os.path.abspath(os.path.dirname(__file__))

            # if img_filename == prod_cat.category_image_url:
            #     os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

             
            
            
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
            prod_cat.category_name_en=request.form['category_name_en']
            prod_cat.category_name_ar=request.form['category_name_ar']
            prod_cat.category_image_url=upload_image.link
            prod_cat.category_desc_en=request.form['category_desc_en']
            prod_cat.category_desc_ar=request.form['category_desc_ar'] 
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            return redirect(url_for('viewProductCategory'))
        except Exception as e:
            return jsonify({'return': 'error getting product category :- '+str(e)})
    return render_template('editProductCategory.html', prod_cat=prod_cat)

@app.route('/deleteProductCategory/<id>', methods=['GET', 'POST'])
@login_required
def deleteProductCategory(id):
    prod_cat = ProductCategory.query.get_or_404(id)
    try:
        
        db.session.delete(prod_cat)
        db.session.commit()

        return redirect(url_for('viewProductCategory'))
    except Exception as e:
        return jsonify({'return': 'error deleting product category :- '+str(e)})
    
                                             #-----Porduct category-----#



                                            #-----Porduct sub category-----#

@app.route('/addProductSubCategory/<id>', methods=['POST', 'GET'])
@login_required
def addProductSubCategory(id):   
    if request.method == 'POST':
        try: 
            with app.app_context():
                img = request.files.get('subcategory_image_url')
                img_filename = secure_filename(request.files['subcategory_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

                prod_subcat = ProductSubCategory(fk_prod_cat_id=id,
                    subcategory_name_en=request.form['subcategory_name_en'], 
                    subcategory_name_ar=request.form['subcategory_name_ar'],
                    subcategory_image_url=upload_image.link,
                    subcategory_desc_en=request.form['subcategory_desc_en'],
                    subcategory_desc_ar=request.form['subcategory_desc_ar']  
                )
                db.session.add(prod_subcat)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

            return redirect(url_for('viewProductSubCategory',id=id,name=request.form['subcategory_name_en']))
        except Exception as e:
            return jsonify({'return': 'error adding product sub category :- '+str(e)})
    return render_template('addProductSubCategory.html')
    

@app.route('/viewProductSubCategory/<id>/<name>', methods=['GET', 'POST'])
@login_required
def viewProductSubCategory(id,name):
    prod_subcat = ProductSubCategory.query.filter_by(fk_prod_cat_id=id).all()
    return render_template('viewProductSubCategory.html', prod_subcat=prod_subcat, name=name, id=id)
       
@app.route('/editProductSubCategory/<id>/<name>', methods=['GET', 'POST'])
@login_required
def editProductSubCategory(id,name):
    prod_subcat = ProductSubCategory.query.get_or_404(id)
    if request.method == 'POST':
        # print(prod_subcat)
        try:
            # with app.app_context():
            img = request.files.get('subcategory_image_url')
            img_filename = secure_filename(request.files['subcategory_image_url'].filename)
            basedir = os.path.abspath(os.path.dirname(__file__))

            # if img_filename == prod_subcat.subcategory_image_url:
            #     os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                

            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

            prod_subcat.subcategory_name_en=request.form['subcategory_name_en']
            prod_subcat.subcategory_name_ar=request.form['subcategory_name_ar']
            prod_subcat.subcategory_image_url=upload_image.link
            prod_subcat.subcategory_desc_en=request.form['subcategory_desc_en']
            prod_subcat.subcategory_desc_ar=request.form['subcategory_desc_ar']  
            
            
            
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            return redirect(url_for('viewProductSubCategory', id=prod_subcat.fk_prod_cat_id, name=name))
        except Exception as e:
            return jsonify({'return': 'error getting product sub category :- '+str(e)})
    return render_template('editProductSubCategory.html', prod_subcat=prod_subcat , name=name)

@app.route('/deleteProductSubCategory/<id>', methods=['GET', 'POST'])
@login_required
def deleteProductSubCategory(id):
    prod_subcat = ProductSubCategory.query.get_or_404(id)
    try:
        
        db.session.delete(prod_subcat)
        db.session.commit()

        return redirect(url_for('viewProductSubCategory',id=prod_subcat.fk_prod_cat_id,name=prod_subcat.subcategory_name_en))
    except Exception as e:
        return jsonify({'return': 'error deleting product sub category :- '+str(e)})

                                            #-----Porduct sub category-----#

@app.route('/addProductWithSubcat/<subcat_id>', methods=['POST', 'GET'])
@login_required
def addProductWithSubcat(subcat_id):
    category = ProductCategory.query.all()
    subcategory = ProductSubCategory.query.all()

    addSubcat = ProductSubCategory.query.get_or_404(subcat_id)
    addCat = ProductCategory.query.get_or_404(addSubcat.fk_prod_cat_id)

    def status(stat):
        if str(stat) == 'on':
            return "1"
        else:
            return "0"
        
        

    if request.method == 'POST':
      
            with app.app_context():
        
                prod = Products(
                    product_name_en=request.form['product_name_en'], 
                    product_name_ar=request.form['product_name_ar'],
                    product_desc_en=request.form['product_desc_en'],
                    product_desc_ar=request.form['product_desc_ar'],
                    unit_id=request.form['unit'],
                    unit_quantity=request.form['unit_quantity'],
                    product_code=request.form['product_code'],
                    produc_barcode=request.form['product_barcode'],
                    other_title_en=request.form['other_title_en'],
                    other_title_ar=request.form['other_title_ar'],
                    other_desc_en=request.form['other_desc_en'],
                    other_desc_ar=request.form['other_desc_ar'],
                    status=status(request.form.get('status')),
                    fast_delivery =status(request.form.get('fast_delivery')),
                    featured=status(request.form.get('featured')),
                    fresh=status(request.form.get('fresh')),
                    offer=status(request.form.get('offer')),
                    cat=addCat.id,
                    subcat=addSubcat.id
                )
                db.session.add(prod)
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                prod_stock = ProductStock(fk_product_id=prod.id,
                        product_price=request.form['product_price'],
                        product_offer_price=request.form['product_offer_price'],
                        product_purchase_price=request.form['product_purchase_price'],
                        opening_stock=request.form['opening_stock'],
                        min_stock=request.form['min_stock'],
                        max_stock=request.form['max_stock']
                )
                db.session.add(prod_stock)
                db.session.commit()


            return redirect(url_for('viewSubcatOnlyProducts', id=addSubcat.id))
        
    return render_template('addProductWithSubcat.html', 
                            category=category, 
                            subcategory=subcategory,
                            subcat_id=subcat_id, 
                            addCat=addCat,
                            addSubcat=addSubcat)

@app.route('/addProducts/execl/<subcat_id>', methods=['GET', 'POST'])
@login_required
def addProductsExecl(subcat_id):
    addSubcat = ProductSubCategory.query.get_or_404(subcat_id)
    addCat = ProductCategory.query.get_or_404(addSubcat.fk_prod_cat_id)
    ALLOWED_EXTENSIONS = {'xlsx'}
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def status(stat):
        if str(stat) == 'on' or str(stat) == '1' or stat == 1 :
            return "1"
        else:
            return "0"

    def product_status(stat):
        if str(stat) == 'on' or str(stat) == '1' or stat == 1 :
            return "enable"
        else:
            return "disable"
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return 'redirect(request.url)'
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return 'redirect(request.url)'
        if file and allowed_file(file.filename):
            print('file')
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            loc = (UPLOAD_FOLDER+f.filename)
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            print(sheet.nrows)
            for i in range(2, sheet.nrows):
                with app.app_context():
                    prod = Products(
                        product_name_en=sheet.cell_value(i, 0), 
                        product_name_ar=sheet.cell_value(i, 1),
                        product_desc_en=sheet.cell_value(i, 2),
                        product_desc_ar=sheet.cell_value(i, 3),
                        unit_id=sheet.cell_value(i, 4),
                        unit_quantity=sheet.cell_value(i, 5),
                        product_code=sheet.cell_value(i, 12),
                        produc_barcode=sheet.cell_value(i, 13),
                        other_title_en=sheet.cell_value(i, 14),
                        other_title_ar=sheet.cell_value(i, 15),
                        other_desc_en=sheet.cell_value(i, 16),
                        other_desc_ar=sheet.cell_value(i, 17),
                        status=product_status(sheet.cell_value(i, 18)),
                        fast_delivery =status(sheet.cell_value(i, 19)),
                        featured=status(sheet.cell_value(i, 20)),
                        fresh=status(sheet.cell_value(i, 21)),
                        offer=status(sheet.cell_value(i, 22)),
                        cat=addCat.id,
                        subcat=addSubcat.id
                    )
                    db.session.add(prod)
                    db.session.commit()
                    prod_stock = ProductStock(fk_product_id=prod.id,
                        product_price=sheet.cell_value(i,6),
                        product_offer_price=sheet.cell_value(i, 7),
                        product_purchase_price=sheet.cell_value(i, 8),
                        opening_stock=sheet.cell_value(i, 9),
                        min_stock=sheet.cell_value(i, 10),
                        max_stock=sheet.cell_value(i, 11)
                    )
                    db.session.add(prod_stock)
                    db.session.commit()
            return redirect(url_for('viewSubcatOnlyProducts', id=addSubcat.id))

    
    




@app.route('/addProduct', methods=['POST', 'GET'])
# @login_required
def addProduct():
    category = ProductCategory.query.all()
    subcategory = ProductSubCategory.query.all()

    # addSubcat = ProductSubCategory.query.get_or_404(subcat_id)
    # addCat = ProductCategory.query.get_or_404(addSubcat.fk_prod_cat_id)

    subcat= [[],[]]
    opt= {}
    with app.app_context():
        category = ProductCategory.query.all()
        for cat in category:
            for sub in cat.sub_cat:
                subcat[0].append(sub.subcategory_name_en)
                subcat[1].append(sub.id)
                opt[cat.id] = subcat
            subcat= [[],[]]
         
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
        

    if request.method == 'POST':
        try: 
            with app.app_context():
        
                prod = Products(
                    product_name_en=request.form['product_name_en'], 
                    product_name_ar=request.form['product_name_ar'],
                    product_desc_en=request.form['product_desc_en'],
                    product_desc_ar=request.form['product_desc_ar'],
                    unit_id=request.form['unit'],
                    unit_quantity=request.form['unit_quantity'],
                    product_code=request.form['product_code'],
                    produc_barcode=request.form['product_barcode'],
                    other_title_en=request.form['other_title_en'],
                    other_title_ar=request.form['other_title_ar'],
                    other_desc_en=request.form['other_desc_en'],
                    other_desc_ar=request.form['other_desc_ar'],
                    status=status(request.form.get('status')),
                    fast_delivery =status(request.form.get('fast_delivery')),
                    featured=status(request.form.get('featured')),
                    fresh=status(request.form.get('fresh')),
                    offer=status(request.form.get('offer')),
                    cat=request.form['category'],
                    subcat=request.form['subcategory']
                )
                db.session.add(prod)
                db.session.commit()
                prod_img = request.files.getlist('product_image_url')
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

                prod_stock = ProductStock(fk_product_id=prod.id,
                        product_price=request.form['product_price'],
                        product_offer_price=request.form['product_offer_price'],
                        product_purchase_price=request.form['product_purchase_price'],
                        opening_stock=request.form['opening_stock'],
                        min_stock=request.form['min_stock'],
                        max_stock=request.form['max_stock']
                )
                db.session.add(prod_stock)
                db.session.commit()


            return redirect(url_for('viewProduct'))
        except Exception as e:
            return jsonify({'return': 'error adding product :- '+str(e)})
    return render_template('addProduct.html', 
                            category=category, 
                            subcategory=subcategory,
                            otp=opt)
                            


@app.route('/deleteImage/<id>', methods=['GET', 'POST'])
@login_required
def deleteImage(id):
    prod_img = ProductImages.query.get_or_404(id)
    db.session.delete(prod_img)
    db.session.commit()
    return redirect(url_for('editProduct', id=prod_img.fk_product_id))





@app.route('/viewProduct', methods=['GET', 'POST'])
@login_required
def viewProduct():
    prod = Products.query.all()
    prod_img = ProductImages.query.all()
    prod_stock = ProductStock.query.all()
    return render_template('viewProduct.html', prod=prod, prod_img=prod_img,zip=zip, prod_stock=prod_stock)


@app.route('/editProduct/<id>', methods=['GET', 'POST'])
@login_required
def editProduct(id):
    prod = Products.query.get_or_404(id)
    subcat = ProductSubCategory.query.get_or_404(prod.subcat)
    prod_img = ProductImages.query.filter_by(fk_product_id=id).all()
    prod_stock = ProductStock.query.filter_by(fk_product_id=id).all()
    if request.method == 'POST':
        try:
            # with app.app_context():
            print('-------------------Debug Print-----------------')
            print(request.form['product_name_en'])
            print(request.form['product_name_ar'])
            print(request.form['product_desc_en'])
            print(request.form['product_desc_ar'])
            print(request.form['unit'])
            print(request.form['unit_quantity'])
            
            print('-------------------Debug Print-----------------')
            prod.product_name_en=request.form['product_name_en']
            prod.product_name_ar=request.form['product_name_ar']
            prod.product_desc_en=request.form['product_desc_en']
            prod.product_desc_er=request.form['product_desc_ar']
            prod.unit_id=request.form['unit']
            prod.unit_quantity=request.form['unit_quantity']
            db.session.commit()
            prod_img = request.files.getlist('product_image_url')
            if not prod_img or not any(f for f in prod_img):
                print('no image')
            else:
                for img in prod_img:
                    img_filename = secure_filename(img.filename)
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)

                    prod_img = ProductImages(fk_product_id=prod.id,
                        product_image_url=upload_image.link
                    )
                    db.session.add(prod_img)
                    db.session.commit()
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

            prod_stock[0].product_price=request.form['product_price']
            prod_stock[0].product_offer_price=request.form['product_offer_price']
            prod_stock[0].product_purchase_price=request.form['product_purchase_price']
            prod_stock[0].opening_stock=request.form['opening_stock']
            prod_stock[0].min_stock=request.form['min_stock']
            prod_stock[0].max_stock=request.form['max_stock']
            db.session.commit()
            return redirect(url_for('viewSubcatOnlyProducts', id=subcat.id))
        except Exception as e:
            return jsonify({'return': 'error getting product :- '+str(e)})
    return render_template('editProduct.html', prod=prod, prod_img=prod_img, prod_stock=prod_stock )



@app.route('/deleteProduct/<id>', methods=['GET', 'POST'])
@login_required
def deleteProduct(id):
    prod = Products.query.get_or_404(id)
    subcat = ProductSubCategory.query.get_or_404(prod.subcat)
    try:
        db.session.delete(prod)
        db.session.commit()
        return redirect(url_for('viewSubcatOnlyProducts', id=subcat.id))
    except Exception as e:
        return jsonify({'return': 'error deleting product :- '+str(e)})




@app.route('/viewSubcatOnlyProducts/<id>', methods=['GET', 'POST'])
@login_required
def viewSubcatOnlyProducts(id):
    prod = Products.query.filter_by(subcat=id).all()
    sub_cat = ProductSubCategory.query.get_or_404(id)
    prod_img = ProductImages.query.all()
    prod_stock = ProductStock.query.all()
    return render_template('viewSubcatOnlyProducts.html', prod=prod, prod_img=prod_img,zip=zip, prod_stock=prod_stock, sub_cat=sub_cat)


@app.route('/addBanner', methods=['GET', 'POST'])
@login_required
def addBanner():
    if request.method == 'POST':
        try:
            with app.app_context():
                img = request.files.get('banner_image_url')
                img_filename = secure_filename(request.files['banner_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                banner = BannerSection(banner_name_en=request.form['banner_name_en'],
                    banner_image_url=upload_image.link,
                    banner_desc_en=request.form['banner_desc_en'],
                    # status=request.form['status']
                )
                db.session.add(banner)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            return redirect(url_for('viewBanner'))
        except Exception as e:
            return jsonify({'return': 'error adding banner :- '+str(e)})
    return render_template('addBanner.html')

@app.route('/viewBanner', methods=['GET', 'POST'])
@login_required
def viewBanner():
    banner = BannerSection.query.all()
    return render_template('viewBanner.html', banner=banner)

@app.route('/editBanner/<id>', methods=['GET', 'POST'])
@login_required
def editBanner(id):
    banner = BannerSection.query.get_or_404(id)
    if request.method == 'POST':
        try:
            with app.app_context():
                img = request.files.get('banner_image_url')
                img_filename = secure_filename(request.files['banner_image_url'].filename)
                if img_filename != '':
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    banner.banner_image_url=upload_image.link
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                else:
                    pass
                banner.banner_name_en=request.form['banner_name_en']
                banner.banner_desc_en=request.form['banner_desc_en']
                # banner.status=request.form['status']
                db.session.commit()
                
            
            return redirect(url_for('viewBanner'))
        except Exception as e:
            return jsonify({'return': 'error getting banner :- '+str(e)})
    return render_template('editBanner.html', banner=banner)

@app.route('/deleteBanner/<id>', methods=['GET', 'POST'])
@login_required
def deleteBanner(id):
    banner = BannerSection.query.get_or_404(id)
    try:
        db.session.delete(banner)
        db.session.commit()
        return redirect(url_for('viewBanner'))
    except Exception as e:
        return jsonify({'return': 'error deleting banner :- '+str(e)})



@app.route('/termsandconditions')
def termsandconditions():
    return render_template('Terms-and-Conditions-for-Kenz-Food.html')

@app.route('/privacypolicy')
def privacypolicy():   
    return render_template('Privacy-Policy-for-Kenz-Food.html')



@app.route('/addSecondaryBanner', methods=['GET', 'POST'])
@login_required
def addSecondaryBanner():
    if request.method == 'POST':
        try:
            with app.app_context():
                img = request.files.get('banner_image_url')
                img_filename = secure_filename(request.files['banner_image_url'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                banner = SecondaryBanner(banner_name_en=request.form['banner_name_en'],
                    banner_image_url=upload_image.link,
                    banner_desc_en=request.form['banner_desc_en'],
                    # status=request.form['status']
                )
                db.session.add(banner)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            return redirect(url_for('viewSecondaryBanner'))
        except Exception as e:
            return jsonify({'return': 'error adding banner :- '+str(e)})
    return render_template('addSecondaryBanner.html')

@app.route('/viewSecondaryBanner', methods=['GET', 'POST'])
@login_required
def viewSecondaryBanner():
    banner = SecondaryBanner.query.all()
    return render_template('viewSecondaryBanner.html', banner=banner)

@app.route('/editSecondaryBanner/<id>', methods=['GET', 'POST'])
@login_required
def editSecondaryBanner(id):
    banner = SecondaryBanner.query.get_or_404(id)
    if request.method == 'POST':
        try:
            with app.app_context():
                img = request.files.get('banner_image_url')
                img_filename = secure_filename(request.files['banner_image_url'].filename)
                if img_filename != '':
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                    upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                    banner.banner_image_url=upload_image.link
                    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                else:
                    pass
                banner.banner_name_en=request.form['banner_name_en']
                banner.banner_desc_en=request.form['banner_desc_en']
                # banner.status=request.form['status']
                db.session.commit()
                
            
            return redirect(url_for('viewSecondaryBanner'))
        except Exception as e:
            return jsonify({'return': 'error getting banner :- '+str(e)})
    return render_template('editSecondaryBanner.html', banner=banner)

@app.route('/deleteSecondaryBanner/<id>', methods=['GET', 'POST'])
@login_required
def deleteSecondaryBanner(id):
    banner = SecondaryBanner.query.get_or_404(id)
    try:
        db.session.delete(banner)
        db.session.commit()
        return redirect(url_for('viewSecondaryBanner'))
    except Exception as e:
        return jsonify({'return': 'error deleting banner :- '+str(e)})


# @app.route('/notifications/add', methods=['GET', 'POST'])
# @login_required
# def addNotification():
#     notifications = Notifications.query.all()
#     if request.method == 'POST':
#         try:
#             with app.app_context():
#                 img = request.files.get('notification_image')
#                 img_filename = secure_filename(request.files['notification_image'].filename)
#                 basedir = os.path.abspath(os.path.dirname(__file__))
#                 img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
#                 upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
#                 notification = Notifications(title=request.form['title'],
#                     notification_image=upload_image.link,
#                     message=request.form['message'],
#                 )
#                 db.session.add(notification)
#                 db.session.commit()
#                 os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
#             return render_template('addNotifications.html', notifications=notifications)
#         except Exception as e:
#             return jsonify({'return': 'error adding notification :- '+str(e)})
#     return render_template('addNotifications.html', notifications=notifications)

# dev 2
@app.route('/notifications/add', methods=['GET', 'POST'])
@login_required
def addNotification():
    notifications = Notifications.query.all()
    print(notifications)
    products = db.session.query(Products.id, Products.product_name_en).all()
    print(products)
    if request.method == 'POST':
        try:
            with app.app_context():
                img = request.files.get('notification_image')
                img_filename = secure_filename(request.files['notification_image'].filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
                notification = Notifications(title=request.form['title'],
                    notification_image=upload_image.link,
                    message=request.form['message'],
                    fk_product_id=request.form['product_id']
                )
                db.session.add(notification)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            
            return render_template('addNotifications.html', notifications=notifications, products=products)
        except Exception as e:
            return jsonify({'return': 'error adding notification :- '+str(e)})
    return render_template('addNotifications.html', notifications=notifications, products=products)


@app.route('/notifications/delete', methods=['GET', 'POST'])
@login_required
def deleteNotification():
    notifications = Notifications.query.all()
    if request.method == 'POST':
        try:
            with app.app_context():
                notification = Notifications.query.get_or_404(request.form['id'])
                db.session.delete(notification)
                db.session.commit()
            
            return render_template('addNotifications.html', notifications=notifications)
        except Exception as e:
            return jsonify({'return': 'error deleting notification :- '+str(e)})
    return render_template('addNotifications.html', notifications=notifications)


# dev2

# @app.route('/countries', methods=['GET'])
# @token_required
# def get_countries():
#     with app.app_context():
#         countries = country.query.all()
#     country_list = []
#     for country in countries:
#         country_dict = {
#             'id': country.id,
#             'country_name': country.country_name,
#             'country_image_url': country.country_image_url,
#             'country_code': country.country_code
#         }
#         country_list.append(country_dict)
#     return jsonify(country_list)

@app.route('/countries', methods=['GET'])
def get_countries():
    if request.method == 'GET':
        try:
            countries = country.query.all()
            if countries:
                country_list = []
                for country_lists in countries:
                    country_json = {
                        'id': country_lists.id,
                        'country_name': country_lists.country_name,
                        'country_image_url': country_lists.country_image_url,
                        'country_code': country_lists.country_code,
                    }
                    country_list.append(country_json)
                return jsonify({'return': 'success', 'country': country_json})
            else:
                return jsonify({'return': 'no countries found'})
        except Exception as e:
            return jsonify({'return': 'error getting countries : '+ str(e)})
    return jsonify({'return': 'no GET request'})




    # dev2
# delivery charge

@app.route('/delivery_charges', methods=['GET', 'POST'])
def delivery_charge():
    if request.method == 'GET':
        zipcode = request.args.get('zipcode')
        delivery_charge = delivery_charges.query.filter_by(location_zipcode=zipcode).first()
        if delivery_charge:
            return jsonify({
                'zipcode': delivery_charge.location_zipcode,
                'normal_charge': delivery_charge.normal_charge,
                'fast_charge': delivery_charge.fast_charge
            }), 200
        else:
            return jsonify({'message': 'Delivery charges not found.'}), 404
    elif request.method == 'POST':
        data = request.get_json()
        delivery_charge = delivery_charges(
                                       location_name=data['location_name'],
                                       location_zipcode=data['location_zipcode'],
                                       normal_charge=data['normal_charge'],
                                       fast_charge=data['fast_charge'],
                                       active_status=data['active_status'])
        db.session.add(delivery_charge)
        db.session.commit()
        return jsonify({'message': 'Delivery charges added successfully.'}), 201




# coupon code 

@app.route('/apply_coupon', methods=['POST'])
def apply_coupon():
    data = request.get_json()
    coupon = Coupon.query.filter_by(coupon_code=data['coupon_code'], active_status=True).first()
    if coupon is None:
        return jsonify({'message': 'Invalid coupon code or coupon inactive.'}), 404

    # Calculate the new total price after applying the coupon
    original_price = data['price']
    reduction_amount = coupon.reduction_amount
    new_total_price = max(original_price - reduction_amount, 0)

    # Update the coupon quantity and save to the database
    coupon.quantity = max(coupon.quantity - 1, 0)
    db.session.commit()

    # Return the new total price
    return jsonify({'new_total_price': new_total_price}), 200




@app.route('/coupons', methods=['POST'])
def add_coupon():
    data = request.get_json()
    coupon = Coupon(
        coupon_name=data['coupon_name'],
        coupon_code=data['coupon_code'],
        reduction_amount=data['reduction_amount'],
        quantity=data['quantity'],
        active_status=data['active_status'],
        price_reduction=data['price_reduction']
    )
    db.session.add(coupon)
    db.session.commit()
    return jsonify({'message': 'Coupon added successfully.'}), 201
