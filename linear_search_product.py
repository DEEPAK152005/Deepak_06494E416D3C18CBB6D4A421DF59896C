def linear_search_product(product_list, target_product):
    indices = []
    
    # Loop through the list of products
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    
    return indices
  