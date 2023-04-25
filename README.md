# AutomationExcercise

## 1. Goal of the project: 
automating tests for the website: https://automationexercise.com/
    
## 2. Test Scenarios:

  <details><summary>Test Case 1: Register New User</summary>

    1. Navigate to url 'http://automationexercise.com/login'
    2. Enter name and email address.
    3. Click 'Signup' button.
    4. Fill details: Title, Name, Email, Password, Date of birth.
    5. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number.
    6. Click 'Create Account button'
    7. Verify that 'ACCOUNT CREATED!' is visible.
    8. Continue to homepage.
    9. Verify that label "Logged in as [username]" is visible.
    10. Click "Delete Account". 
    11. Verify that 'ACCOUNT DELETED' is visible.
       
 </details>
  
 <details><summary>Test Case 2: Register User with existing email</summary>

    1. Navigate to url 'http://automationexercise.com/login'
    2. Enter name and already registered email address.
    3. Click 'Signup' button.
    4. Verify error 'Email Address already exist!' is visible.

 </details>

 <details><summary>Test Case 3: Login User with correct email and password</summary>

    1. Navigate to url 'http://automationexercise.com/login'.
    2. Enter correct email address and password.
    3. Click 'login' button.
    4. Verify that label 'Logged in as [username]' is visible.

 </details>

 <details><summary>Test Case 4: Login User with incorrect email and password</summary>

    1. Navigate to url 'http://automationexercise.com/login'.
    2. Enter incorrect email address and password.
    3. Click 'login' button.
    4. Verify error 'Your email or password is incorrect!' is visible.

 </details>

 <details><summary>Test Case 5: Log Out User</summary>

    1. Navigate to url 'http://automationexercise.com/login'.
    2. Enter correct email address and password.
    3. Click 'login' button.
    4. Verify that label 'Logged in as [username]' is visible.
    5. Click 'Logout' button.
    6. Verify that user is navigated to login page.

 </details>
 
 <details><summary>Test Case 6: Verify All Product Brands</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Verify that Brands are visible on left side bar.
    4. Click on any brand name.
    5. Verify that user is navigated to brand page and brand products are displayed.
    6. Check number of products in brackets next to brand name.
    7. Verify if this number corresponds to number of products available.
    8. Repeat this process for every brand.
       
 </details>

 <details><summary>Test Case 7: Verify Product Categories</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select random Category and then Subcategory.
    4. Click on chosen Subcategory name.
    5. Verify that user is navigated to category page and category products are displayed.
    6. Verify if name of a random product contains Category's name. 
       
 </details>

 <details><summary>Test Case 8: Verify Product Details</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select random Category and then Subcategory.
    4. Check the name and price of a product.
    5. Click 'View product' button.
    6. Verify that product's name, price and subcategory match with details from Products page. 
       
 </details>

 <details><summary>Test Case 9: Send Review Form</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select random Category and then Subcategory.
    4. Click 'View product' button.
    5. Fill details: randomised name, correct email and randomised message.
    6. click 'Submit' button.
    7. Verify that 'Thank you for your review.' message is vivible.
       
 </details>

 <details><summary>Test Case 10: Add Products To Cart</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select the searchbox and enter a phrase 'jeans'.
    4. Hover over product, check it's name and price and click 'Add to cart'.
    5. Click 'Continue Shopping' button.
    6. Clear the searchbox and enter a phrase 'unicorn'.
    7. Hover over product, check it's name and price and click 'Add to cart'.
    8. Click 'View Cart' button.
    9. Verify that both products are added to Cart.
    10. Verify that name and proce of both products match with details from Products page.
    
 </details>

 <details><summary>Test Case 11: Check Positive Quantity of Products in Cart</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select random Category and then Subcategory.
    4. Click 'View product' button and check produt's price.
    5. Enter number '3' into Quantity box and click Add to Cart.
    6. Click 'Continue Shopping' button.
    7. Enter number '4' into Quantity box and click Add to Cart.
    8. Click 'View Cart' button.
    9. Verify that quantity of the product in cart is sum of two numbers entered before.
    10. Verify that total price is the result of multiplication of the product's price by the quantity.
    
 </details>
 
 <details><summary>Test Case 12: Check Negative Quantity of Products in Cart</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select random Category and then Subcategory.
    4. Click 'View product' button.
    5. Enter number '-3' into Quantity box and click Add to Cart.
    6. Click 'View Cart' button.
    7. Verify that there are no products in cart.
    
 </details>
 
 <details><summary>Test Case 13: Remove Products from Cart</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Products' button.
    3. Select the searchbox and enter a phrase 'winter'.
    4. Hover over product and click 'Add to cart'.
    5. Click 'Continue Shopping' button.
    6. Clear the searchbox and enter a phrase 'summer'.
    7. Hover over product and click 'Add to cart'.
    8. Click 'View Cart' button.
    9. Click 'X' button corresponding to particular product.
    10. Verify that the product is removed and that there is only one product left in the cart.
    11. Click 'X' button corresponding to last product.
    12. Verify that "Cart is empty!" message is visible.

 </details>

 <details><summary>Test Case 14: Send ContactUs Form</summary>

    1. Navigate to url 'https://automationexercise.com'.
    2. Click on 'Contact us' button.
    3. Verify 'GET IN TOUCH' is visible.
    4. Enter name, email, subject and message.
    5. Upload file.
    6. Click 'Submit' button.
    7. Click OK button.
    8. Verify success message 'Success! Your details have been submitted successfully.' is visible. 

 </details>
 
## 3. Technology Stack:
  
  - Selenium - open-source tool that automates web browsers
  - Python - programming language used in this repository to write automated tests
  - unittest - Python framework supporting test automation

## 4. Directories descpription:
  
  - pages - contains page objects classes representing particular pages of the website
  - tests - contains test classes with testcases
  - utilities - contains supporting files
