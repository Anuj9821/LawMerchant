import React from 'react';
import Lottie from 'lottie-react';
import heroani from '../../animations/heroani.json';
import './hero.css';

function Hero() {
    return (
        <div className="container-fluid Hero">
            <div className="row align-items-center">
                <div className="col-lg-6 col-md-12 H-left">
                    <h1>
                        A agency<br />
                        which navigates 
                        the Government laws for your product.
                    </h1>
                    <h4>
                        Law-Merchant allow you to find out the applicable rules to you product in a proper manner.
                    </h4>
                    <span>
                        Now with our services there's no need to fetch for the <b>rules</b> and <b>regulation</b> on the government repositories which is time consuming process. You are able to find all the rules and regulations for your product on this platform
                    </span>
                </div>
                <div className="col-lg-6 col-md-12 H-right">
                <Lottie animationData={heroani} />
                </div>
            </div>
        </div>
    );
}

export default Hero;
