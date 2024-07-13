import React, { useState } from 'react';

// Header component
function Header() {
  return (
    <div id="header">
      <div>
        <ul className="navigation">
          <li><a href="Home">Home</a></li>
          <li><a href="About">About</a></li>
          <li><a className="active" href="Menu">Menu</a></li>
          <li><a href="Payment">Payment</a></li>
        </ul>
      </div>
    </div>
  );
}

// MenuCategory component
const MenuCategory = ({ title, items, addToCart }) => {
  return (
    <div className="menu-category">
      <h2>{title}</h2>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <span className="price">{item.price}$</span>
            <button onClick={() => addToCart(item)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Cart component
const Cart = ({ cart }) => {
  const getTotalPrice = () => {
    return cart.reduce((total, item) => total + item.price, 0);
  };

  return (
    <div className="cart">
      <h2>Shopping Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <ul>
            {cart.map((item, index) => (
              <li key={index}>
                <span>{item.name}</span>
                <span className="cart-item-price">{item.price}$</span>
              </li>
            ))}
          </ul>
          <p>Total: <strong>{getTotalPrice()}$</strong></p>
          
          <button className="order-button" onClick={() => window.location.href='Payment'}>Payment</button>
          </>
      )}
    </div>
  );
};

// Menu sections
const BurgerMenu = ({ addToCart }) => {
  const burgers = [
    { name: "Burger Special- 150gr", description: "Classic hamburger with lettuce, tomato, pickle and purple onion.", price: 15 },
    { name: "Veggie Burger- 150gr", description: "Vegetarian burger with lettuce, tomato, pickle and purple onion.", price: 17 },
    { name: "Super Duper Burger- 250gr", description: "Double hamburger with lettuce, tomato, pickle and purple onion.", price: 15 },
    { name: "Kiddies Burger- 100gr", description: "Hamburger + fries / mashed potatoes + drink + ice cream scoop.", price: 10 }
  ];

  return <MenuCategory title="Burgers" items={burgers} addToCart={addToCart} />;
};

const BreakfastMenu = ({ addToCart }) => {
  const breakfastItems = [
    { name: "Strawberry Waffle", description: "Hot waffle with fresh strawberries.", price: 10 },
    { name: "Shakshuka", description: "Eggs cooked in tomato sauce with spices and vegetables.", price: 8 },
    { name: "French Toast With Eggs", description: "Brioche bread dipped in eggs, milk and spices, fried golden.", price: 13 },
    { name: "Icecream and Pancakes", description: "Pancakes with ice cream.", price: 14 }
  ];

  return <MenuCategory title="Breakfast" items={breakfastItems} addToCart={addToCart} />;
};

const ShakesMenu = ({ addToCart }) => {
  const shakes = [
    { name: "Chocolate Vanilla", description: "Classic chocolate and vanilla milk drink.", price: 10 },
    { name: "Strawberry Smoothie", description: "Fruit smoothie with strawberries, milk, yogurt and cinnamon.", price: 7 },
    { name: "Mango Banana Medley", description: "Tropical smoothie with mango and banana.", price: 13 },
    { name: "Dark Chocolate Supreme", description: "Dessert made from dark chocolate.", price: 14 }
  ];

  return <MenuCategory title="Shakes" items={shakes} addToCart={addToCart} />;
};

const HotdogMenu = ({ addToCart }) => {
  const hotdogs = [
    { name: "Hotdog Special", description: "Classic sausage in a bun with ketchup, mustard and pickles.", price: 5 },
    { name: "Bacon Cheesedog", description: "Hot dog with bacon and melted cheese.", price: 10 },
    { name: "King Size Hotdog", description: "Large hot dog with all toppings.", price: 8 },
    { name: "Kiddies Hotdog", description: "Small sausage in a bun with ketchup and mustard.", price: 3 }
  ];

  return <MenuCategory title="Hotdogs" items={hotdogs} addToCart={addToCart} />;
};

// App component
function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (item) => {
    if (!cart.find(cartItem => cartItem.name === item.name)) {
      setCart([...cart, item]);
    }
  };

  return (
    <div className="app-container">
      {/* <Header /> */}
      <div className="content">
        <BurgerMenu addToCart={addToCart} />
        <BreakfastMenu addToCart={addToCart} />
        <ShakesMenu addToCart={addToCart} />
        <HotdogMenu addToCart={addToCart} />
      </div>
      <Cart cart={cart} />
    </div>
  );
}

export default App;
