from flask import Blueprint, render_template, request, session, redirect, url_for
from db_connection import cursor, conn
import decimal
from random import randint

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    cursor = conn.cursor()
    category = request.form.get('category')

    search = request.form.get('search-input')

    product_stock = []
    rows = []
    stock_lst = []

    if category:
        if category == "All":
            cursor.execute("SELECT * FROM Retail_Application.Product")
            rows = cursor.fetchall()

            cursor.execute("SELECT * FROM Retail_Application.Inventory")
            product_stock = cursor.fetchall()

        else:
            cursor.execute( "SELECT * FROM Retail_Application.Product WHERE category = %s", (category, ))
            rows = cursor.fetchall()

            cursor.execute("SELECT ID, Current_Stock FROM Retail_Application.Product INNER JOIN Retail_Application.Inventory ON InventoryID = ID AND category = %s", (category, ))
            product_stock = cursor.fetchall()
            
        
        for i in range(len(product_stock)):
            stock_lst.append(product_stock[i][1])
            print(stock_lst[i])

    elif search:
        search = '%' + search + '%'
        cursor.execute("SELECT DISTINCT ProductID, Name, Price, image_file_path, current_stock FROM Retail_application.Product INNER JOIN Retail_application.Inventory WHERE Product.InventoryID = Inventory.ID AND Name LIKE %s", (search, ))
        rows = cursor.fetchall()
        
        for prod in rows:
            product_stock.append(prod[4])
        
        for stock in product_stock:
            stock_lst.append(stock)
        
    return render_template("index.html", rows=rows, stock_lst=stock_lst, length=len(rows))


@views.route('/about')
def about():
    return render_template('about.html')

def update_cart(current_cart, item_to_add):
    return dict(list(current_cart.items()) + list(item_to_add.items()))


@views.route('/reviews', methods=["GET", "POST"])
def reviews():
    
    title = request.form.get("title")
    review = request.form.get("review")
    
    print(session['username'])
    if title and review and 'loggedin' in session.keys():
        cursor.execute("Insert into retail_application.reviews(ReviewerID, username, Title, Review) VALUES(%s, %s, %s, %s)", (session['UserID'], session['username'], title, review))
        conn.commit()
    
    cursor.execute("SELECT * FROM Retail_Application.Reviews")
    reviews = cursor.fetchall()
    print(reviews)
    
    return render_template('review.html', reviews= reviews)


@views.route('/cart', methods = ["POST", "GET"])
def cart():
    
    if 'loggedin' in session:
        
        pid = request.form.get('pid')
        qty = request.form.get('qty')     
        
        if pid and qty:
            
            
            cursor.execute("SELECT * FROM Retail_Application.Product WHERE ProductID = %s", (pid, ))
            product = cursor.fetchone()
                        
            temp = qty
            total_price = decimal.Decimal(temp) * product[2]
                        
            cart = {pid: {'name': product[1], 'price': product[2], 'category': product[4], 'image': 'static/' + product[3], 'qty': qty, 'subtotal': total_price, 'CartID': -1}}
            
            cursor.execute("SELECT Tokens from Retail_Application.Users WHERE UserID = %s", (session['UserID'], ))
            tokens = cursor.fetchone()
            session['tokens'] = list(tokens)
            print("Current tokens:" + str(session['tokens'][0]))
            
            
            if 'shopping_cart' in session:
                
                if pid not in session['shopping_cart']:
                    session['shopping_cart'] = update_cart(session['shopping_cart'], cart)
            else:
                session['shopping_cart'] = cart

            cursor.execute('INSERT INTO Retail_Application.ShoppingCart(Quantity, Amount_Due) VALUES (%s, %s)', (qty, session['shopping_cart'][pid]['subtotal']))
            conn.commit()
            
            cursor.execute("SELECT CartID FROM Retail_Application.ShoppingCart WHERE CartID = last_insert_id()")
            cart_id = list(cursor.fetchone())
            
            session['shopping_cart'][pid]['CartID'] = cart_id[0]
            
            cursor.execute('INSERT IGNORE Retail_Application.cart_consistsof_product(CID, PID) VALUES (%s, %s)', (cart_id[0], pid))
            conn.commit()
            
            total = decimal.Decimal('0')
            for value in session['shopping_cart'].values():
                
                total = (decimal.Decimal(value['subtotal']) + decimal.Decimal(total))
            
            session['cart_total'] = total
            
            get_Discount()    
        return render_template('cart.html')
    else:
        return redirect(url_for('auth.login'))

