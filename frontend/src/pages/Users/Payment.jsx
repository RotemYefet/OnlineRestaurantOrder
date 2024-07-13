import React from 'react';

function ShoppingCart() {
  return (
      <div className="shopping-cart">
          {/* Add shopping cart items here */}
      </div>
  );
}

function CheckoutForm() {
    return (
        <div className="row">
            <div className="col-75">
                <div className="container">
                    <form action="/action_page.php">
                        <div className="row">
                            <div className="col-50">
                                <h3>Billing Address</h3>
                                <label htmlFor="fname"><i className="fa fa-user"></i> Full Name</label>
                                <input type="text" id="fname" name="firstname" placeholder="John M. Doe" />
                                <label htmlFor="email"><i className="fa fa-envelope"></i> Email</label>
                                <input type="text" id="email" name="email" placeholder="john@example.com" />
                                <label htmlFor="adr"><i className="fa fa-address-card-o"></i> Address</label>
                                <input type="text" id="adr" name="address" placeholder="542 W. 15th Street" />
                                <label htmlFor="city"><i className="fa fa-institution"></i> City</label>
                                <input type="text" id="city" name="city" placeholder="New York" />

                                <div className="row">
                                    <div className="col-50">
                                    </div>
                                    <div className="col-50">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <label>
                            <input type="checkbox" checked="checked" name="sameadr" /> Shipping address same as billing
                        </label>
                        <br />
                        <input type="submit" value="Order Confirmation" className="btn" />
                    </form>
                </div>
            </div>
        </div>
    );
}

function CheckoutPage() {
    return (
        <div>
            <ShoppingCart />
            <h2>Responsive Checkout Form</h2>
            <CheckoutForm />
        </div>
    );
}

function App() {
  return (
      <div>
          <CheckoutPage />
      </div>
  );
}

export default App;
