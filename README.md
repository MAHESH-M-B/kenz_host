<h1>Kenz-Food-APIs Documentaions</h1>

<b>(Token required)* </b>

1. [User Authentication](#user-authentication)
    - [Sign In User](#sign-in-user)
    - [Token Headers format*](#token-headers-format)
2. [User APIs](#user-apis)
    - [Insert User](#insert-user)
    - [Get Users](#get-users)
    - [Get Current User Details*](#get-current-user-details)
    - [Add User Address*](#add-user-address)
    - [Get All User Address](#get-all-user-address)
    - [Get User Address with id](#get-user-address-with-id)
    - [Get User Address with id](#get-user-address-with-id)
    - [Update User Address*](#update-user-address)
    - [Update user Password](#update-user-password)
    - [Update Current user Profile*](#update-current-user-profile)
    - [Verify user](#verify-user)
    - [Check user Verification](#check-user-verification)
    - [Deactivate current User*](#deactivate-current-user)

3. [Banner API](#banner-api)
    - [Get all Banners](#get-all-banners)
    - [Get all Secondary Banner](#get-all-secondary-banner)
    - [Get all Notifications](#get-all-notifications)

4. [Category APIs](#category-apis)
    - [Get all Categories](#get-all-categories)
    - [Get SubCategory by ID](#get-subcategory-by-id)

5. [Product APIs](#product-apis)
    - [Get all Products by search](#get-all-products-by-search)
    - [Get Fast delivery Products](#get-fast-delivery-products)
    - [Get Normal delivery Products](#get-normal-delivery-products)
    - [Get Product images by ID](#get-product-images-by-id)
    - [Get Product Stock data by ID](#get-product-stock-data-by-id)
    - [Get Products](#get-products)
    - [Add Products](#add-products)
    - [Product Status](#product-status)

6. [Cart APIs](#cart-apis)
    - [Add Product to cart*](#add-product-to-cart)
    - [Get all items in Cart*](#get-all-items-in-cart)
    - [Delete Cart item*](#delete-cart-item)
    - [Clear cart*](#clear-cart)
    - [Increment Cart item](#increment-cart-item)
    - [Decrement Cart item*](#decrement-cart-item)

6. [Wishlist APIs*](#wishlist-apis)
    - [Add to Wishlist*](#add-to-wishlist)
    - [Get all Wishlist items*](#get-all-wishlist-items)
    - [Delete Wishlist item*](#delete-wishlist-item)
    - [Clear wishlist*](#clear-wishlist)
    - [Check for an item in Wishlist*](#check-for-an-item-in-wishlist)

7. [Order APIs*](#order-apis)
    - [Place Order*](#place-order)
    - [Get all Orders*](#get-all-orders)
    - [Get specific Order*](#get-specific-order)
    - [Get all Order items*](#get-all-order-items)
    - [Cancel Order*](#cancel-order)

<h2>User Authentication</h2>

<h3>Sign In User</h3>
<ul>
    <p>Sign in a user by passing email and password</p>
    <p>URL: /sign_in</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>

        Example Input body:
        {
            "email" : "admin@test.com",
            "password" : "test123"
        }

        Example Response body:
        {
            "is_verified": False,
            "phone": "1234567890",
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiIzZmU3ZDlkOC1jZTlhLTRhNmQtOTIwZS0xYjA1ZGIwOTU3ZjMifQ.wMpnikIZzeCcV0sKcZ2LGkmnAoMpsmOKklYa8qV4110",
            "user_id": 1
        }
</ul>

<h3>Token Headers format</h3>
<p>Headers : </p>

    var headers = {
        'x-access-token': '[token]'
        };

<h2>User APIs</h2>

<h3>Insert User</h3>
<ul>
    <p>Insert a new user into the database</p>
    <p>URL: /insert_users</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>

        Example Input body:
        {
            "ip_address" : "0.0.0.0", 
            "user_type" : "admin",
            "username" : "admin",
            "firstname" : "adminf",
            "lastname" : "adminl",
            "password" : "admin123",
            "email" : "admin@admin.com",
            "phone" :  "1234567890"
        }

        Example Response body:
        {
            "created_at": "2023-01-18 09:56:42.669695",
            "email": "admin@admin.com",
            "firstname": "adminf",
            "lastname": "adminl",
            "phone": "1234567890",
            "public_id": "69e853bf-8cb0-4845-8937-37aadd574d71",
            "return": "user added successfully",
            "user_id": 1,
            "user_type": "admin",
            "username": "admin"
        }

</ul>

<h3>Get Users</h3>
<ul>
    <p>Get user data from database</p>
    <p>URL: /get_users/{parm}</p>
    <p>Method: GET</p>

<p>Pram list:-</p>

    • /username
    • /email
    • /phone

<p>Example:-</p>
<p>https://kenz-food-api.herokuapp.com/get_users/username?username=admin</p>

    Response Body: JSON Object
    Example:
    {
        "active_user": null,
        "created_at": null,
        "email": "admin@admin.com",
        "fcm_id": null,
        "firstname": "adminf",
        "ip_address": "10.1.11.233",
        "last_login": null,
        "lastname": "adminl",
        "latitude": null,
        "longitude": null,
        "password": "sha256$zPVbqIAsXT7soQq9$103a327c03c45e6a4755c3c94d225be702d49cb5426d0be3bfc2dc2fe45d259b",
        "phone": "1234567890",
        "profile_url": null,
        "publci_id": "ae6b0ef5-fcce-4148-b03c-7a836803ef8f",
        "return": "success",
        "user": "admin",
        "user_type": "admin",
        "verified_user": false
    }

</ul>

<h3>Get Current User Details</h3>
<ul>
    <p>Get current user details from database</p>
    <p>URL: /get_user/current</p>
    <p>Method: GET</p>
    <p>Headers: x-access-token</p>
    <p>https://kenz-food-api.herokuapp.com/get_user/current</p>

        Example Response body:
        {
            "active_user": null,
            "created_at": null,
            "email": "admin@admin.com",
            "fcm_id": null,
            "firstname": "adminf",
            "ip_address": "10.1.11.233",
            "last_login": null,
            "lastname": "adminl",
            "latitude": null,
            "longitude": null,
            "password": "sha256$zPVbqIAsXT7soQq9$103a327c03c45e6a4755c3c94d225be702d49cb5426d0be3bfc2dc2fe45d259b",
            "phone": "1234567890",
            "profile_url": null,
            "publci_id": "ae6b0ef5-fcce-4148-b03c-7a836803ef8f",
            "return": "success",
            "user": "admin",
            "user_type": "admin",
            "verified_user": false
        }

</ul>

<h3>Add User Address</h3>
<ul>
    <p>Add a new address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr</p>

        Example Input body:
        {
            'address_line1': "address_line1",
            'address_line2': "address_line2",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile': "1234567890",
            'latitude': '10.995003718149182', 
            'longitude': '76.99166976233744'
        }
</ul>

<h3>Get All User Address</h3>
<ul>
    <p>Get all address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr</p>

        Example Response body:
        {
            'id': 1,
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>Get User Address with id</h3>
<ul>
    <p>Get a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr/1</p>

        Example Response body:
        {
            'id': 1,
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>Update User Address</h3>
<ul>
    <p>Update a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_addr/1</p>

        Example Input body:
        {
            'address_line1': "address_line112",
            'address_line2': "address_line2223",
            'city': "cityxyz12",
            'postal_code': "123456213",
            'country': "countryxyz13",
            'telephone': "1234522890",
            'mobile': "1234567220",
            'latitude': '10.99500312312718149182', 
            'longitude': '76.99166976212333744'
        }

</ul>

<h3>Update user Password</h3>
<ul>
    <p>Update a password for a user</p>
    <p>URL: /update_password/{id}</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/update_password/1</p>

        Example Input body:
        {   
            "new_password": "admin123"
        }
        Example Response body:
        {
            "created_at": "2023-01-18 09:56:42.669695",
            "email": "admin@admin.com",
            "firstname": "adminf",
            "lastname": "adminl",
            "phone": "1234567890",
            "public_id": "69e853bf-8cb0-4845-8937-37aadd574d71",
            "return": "user added successfully",
            "user_id": 1,
            "user_type": "admin",
            "username": "admin"
        }

</ul>

<h3>Update Current user Profile</h3>
<ul>
    <p>Update a profile for a user</p>
    <p>URL: /update_user</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: multipart/form-data</p>
    <p>Example : https://kenz-food-api.herokuapp.com/update_user</p>

        Example Input Keys(All are required): 
        ['firstname'] ('String')
        ['lastname'] ('String')
        ['email'] ('String')
        ['phone'] ('String')
        ['user_image'] ('File')

</ul>

<h3>Verify user</h3>
<ul>
    <p>Verify a user</p>
    <p>URL: /verify/{id}</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/verify/1</p>

        Example Input body:
        {
            'verified_user': True
        }

</ul>

<h3>Check user Verification</h3>
<ul>
    <p>Check a verification for a user</p>
    <p>URL: /verify/{id}</p>
    <p>Method: GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/verify/1</p>

        Example Response body:
        {
            "return": "success",
            "user_verification_status": False
        }

</ul>

<h3>Deactivate current User</h3>
<ul>
    <p>Deactivate a user</p>
    <p>URL: /user_deactivate</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://kenz-food-api.herokuapp.com/user_deactivate</p>

       Example Input body:
        {
            'password': "admin123"
        }

        Example Response body:
        {
            'return': "success User Deactivated"
        }

</ul>

<h2>Banner API</h2>

<h3>Get all Banners</h3>
<ul>
    <p>Get all data from banner table</p>
    <p>URL: /banner</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/banner</p>

    Response Body: JSON Object
    Example:
    {
        "data": [
            {
                "banner_desc_en": "qweqwe",
                "banner_image_url": "https://i.imgur.com/vy00tog.jpg",
                "banner_name_en": "Test ",
                "id": 1,
                "status": null
            }
        ],
        "message": "banner fetched",
        "return": "success"
    }
</ul>

<h3>Get all Secondary Banner</h3>
<ul>
    <p>Get all data from secondary banner table</p>
    <p>URL: /secondary_banner</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/secondary_banner</p>

    Response Body: JSON Object
    Example:
    {
        "data": [
            {
                "banner_desc_en": "qweqwe",
                "banner_image_url": "https://i.imgur.com/vy00tog.jpg",
                "banner_name_en": "Test ",
                "id": 1,
                "status": null
            }
        ],
        "message": "banner fetched",
        "return": "success"
    }
</ul>

<h3>Get all Notifications</h3>
<ul>
    <p>Get all data from notification table</p>
    <p>URL: /notifications</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/notifications</p>

    Response Body: JSON Object
    Example:
    {
        "data": [
            {
                "id": 1,
                "image_url": "https://i.imgur.com/mtzqSXZ.png",
                "message": "qwe",
                "title": "qwe"
            },
            {
                "id": 2,
                "image_url": "https://i.imgur.com/hiNtk1w.png",
                "message": "qweqwe",
                "title": "wqe"
            }
        ],
        "message": "notifications fetched",
        "return": "success"
    }
</ul>

<h2>Category APIs</h2>

<h3>Get all Categories</h3>
<ul>
    <p>Get all data from category table</p>
    <p>URL: /get_categories</p>
    <p>Method : GET</p>
    <p>Example : https://kenz-food-api.herokuapp.com/get_categories</p>

    Response Body: JSON Object
    Example:
    {
        "categories": [
            {
                "active": null,
                "category_desc_ar": "هذا إدخال اختبار فرعي للقطط",
                "category_desc_en": "this is a test entery",
                "category_image_url": "FWA_LOGO.png",
                "category_name_ar": "إدخال الاختبار",
                "category_name_en": "test_xcat1",
                "category_order": null,
                "id": 1
            },
            {
                "active": null,
                "category_desc_ar": "إدخال اإدخال اإدخال اإدخال اإدخال اإدخال اإدخال ا",
                "category_desc_en": "this is about cat 2",
                "category_image_url": "hash-it-02.jpg",
                "category_name_ar": "إدخال اإدخال الاختبار",
                "category_name_en": "cat 2",
                "category_order": null,
                "id": 2
            },
            {
                "active": null,
                "category_desc_ar": "asd",
                "category_desc_en": "asd",
                "category_image_url": "TESLA_BLACK_AAA_shrink_10_transparent_-_kopie.png",
                "category_name_ar": "asd",
                "category_name_en": "test_xcat1",
                "category_order": null,
                "id": 3
            }
        ],
        "return": "success"
    }

</ul>

<h3>Get SubCategory by ID</h3>
<ul>
    <p>Get all subcatagories data  in a given category by ID</p>
    <p>URL: /get_subcategory</p>
    <p>Method : GET</p>
    <p>Example : http://192.168.100.83:5000/get_subcategory?category_id=1</p>

    Response Body: JSON Object
    Example:
    {
        "return": "success",
        "subcategories": [
            {
                "active": null,
                "id": 1,
                "subcategory_desc_ar": "هذا إدخال اختبار فرعي للقطط",
                "subcategory_desc_en": "this is a test sub cat entrty",
                "subcategory_image_url": "Group_84logo.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat1 edit",
                "subcategory_order": null
            },
            {
                "active": null,
                "id": 2,
                "subcategory_desc_ar": "دخول الاختباردخول الاختباردخول الاختبار",
                "subcategory_desc_en": "Thso os tets",
                "subcategory_image_url": "Group_85.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat2",
                "subcategory_order": null
            },
            {
                "active": null,
                "id": 3,
                "subcategory_desc_ar": "دخول الاختباردخول الاختباردخول الاختباردخول الاختبار",
                "subcategory_desc_en": "this is a test 3 entry",
                "subcategory_image_url": "HASH_IT_LOGO.png",
                "subcategory_name_ar": "دخول الاختبار",
                "subcategory_name_en": "test_Subcat3",
                "subcategory_order": null
            }
        ]
    }

</ul>

<h2>Product APIs</h2>

<h3>Get all Products by search</h3>
<ul>
    <p>Get all products data by search query</p>
    <p>URL: /products</p>
    <p>Method : GET</p>
    <p>PARAM : search </p>
    <p>Example : http://kenz-food-api.herokuapp.com/products?search=chi</p>

    Response Body: JSON Object
    Example:
    {
        "products": [
            {
                "cat_id": 2,
                "fast_delivery": null,
                "featured": null,
                "fresh": null,
                "id": 10,
                "offer": null,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 2,
                "product_code": null,
                "product_desc_ar": "asdasdasd",
                "product_desc_en": "chicken biriyani",
                "product_images": [
                    {
                        "id": 42,
                        "product_id": 10,
                        "product_image_url": "https://i.imgur.com/rFpmw8C.jpg"
                    }
                ],
                "product_name_ar": "asd",
                "product_name_en": "chicken biriyani",
                "product_stock": [
                    {
                        "id": 24,
                        "main_rack_no": null,
                        "max_stock": "",
                        "min_stock": "",
                        "opening_stock": "",
                        "product_id": 10,
                        "product_offer_price": "asd",
                        "product_price": "dasd",
                        "product_purchase_price": "asd",
                        "sub_rack_no": null
                    }
                ],
                "product_subcat_id": 2,
                "status": null,
                "subcat_id": 2,
                "unit_quantity": "dasdasd"
            }
        ],
        "return": "success" }
</ul>

<h3>Get Fast delivery Products</h3>
<ul>
    <p>Get all products data by search query</p>
    <p>URL: /get_products/fast_delivery</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_products/fast_delivery</p>

    Response Body: JSON Object
    Example:
    {
        "products": [
            {
                "cat_id": 1,
                "fast_delivery": "1",
                "featured": "0",
                "fresh": "0",
                "id": 2,
                "offer": "0",
                "other_title_ar": "123",
                "other_title_en": "894",
                "product_barcode": "84",
                "product_cat_id": 1,
                "product_code": "9849",
                "product_desc_ar": "498",
                "product_desc_en": "498",
                "product_images": [
                    {
                        "id": 3,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/mgO1fLo.png"
                    }
                ],
                "product_name_ar": "498",
                "product_name_en": "48",
                "product_stock": [
                    {
                        "id": 2,
                        "main_rack_no": null,
                        "max_stock": "9494",
                        "min_stock": "94",
                        "opening_stock": "984",
                        "product_id": 2,
                        "product_offer_price": "9849",
                        "product_price": "984",
                        "product_purchase_price": "84",
                        "sub_rack_no": null
                    }
                ],
                "product_subcat_id": 1,
                "status": "enable",
                "subcat_id": 1,
                "unit_quantity": "49"
            }
        ],
        "return": "success"
    }
</ul>

<h3>Get Normal delivery Products</h3>
<ul>
    <p>Get all products data by search query</p>
    <p>URL: /get_products/normal_delivery</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_products/normal_delivery</p>

    Response Body: JSON Object
    Example:
    
    "products": [
        {
            "cat_id": 1,
            "fast_delivery": "0",
            "featured": "0",
            "fresh": "0",
            "id": 1,
            "offer": "0",
            "other_title_ar": "15",
            "other_title_en": "5",
            "product_barcode": "51",
            "product_cat_id": 1,
            "product_code": "51",
            "product_desc_ar": "qweqw",
            "product_desc_en": "eqwe",
            "product_images": [
                {
                    "id": 1,
                    "product_id": 1,
                    "product_image_url": "https://i.imgur.com/uwWaWvs.jpg"
                },
                {
                    "id": 2,
                    "product_id": 1,
                    "product_image_url": "https://i.imgur.com/noaIyZa.png"
                }
            ],
            "product_name_ar": "weqwe",
            "product_name_en": "qwe12",
            "product_stock": [
                {
                    "id": 1,
                    "main_rack_no": null,
                    "max_stock": "1",
                    "min_stock": "15",
                    "opening_stock": "55",
                    "product_id": 1,
                    "product_offer_price": "234",
                    "product_price": "234",
                    "product_purchase_price": "234",
                    "sub_rack_no": null
                }
            ],
            "product_subcat_id": 1,
            "status": "enable",
            "subcat_id": 1,
            "unit_quantity": "123"
        },
        {
            "cat_id": 1,
            "fast_delivery": "0",
            "featured": "0",
            "fresh": "0",
            "id": 3,
            "offer": "0",
            "other_title_ar": "51",
            "other_title_en": "516",
            "product_barcode": "516",
            "product_cat_id": 1,
            "product_code": "516",
            "product_desc_ar": "165",
            "product_desc_en": "165",
            "product_images": [
                {
                    "id": 4,
                    "product_id": 3,
                    "product_image_url": "https://i.imgur.com/dcXAIvA.png"
                }
            ],
            "product_name_ar": "5",
            "product_name_en": "chicken Biryani",
            "product_stock": [
                {
                    "id": 3,
                    "main_rack_no": null,
                    "max_stock": "6516",
                    "min_stock": "651",
                    "opening_stock": "51",
                    "product_id": 3,
                    "product_offer_price": "16",
                    "product_price": "6515",
                    "product_purchase_price": "516",
                    "sub_rack_no": null
                }
            ],
            "product_subcat_id": 1,
            "status": "enable",
            "subcat_id": 1,
            "unit_quantity": "165"
        }
    ],
    "return": "success"
}
</ul>

<h3>Get Product images by ID</h3>
<ul>
    <p>Get All images of a product query by Product ID</p>
    <p>URL: /get_product_images</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_products_images?product_id=3</p>

    Response Body: JSON Object
    Example:
    {
        "product_images": [<image_URL1>, <image_URL2>, <image_URL3>],
        "return": "success"
    }
</ul>

<h3>Get Product Stock data by ID</h3>
<ul>
    <p>Get all product stocks query by product ID</p>
    <p>URL: /get_product_stocks</p>
    <p>Method : GET</p>
    <p>Example : http://kenz-food-api.herokuapp.com/get_product_stocks?product_id=1</p>

    Response Body: JSON Object
    Example:
    {
        "product_stocks": [<stock_URL_10>, <stock_URL_20>, <stock_URL_30>],
        "return": "success"
    }
</ul>

<h3>Get Products</h3>
<ul>
    <p>Get all Products based on parm input</p>
    <p>URL: /get_products</p>
    <p>Method : GET</p>
    <p>Parameters : parm, id</p>
    <ol>
        <li>parm = {product_id, category_id, subcategory_id, all}</li>
        <li>id = {id}</li>
        <p><b>*(parm=all) requires no id</b></p>
    </ol>
    <p>Example : http://kenz-food-api.herokuapp.com/get_product?parm=category_id&id=1</p>

    Response Body: JSON Object
    Example:
    {
    "products": [
        {
            "cat_id": 2,
            "fast_delivery": null,
            "featured": null,
            "fresh": null,
            "id": 10,
            "offer": null,
            "other_title_ar": null,
            "other_title_en": null,
            "product_barcode": null,
            "product_cat_id": 2,
            "product_code": null,
            "product_desc_ar": "asdasdasd",
            "product_desc_en": "asdasd",
            "product_images": [
                {
                    "id": 42,
                    "product_id": 10,
                    "product_image_url": "https://i.imgur.com/rFpmw8C.jpg"
                }
            ],
            "product_name_ar": "asd",
            "product_name_en": "Test image url 1",
            "product_stock": [
                {
                    "id": 24,
                    "main_rack_no": null,
                    "max_stock": "",
                    "min_stock": "",
                    "opening_stock": "",
                    "product_id": 10,
                    "product_offer_price": "asd",
                    "product_price": "dasd",
                    "product_purchase_price": "asd",
                    "sub_rack_no": null
                }
            ],
            "product_subcat_id": 2,
            "status": null,
            "subcat_id": 2,
            "unit_quantity": "dasdasd"
        }
    ],
    "return": "success" }

</ul>

<h3>Add Products</h3>
<ul>
    <p>Add Products to a subcatagory</p>
    <p>URL: \addProduct</p>
    <p>Method : POST</p>
    <p>Parameters : product_name_en, product_name_ar, product_desc_en, product_desc_ar, product_image_url, subcategory_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/addProduct</p>

    Request Body: JSON Object
    Example:
    {
        "product_name_en": "test_Subcat1 edit",
        "product_name_ar": "دخول الاختبار",
        "product_desc_en": "this is a test sub cat entrty",
        "product_desc_ar": "هذا إدخال اختبار فرعي للقطط",
        "product_image_url": "Group_84logo.png",
        "subcategory_id": 1
        ,.......{more left for disccusion}
    }

</ul>

<h3>Product Status</h3>
<ul>
    <p>Change and Check Product Status</p>
    <p>URL: /changeProductStatus/{status}</p>
    <p>Method : GET</p>
    <p>Parameters : product_id, status</p>
    <p>{status} = enable,diable,check</p>
    <p>Example : http://kenz-food-api.herokuapp.com/enable?id=8</p>

    Request Body: JSON Object
    Example:
    {
        "message": "product status changed",
        "return": "success"
    }

    Example : http://kenz-food-api.herokuapp.com/check?id=8

    {
        "return": "success",
        "status": "enable"
    }

</ul>

<h2>Cart APIs</h2>

<h3>Add Product to cart</h3>
<ul>
    <p>Add Product to cart with product id</p>
    <p>URL: /cart/{product_id}</p>
    <p>Method : POST</p>
    <p>Parameters : product_id, quantity, user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/1</p>

    Request Body: JSON Object
    Example :
    {
        "quantity": "1"
    }

    Response Body: JSON Object
    Example (If product is already in cart):
    {
        "message": "product quantity updated",
        "return": "success"
    }

    Response Body: JSON Object
    Example:
    {
        "message": "product added to cart",
        "return": "success"
    }
</ul>

<h3>Get all items in Cart</h3>
<ul>
    <p>Get all items in cart</p>
    <p>URL: /cart</p>
    <p>Method : GET</p>
    <p>Parameters : user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart</p>

    Response Body: JSON Object
    Example Output:
    {
        "cart items": [
            {
                "cat_id": 1,
                "created_at": "Sun, 18 Dec 2022 02:18:43 GMT",
                "fast_delivery": null,
                "featured": null,
                "fresh": null,
                "id": 2,
                "modified_at": "Sun, 18 Dec 2022 02:18:43 GMT",
                "offer": null,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "veg briyani - 2veg briyaasdani - 2veg briyani - 2vesdbriyani - asda2veg briyani - 2",
                "product_desc_en": "veg briyandasdai - 2veg briyani - 2veg briyani - 2vegasda briyani - 2",
                "product_id": 2,
                "product_images": [
                    {
                        "id": 4,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/ECJ7Uws.jpg"
                    },
                    {
                        "id": 5,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/erT6QGZ.jpg"
                    },
                    {
                        "id": 6,
                        "product_id": 2,
                        "product_image_url": "https://i.imgur.com/SKdJx59.jpg"
                    }
                ],
                "product_name_ar": "veg briyani - 2",
                "product_name_en": "veg briyani - 2",
                "product_stock": {
                    "id": 2,
                    "main_rack_no": null,
                    "max_stock": "5435",
                    "min_stock": "5",
                    "opening_stock": "45",
                    "product_id": 2,
                    "product_offer_price": "345",
                    "product_price": "5345",
                    "product_purchase_price": "3453",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "quantity": "5",
                "status": "enable",
                "subcat_id": 1,
                "unit_quantity": "1234",
                "user_id": 1
            }
        ],
        "return": "success"
    }
</ul>

<h3>Delete Cart item</h3>
<ul>
    <p>Delete a specific item in the cart with product id</p>
    <p>URL: /cart/itemDelete/{product_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/itemDelete/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "cart item deleted",
        "return": "success"
    }
</ul>

<h3>Clear cart</h3>
<ul>
    <p>Clear all items in cart</p>
    <p>URL: /cart/clear</p>
    <p>Method : DELETE</p>
    <p>Parameters : user_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/clear</p>

    Response Body: JSON Object
    Example:
    {
        "message": "cart cleared",
        "return": "success"
    }
</ul>

<h3>Increment Cart item</h3>
<ul>
    <p>Increment a specific item in the cart with product id by 1 (+1)</p>
    <p>URL: /cart/incQty/{product_id}</p>
    <p>Method : PUT</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/incQty/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "quantity increased",
        "return": "success"
    }
</ul>

<h3>Decrement Cart item</h3>
<ul>
    <p>Decrement a specific item in the cart with product id by 1 (-1)</p>
    <p>URL: /cart/decQty/{product_id}</p>
    <p>Method : PUT</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/cart/decQty/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "quantity decreased",
        "return": "success"
    }
</ul>

<h2>Wishlist APIs</h2>

<h3>Add to Wishlist</h3>
<ul>
    <p>Add a product to wishlist</p>
    <p>URL: /wishlist/{product_id}</p>
    <p>Method : POST</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/1</p>

    Request Body: JSON Object
    Example :
    {
        "message": "product added to wishlist",
        "return": "success"
    }

    Response Body: JSON Object
    Example (If product is already in wishlist):
    {
        "message": "product already in wishlist",
        "return": "success"
    }
</ul>

<h3>Get all Wishlist items</h3>
<ul>
    <p>Get all items in wishlist</p>
    <p>URL: /wishlist</p>
    <p>Method : GET</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist</p>

    Response Body: JSON Object
    Example Output:
    {
        "data": [
            {
                "cat_id": 1,
                "created_at": "Sun, 18 Dec 2022 04:05:54 GMT",
                "fast_delivery": null,
                "featured": null,
                "fresh": null,
                "id": 1,
                "modified_at": "Sun, 18 Dec 2022 04:05:54 GMT",
                "offer": null,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "veg briyani 1veg briyani 1veg briyani 1veg briyani 1veg briyani 1veg briyani 1",
                "product_desc_en": "veg briyani 1veg briyani 1ac",
                "product_id": 1,
                "product_images": [
                    {
                        "id": 1,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/Ptusp9y.jpg"
                    },
                    {
                        "id": 2,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/q8PDpAp.jpg"
                    },
                    {
                        "id": 3,
                        "product_id": 1,
                        "product_image_url": "https://i.imgur.com/PRIIs60.jpg"
                    }
                ],
                "product_name_ar": "veg briyani 1",
                "product_name_en": "veg briyani 1",
                "product_stock": {
                    "id": 1,
                    "main_rack_no": null,
                    "max_stock": "3",
                    "min_stock": "12312",
                    "opening_stock": "123",
                    "product_id": 1,
                    "product_offer_price": "123",
                    "product_price": "123",
                    "product_purchase_price": "123",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "status": "enable",
                "subcat_id": 1,
                "unit_quantity": "2",
                "user_id": 1
            }
        ],
        "message": "wishlist fetched",
        "return": "success"
    }
</ul>

<h3>Delete Wishlist item</h3>
<ul>
    <p>Delete a specific item in the wishlist with product id</p>
    <p>URL: /wishlist/{product_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/2</p>

    Response Body: JSON Object
    Example:
    {
        "message": "product removed from wishlist",
        "return": "success"
    }
</ul>

<h3>Clear wishlist</h3>
<ul>
    <p>Clear all items in wishlist</p>
    <p>URL: /wishlist/clear</p>
    <p>Method : DELETE</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/clear</p>

    Response Body: JSON Object
    Example:
    {
        "message": "wishlist cleared",
        "return": "success"
    }
</ul>

<h3>Check for an item in Wishlist</h3>
<ul>
    <p>Check if a specific item is in the wishlist with product id</p>
    <p>URL: /wishlist/check/{product_id}</p>
    <p>Method : GET</p>
    <p>Parameters : product_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/wishlist/check/2</p>

    Response Body: JSON Object
    Example 1:
    {
        "message": "product in wishlist",
        "return": "True"
    }
    Example 2:
    {
        "message": "product not in wishlist",
        "return": "False"
    }
</ul>

<h2>Order APIs</h2>

<h3>Place Order</h3>
<ul>
    <p>Place an order, all items in cart will be deleted and moved to order</p>
    <p>URL: /order/{user_addr_id}</p>
    <p>Method : POST</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Example Input:
    {
        "transaction_id": "XYZ000000",
    }

    Response Body: JSON Object
    Example:
    {
        "message": "order placed",
        "return": "success"
    }
</ul>

<h3>Get all Orders</h3>
<ul>
    <p>Get all orders</p>
    <p>URL: /order</p>
    <p>Method : GET</p>
    <p>Parameters : </p>
    <p>Example : http://kenz-food-api.herokuapp.com/order</p>

    Response Body: JSON Object
    Example:
    {
        "orders": [
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 16:08:36 GMT",
                "id": 1,
                "modified_at": "Thu, 22 Dec 2022 16:08:36 GMT",
                "status": "cancelled",
                "total_price": "22500",
                "total_quantity": "3"
            },
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 16:09:51 GMT",
                "id": 2,
                "modified_at": "Thu, 22 Dec 2022 16:09:51 GMT",
                "status": "pending",
                "total_price": "35000",
                "total_quantity": "4"
            },
            {
                "address_id": 1,
                "created_at": "Thu, 22 Dec 2022 18:17:58 GMT",
                "id": 3,
                "modified_at": "Thu, 22 Dec 2022 18:17:58 GMT",
                "status": "pending",
                "total_price": "15000",
                "total_quantity": "2"
            }
        ],
        "return": "success"
    }
</ul>

<h3>Get specific Order</h3>
<ul>
    <p>Get a specific order with order id</p>
    <p>URL: /order/{order_id}</p>
    <p>Method : GET</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "data": {
            "id": 1,
            "order_date": "Sun, 18 Dec 2022 04:05:54 GMT",
            "order_no": "ORD-1",
            "order_status": "pending",
            "order_total": "123",
            "user_id": 1
        },
        "message": "order fetched",
        "return": "success"
    }
</ul>

<h3>Get all Order items</h3>
<ul>
    <p>Get all items in a specific order with order id</p>
    <p>URL: /order/details/{order_id}</p>
    <p>Method : GET</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/details/1</p>

    Response Body: JSON Object
    Example:
    {
        "order_details": [
            {
                "cat_id": 1,
                "fast_delivery": null,
                "featured": null,
                "fk_order_id": 2,
                "fk_product_id": 3,
                "address_id": 1,
                "item_quantity":"5";
                "fresh": null,
                "offer": null,
                "order_date": "Thu, 22 Dec 2022 16:09:51 GMT",
                "order_id": 11,
                "other_title_ar": null,
                "other_title_en": null,
                "product_barcode": null,
                "product_cat_id": 1,
                "product_code": null,
                "product_desc_ar": "849",
                "product_desc_en": "9849",
                "product_id": 3,
                "product_images": [
                    {
                        "id": 7,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/fsKa5Xh.jpg"
                    },
                    {
                        "id": 8,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/PdnR6Qu.jpg"
                    },
                    {
                        "id": 9,
                        "product_id": 3,
                        "product_image_url": "https://i.imgur.com/Hh39YnI.jpg"
                    }
                ],
                "product_name_ar": "454984",
                "product_name_en": "p3",
                "product_stock": {
                    "id": 3,
                    "main_rack_no": null,
                    "max_stock": "4",
                    "min_stock": "498",
                    "opening_stock": "98",
                    "product_id": 3,
                    "product_offer_price": "984",
                    "product_price": "1500",
                    "product_purchase_price": "984",
                    "sub_rack_no": null
                },
                "product_subcat_id": 1,
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "84"
            },
            {
                "cat_id": 1,
                .
                .
                .
                .
                .
                .
                .
                .
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "123"
            },
            {
                "cat_id": 1,
                .
                .
                .
                .
                .
                .
                .
                .
                "status": null,
                "subcat_id": 1,
                "unit_quantity": "651"
            }
        ],
        "return": "success"
    }
</ul>

<h3>Cancel Order</h3>
<ul>
    <p>Cancel a specific order with order id</p>
    <p>URL: /order/{order_id}</p>
    <p>Method : DELETE</p>
    <p>Parameters : order_id</p>
    <p>Example : http://kenz-food-api.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "message": "order cancelled",
        "return": "success"
    }
</ul>

<h3>updated apis</h3>

<h3>basic url for test":https://epay-apis.herokuapp.com/</h3>
<h3>1.Get all Notifications</h3>
<ul>
    <p>Get all data from notification table</p>
    <p>URL: /notifications</p>
    <p>Method : GET</p>
    <p>Example : https://epay-apis.herokuapp.com/notifications</p>

    Response Body: JSON Object
    Example:
    {
        "data": [
            {
        "id": 1,
        "image_url": "https://i.imgur.com/85X0zxa.png",
        "message": "asdf",
        "product_id": 1,
        "title": "asfdasd"
            },
            {
        "id": 2,
        "image_url": "https://i.imgur.com/YfAn2me.png",
        "message": "asdf",
        "product_id": 2,
        "title": "asdfa"
            },
            {
        "id": 3,
        "image_url": "https://i.imgur.com/TjVUNWs.png",
        "message": "asdf",
        "product_id": 2,
        "title": "asdfa"
            }
        ],
        "message": "notifications fetched",
        "return": "success"
    }
</ul>

<h3>2.Get Products</h3>
<ul>
    <p>Get all Products based on parm input</p>
    <p>URL: /get_products</p>
    <p>Method : GET</p>
    <p>Parameters : parm, id</p>
    <ol>
        <li>parm = {product_id, category_id, subcategory_id,delivery_type}</li>
    </ol>
    <p>Example : https://epay-apis.herokuapp.com/get_products?category_id=1&subcategory_id=1&delivery_type=fast</p>

    Response Body: JSON Object
    Example:
    {
        "products": [
            {
                "cat_id": 1,
                "fast_delivery": "1",
                "featured": "0",
                "fresh": "0",
                "id": 1,
                "offer": "0",
                "other_title_ar": "asd",
                "other_title_en": "SDF",
                "product_barcode": "655",
                "product_cat_id": 1,
                "product_code": "88",
                "product_desc_ar": "testproduct1",
                "product_desc_en": "testproduct1",
                "product_images": [
            {
          "id": 1,
          "product_id": 1,
          "product_image_url": "https://i.imgur.com/XeTgdWH.png"
            }
            ],
            "product_name_ar": "testproduct1",
            "product_name_en": "testproduct1",
            "product_stock": [
             {
          "id": 1,
          "main_rack_no": null,
          "max_stock": "5",
          "min_stock": "5",
          "opening_stock": "68",
          "product_id": 1,
          "product_offer_price": "87",
          "product_price": "87",
          "product_purchase_price": "8754",
          "sub_rack_no": null
        }
      ],
      "product_subcat_id": 1,
      "status": "enable",
      "subcat_id": 1,
      "unit_quantity": "1"
            },
        {
         "cat_id": 1,
      "fast_delivery": "1",
      "featured": "0",
      "fresh": "0",
      "id": 2,
      "offer": "0",
      "other_title_ar": "1234",
      "other_title_en": "1234",
      "product_barcode": "124",
      "product_cat_id": 1,
      "product_code": "345",
      "product_desc_ar": "testproduct2",
      "product_desc_en": "testproduct2",
      "product_images": [
        {
          "id": 2,
          "product_id": 2,
          "product_image_url": "https://i.imgur.com/sthURYQ.png"
        }
      ],
      "product_name_ar": "testproduct2",
      "product_name_en": "testproduct2",
      "product_stock": [
        {
          "id": 2,
          "main_rack_no": null,
          "max_stock": "234",
          "min_stock": "23",
          "opening_stock": "234",
          "product_id": 2,
          "product_offer_price": "65",
          "product_price": "54",
          "product_purchase_price": "234",
          "sub_rack_no": null
        }
      ],
      "product_subcat_id": 1,
      "status": "enable",
      "subcat_id": 1,
      "unit_quantity": "87"
        }
        ],
        "return": "success"
    }

</ul>

<h3>3.Delivery charge </h3>
<ul>
    <p>Post Delivery charge based on pincode</p>
    <p>URL: /delivery_charges</p>
    <p>Method : POST</p>
    <p>Example : https://epay-apis.herokuapp.com/delivery_charges</p>

    INPUT Body for post: JSON Object
    Example:
    {
        "location_name": "Example City",
        "location_zipcode": "12345",
        "normal_charge": 5.00,
        "fast_charge": 10.00,
        "active_status": true
    }

<p>4.Get Delivery charge based on pincode</p>
<p>Method : GET</p>
<p>Example : https://epay-apis.herokuapp.com/delivery_charges?zipcode=12345</p>
Respose body from get:JSON Object
Example:
{
  "fast_charge": 9.99,
  "normal_charge": 5.99,
  "zipcode": 12345
}

</ul>

<h3>5.apply coupon</h3>
<ul>
    <p>apply_coupon</p>
    <p>URL: /apply_coupon</p>
    <p>Method : POST</p>
    <p>Example : https://epay-apis.herokuapp.com/apply_coupon</p>

    INPUT Body for post: JSON Object
    Example:
    {
        "coupon_code": "EXAMPLECOUPON",
        "price": 50.00
    }

<h3>6.add coupon</h3>
<ul>
    <p>/coupons</p>
    <p>URL: /coupons</p>
    <p>Method : POST</p>
    <p>Example : https://epay-apis.herokuapp.com/coupons</p>

    INPUT Body for post: JSON Object
    Example:
    {
        "coupon_name": "10% off your first purchase",
        "coupon_code": "FIRST10",
        "reduction_amount": 10.00,
        "quantity": 50,
        "active_status": 1
    }

<h3>7.Add User Address</h3>
<ul>
    <p>Add a new address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: POST</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://epay-apis.herokuapp.com/user_addr</p>

        Example Input body:
        {
            'address_line1': "address_line1",
            'name': "name",
            'address_line2': "address_line2",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile': "1234567890",
            'latitude': '10.995003718149182', 
            'longitude': '76.99166976233744'
        }
</ul>

<h3>8.Get All User Address</h3>
<ul>
    <p>Get all address for a user</p>
    <p>URL: /user_addr</p>
    <p>Method: GET</p>
    <p>Example : https://epay-apis.herokuapp.com/user_addr</p>

        Example Response body:
        {
            'id': 1,
            'name':"samplename"
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>9.Get User Address with id</h3>
<ul>
    <p>Get a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: GET</p>
    <p>Example : https://epay-apis.herokuapp.com/user_addr/1</p>

        Example Response body:
        {
            'id': 1,
            'name':"samplename"
            'address_line1': "address_line123",
            'address_line2': "address_line123",
            'city': "cityxyz",
            'postal_code': "123456",
            'country': "countryxyz",
            'telephone': "1234567890",
            'mobile':   "1234567890",
            'latitude':  '10.995003718149182',
            'longitude': '76.99166976233744',
            'created_at':  '2021-08-03T09:00:00.000Z',
            'modified_at': '2021-08-03T09:00:00.000Z',
            'user_id': 1
        }
</ul>

<h3>10.Update User Address</h3>
<ul>
    <p>Update a address for a user</p>
    <p>URL: /user_addr/{id}</p>
    <p>Method: PUT</p>
    <p>URL Content-Type: JSON</p>
    <p>Example : https://epay-apis.herokuapp.com/user_addr/1</p>

        Example Input body:
        {
            'name':"samplename",
            'address_line1': "address_line112",
            'address_line2': "address_line2223",
            'city': "cityxyz12",
            'postal_code': "123456213",
            'country': "countryxyz13",
            'telephone': "1234522890",
            'mobile': "1234567220",
            'latitude': '10.99500312312718149182', 
            'longitude': '76.99166976212333744'
        }

</ul>

<h3>11.Place Order</h3>
<ul>
    <p>Place an order, all items in cart will be deleted and moved to order</p>
    <p>URL: /order/{user_addr_id}</p>
    <p>Method : POST</p>
    <p>Parameters : </p>
    <p>Example : https://epay-apis.herokuapp.com/order/1</p>

    Example Input:
    {
        "delivery_type": "door delivery",
        "delivery_time": "2023-04-10 10:00:00",
        "transaction_id": "1234abcd"
    }

    Response Body: JSON Object
    Example:
    {
        "message": "order placed",
        "return": "success"
    }
</ul>

<h3>12.Get specific Order</h3>
<ul>
    <p>Get a specific order with order id</p>
    <p>URL: /order/{order_id}</p>
    <p>Method : GET</p>
    <p>Parameters : order_id</p>
    <p>Example : https://epay-apis.herokuapp.com/order/1</p>

    Response Body: JSON Object
    Example:
    {
        "data": {
            "id": 1,
            "total_price":234234,
            "total_quantity":3,
            "address_id":1,
            "status":"pending"
            "created_at": "Sun, 18 Dec 2022 04:05:54 GMT",
            "modified_at": "Sun, 18 Dec 2022 04:05:54 GMT",
            "delivery_time": "Sun, 18 Dec 2022 04:05:54",
            "delivery_type": "door delivery",
        },
        "message": "order fetched",
        "return": "success"
    }
</ul>
