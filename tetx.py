





import time
import random

counter = 9

def generate_order_id():
    global counter
    counter += 1
    return str(int(time.time())) + str(counter).zfill(3)

print(generate_order_id())  # Outputs something like "160580697212412"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"
print(generate_order_id())  # Outputs something like "160580697212413"

# # from app import app, Products, ProductCategory, ProductSubCategory

# # subcat= [[],[]]
# # opt= {}
# # with app.app_context():
# #     category = ProductCategory.query.all()
# #     for cat in category:
# #         # print(cat.category_name_en)
        
# #         for sub in cat.sub_cat:
# #             # print(sub.subcategory_name_en)
# #             subcat[0].append(sub.subcategory_name_en)
# #             subcat[1].append(sub.id)
# #             opt[cat.category_name_en] = subcat
        
# #         subcat= [[],[]]
         
          
        
        
        
        

# # print(opt)

# from app import app, Products, ProductCategory, ProductSubCategory

# subcat= []
# opt= {}
# with app.app_context():
#     category = ProductCategory.query.all()
#     for cat in category:
#         # print(cat.category_name_en)
        
#         for sub in cat.sub_cat:
#             # print(sub.subcategory_name_en)
#             subcat.append(sub.subcategory_name_en)
            
#             opt[cat.category_name_en] = subcat
        
#         subcat= []
         
          
        
        
        
# print(category[0].sub_cat[0].id)

# print(opt)