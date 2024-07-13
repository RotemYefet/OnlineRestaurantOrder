import React from 'react';

function Header() {
    return (
        <div id="header">
            <div>
                <ul className="navigation">
                    <li>
                        <a className="active" href="Home">Home</a>
                    </li>
                    <li>
                        <a href="About">About</a>
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

function Featured() {
    return (
        <div className="featured">
            <h2 className="featured-title">El Fuego Burgers</h2>
            <p className="featured-description">
                Come enjoy the best burgers in town, prepared on site with the freshest ingredients.
                With us you will find a wide variety of juicy hamburgers, fine toppings and unique sauces.
                Each dish is made with love and professionalism, to give you an unforgettable eating experience.
            </p>
            <a ><img src="images/HAMBURGERY.jpg" className="main-image" alt="Hamburger" /></a>

            <ul className="featured-images">
                <li>
                    <a href="Menu"><img src="images/hotdogs.jpg" className="featured-image" alt="Hot Dogs" /></a>
                </li>
                <li>
                    <a href="Menu"><img src="images/shakes.jpg" className="featured-image" alt="Shakes" /></a>
                </li>
                <li>
                    <a href="Menu"><img src="images/breakfast.jpg" className="featured-image" alt="Breakfast" /></a>
                </li>
            </ul>
            <button className="order-button" onClick={() => window.location.href='Menu'}>TO ORDER</button>
        </div>
    );
}

function Footer() {
    return (
        <div id="footer">
            <div>
                <ul>
                    <li className="first">
                        <h2>For delivery</h2>
                        <h3>Call 0-123-456-789</h3>
                    </li>
                    <li>
                        <ul className="navigation">
                       
                        </ul>
                    </li>
                    <li className="last">
                        <h2>Follow Us By Email</h2>
                        <form action="index.html">
                            <input type="text" name="subscribe" defaultValue="Enter Your Email Here..." />
                        </form>
                    </li>
                </ul>
            </div>
        </div>
    );
}

function App() {
    return (
        <div>
            {/* <Header /> */}
            <Featured />
            <Footer />
        </div>
    );
}

export default App;