@views.route('/remove', methods=["GET", "POST"])
def delete_item():
    
    item_id = request.form.get('remove_itemID')    
    temp = session['shopping_cart']
    
    cursor.execute("SELECT Category FROM retail_application.Product INNER JOIN retail_application.user_shops_product ON user_shops_product.ProductID = Product.ProductID WHERE user_shops_product.UserID = %s GROUP BY category having Count(category) = ( SELECT MAX(most_frequent) as Most_Bought FROM ( SELECT COUNT(category) as most_frequent, Product.category as category FROM retail_application.user_shops_product INNER JOIN retail_application.Product ON product.ProductID = user_shops_product.ProductID WHERE user_shops_product.UserID = %s GROUP BY category)sub);", (1, 1))
    most_bought = cursor.fetchall()
    
    for max_bought in most_bought:
        if max_bought[0] == session['shopping_cart'][item_id]['category']:
            session['discount_notTaken'] = True
    
    
    cursor.execute("DELETE FROM retail_application.shoppingcart WHERE CartID = %s ", (session['shopping_cart'][item_id]['CartID'], ))
    conn.commit()
    
    
    temp.pop(item_id,None)    
    session['shopping_cart'] = temp
    
    total = decimal.Decimal('0')
    
    for value in session['shopping_cart'].values():
            total = (decimal.Decimal(value['subtotal']) + decimal.Decimal(total))
    
    session['cart_total'] = total
        
    return redirect(request.referrer)

@views.route('/tokens', methods=["GET", "POST"])
def apply_token():
    
    if 'loggedin' in session.keys() and request.method == "POST":
        
        tokens = int(request.form.get('token'))
        
        
        if tokens and request.method == "POST":
            original_tokens = session['tokens']
            updated_token_ct = original_tokens[0] - tokens
            
            cursor.execute("UPDATE retail_application.users SET tokens = %s WHERE UserID = %s", (updated_token_ct, session['UserID']))
            conn.commit()
            
            rewards = [ 
                    "5% Discount on active purchase", "10% Discount on active purchase", "15% Discount on active purchase", "Returned investment plus 3",
                    "25% Discount on active purchase", "50% Discount on active purchase", "30% Discount on acitve purchase", "Returned investment plus 5", 
                    "Dollar Off per token", "Free purchase", "Double the tokens", "Triple the tokens"
                    ]
            
            temp = rewards
            
            if tokens < 8:
                temp.remove("Free purchase")
                temp.remove("Double the tokens")
                temp.remove("Triple the tokens")
                temp.remove("Dollar Off per token")
                
                if tokens < 4:
                    temp.remove("30% Discount on acitve purchase")
                    temp.remove("50% Discount on active purchase")
            
            position_rewards = [""] * len(temp)
                
            i = 0
            while "" in position_rewards:

                idx = randint(0, len(temp) - 1)

                if position_rewards[idx] == "":
                    position_rewards[idx] = temp[i]
                    i += 1
                                                
            pick = randint(0, len(position_rewards) - 1)
            reward = position_rewards[pick]
            
            session['reward'] = reward
            
            if 'Discount' in reward:
                
                temp = session['cart_total']
                percentage = 0
                
                if '25% Discount on active purchase' == reward:
                    percentage = 0.25
                elif '10% Discount on active purchase' == reward:
                    percentage = 0.10
                elif '15% Discount on active purchase' == reward:
                    percentage = 0.15
                elif '5% Discount on active purchase' == reward:
                    percentage = 0.05
                elif '50% Discount on active purchase' == reward:
                    percentage = 0.50
                
                temp = decimal.Decimal(temp)
                percentage = decimal.Decimal(percentage)
                
                temp = temp - (temp * percentage)
                temp = temp.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)
                
                for value in session['shopping_cart'].values():
                    
                    amount_paid = decimal.Decimal(value['subtotal']) - (decimal.Decimal(value['subtotal']) * percentage)
                    amount_paid = amount_paid.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)
                    
                    value['subtotal'] = amount_paid

                    cursor.execute("UPDATE retail_application.ShoppingCart SET Amount_Due = %s WHERE CartID = %s", (value['subtotal'], value['CartID']))
                    conn.commit()
                            
                if temp > 0:
                    session['cart_total'] = temp
                else:
                    session['cart_total'] = decimal.Decimal('0.00')
            
            elif 'tokens' in reward:
                
                multiplier = 0
                
                if 'Double' in reward:
                    multiplier = 2
                elif 'Triple' in reward:
                    multiplier = 3
                
                updated_token_ct = (original_tokens[0] * multiplier)

            elif 'Returned' in reward:
                
                added_tokens = 0
                
                if '3' in reward:
                    added_tokens = 3
                elif '5' in reward:
                    added_tokens = 5
                
                updated_token_ct = (original_tokens[0] + added_tokens)

            elif "Dollar" in reward:
                temp1 = session['cart_total'] 
                temp1 = decimal.Decimal(temp1) - decimal.Decimal(tokens)
                
                price_per_item = tokens/len(session['shopping_cart'])
                
                for value in session['shopping_cart'].values():
                    
                    temp = decimal.Decimal(value['subtotal'])- decimal.Decimal(price_per_item) 
                    temp = temp.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)
                    value['subtotal'] = temp
                    
                    cursor.execute("UPDATE retail_application.shoppingcart SET Amount_Due = %s WHERE CartID =%s", (value['subtotal'], value['CartID']))
                    conn.commit()
                        
                if temp > 0:
                    session['cart_total'] = temp1 
                else:
                    session['cart_total'] = decimal.Decimal('0.00')
            
            else:
                session['cart_total'] = decimal.Decimal('0.00')

                for value in session['shopping_cart'].values():
                    value['subtotal'] = decimal.Decimal('0.00')
                    
                    cursor.execute("UPDATE retail_application.shoppingcart SET Amount_Due = %s WHERE CartID =%s", (value['subtotal'], value['CartID']))
                    conn.commit()
            
            session['tokens'][0] = updated_token_ct
            cursor.execute("UPDATE retail_application.users SET tokens = %s WHERE UserID = %s", (updated_token_ct, session['UserID']))        
            conn.commit()
        else:
            return redirect(url_for('views.home'))
        
    return redirect(request.referrer)
    

