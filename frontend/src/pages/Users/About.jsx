import React from 'react';

function Header() {
    return (
        <div id="header">
            <div>
                <ul className="navigation">
                    <li>
                        <a href="Home">Home</a>
                    </li>
                    <li>
                        <a className="active" href="About">About</a>
                    </li>
                    <li>
                        <a href="Menu">Menu</a>
                    </li>
                    <li>
                        <a href="Payment">Payment</a>
                    </li>
                  
                </ul>
            </div>
        </div>
    );
}


const About = () => {
  return (
    <div className="about-page">
      <h2 className="about-title" style={{ direction: 'ltr' , fontFamily: 'sans-serif', fontSize: 40}}>
      El Fuego Burgers  </h2>
      <div className="about-content" style={{ direction: 'ltr' , fontFamily: 'sans-serif', fontSize: 20}}>
        <p>
        Welcome to El Fuego Burgers! We are a small, family hamburger restaurant that specializes in making juicy and delicious hamburgers from fresh, high-quality ingredients. We are proud to use fresh ground meat on site, soft and airy buns, and a variety of fresh and spicy toppings.        </p>
        <h2 className="about-subtitle"> What makes us different?</h2>
        <ul className="about-list">
          <li>Juicy burgers: we use fresh ground meat on site, without preservatives or artificial colors.</li>
          <li>Soft Buns: We bake our hamburger buns on site, making them soft, airy and extra delicious.</li>
          <li>Variety of toppings: we offer a wide variety of fresh and spicy toppings, such as roasted vegetables, special sauces, quality cheeses and more.</li>
          <li>Pleasant atmosphere: we believe that the eating experience is just as important as the food itself.</li>
          <li>Courteous service: our staff is courteous and professional and will do everything to guarantee you a pleasant and fast service experience.</li>
        </ul>
        <h2 className="about-subtitle">In addition, we offer:</h2>
        <ul className="about-list">
          <li> Children's meals: we offer a variety of delicious and healthy children's meals.</li>
          <li>Vegan options: we offer a variety of vegan burgers made from quality and tasty ingredients.</li>
          <li>Deliveries: We offer a fast and convenient delivery service to any area.</li>
          <li>Event invitations: We accept invitations for private and business events.</li>
        </ul>
        <div className="about-contact">
          <h2>We will be happy to see you with us!</h2>
          <p>
            <strong>Address:</strong> [Rishon Lezion, Elie Wiesel]
          </p>
          <p>
            <strong>Phone:</strong> [0-123-456-789]
          </p>
        </div>
      </div>
    </div>
  );
};


function App() {
    return (
        <div>
            {/* <Header /> */}
            <About />
        </div>
    );
}

export default App;