def get_Discount():
        
    if 'discount_notTaken' not in session:
        session['discount_notTaken'] = True
    
    if session['discount_notTaken']:
    
        cursor.execute("SELECT COUNT(*) FROM retail_application.transaction Where UserID = %s", (session['UserID'], ))
        num_of_transactions = cursor.fetchone()
        
        
        if num_of_transactions[0] >= 10:
            cursor.execute("SELECT SUM(Amount_Paid) FROM retail_application.transaction Where UserID = %s", (session['UserID'], ))
            overall_spending = cursor.fetchone()
            
            
            if overall_spending[0] > 1000:
                cursor.execute("SELECT Category FROM retail_application.Product INNER JOIN retail_application.user_shops_product ON user_shops_product.ProductID = Product.ProductID WHERE user_shops_product.UserID = %s GROUP BY category having Count(category) = ( SELECT MAX(most_frequent) as Most_Bought FROM ( SELECT COUNT(category) as most_frequent, Product.category as category FROM retail_application.user_shops_product INNER JOIN retail_application.Product ON product.ProductID = user_shops_product.ProductID WHERE user_shops_product.UserID = %s GROUP BY category)sub);", (1, 1))
                category = cursor.fetchall()

                cursor.execute("SELECT AVG(Price) FROM Retail_Application.Product INNER JOIN Retail_Application.user_shops_product ON Product.ProductID = user_shops_product.ProductID WHERE UserID = %s", (session['UserID'], ))                            
                average = list(cursor.fetchone())
                temp = 0
                for value in session['shopping_cart'].values():
                    
                    for ctg in category:                    
                            if value['category'] == ctg[0]:
                                
                                discount = decimal.Decimal(average[0]/num_of_transactions[0])
                                print(discount)
                                
                                if decimal.Decimal(value['subtotal']) > decimal.Decimal(average[0]):
                                
                                    value['subtotal'] = abs(decimal.Decimal(value['subtotal']) - discount)
                                    value['subtotal'] = value['subtotal'].quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)
                                    session['discount_notTaken'] = False
                                
                                break
                    temp = decimal.Decimal(temp) + decimal.Decimal(value['subtotal'])
                
                session['cart_total'] = temp
            
@views.route('/checkout', methods=["GET", "POST"])
def checkout():

    return render_template('checkout.html')


@views.route('/payment', methods=["GET", "POST"])
def payment():

    if 'loggedin' in session.keys() and 'shopping_cart' in session.keys() and len(session['shopping_cart']) > 0:
        
        name = request.form.get('Name')
        card_name = request.form.get('card_name')

        address = request.form.get('address')
        city = request.form.get('City')
        state = request.form.get('State')

        zip_code = request.form.get('Zip')
        email = request.form.get('email')
        cvv = request.form.get('cvv')

        credit_c = request.form.get('cc')
        exp_month = request.form.get('mon')
        exp_year = request.form.get('year')

        cursor.execute('INSERT INTO Retail_Application.Transaction(Full_Name, Email, Amount_Paid, Card_num, Name_on_card, ExpiryMonth, CVV, ExpiryYear, Address, City, State, ZipCode, UserID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, email, session['cart_total'], credit_c, card_name, exp_month, cvv, exp_year, address, city, state, zip_code, session['UserID']))
        
        cursor.execute("UPDATE Retail_Application.Users SET Tokens = Tokens + 1 WHERE UserID = %s", (session['UserID'], ))
        conn.commit()
        
        for item in session['shopping_cart']:
            
            cursor.execute('UPDATE Retail_Application.ShoppingCart SET TransactionID = last_insert_id() WHERE CartID = %s', (session['shopping_cart'][item]['CartID'], ))
            
            cursor.execute('INSERT IGNORE Retail_Application.User_shops_Product(ProductID, UserID) VALUES (%s, %s)', (item, session['UserID']))
            
            cursor.execute("UPDATE Retail_Application.Product INNER JOIN Retail_Application.Inventory SET Current_Stock = Current_Stock - %s WHERE ID = ProductID AND ProductID = %s", (session['shopping_cart'][item]['qty'], item))
            conn.commit()        
        
        session.pop('cart_total', None)
        session.pop('shopping_cart', None)
        session.pop('reward', None)
        session.pop('discount_notTaken', None)
        session.pop('tokens', None)
        
        return "Transaction Succesful!"
    elif 'loggedin' not in session.keys():
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('views.home'))
