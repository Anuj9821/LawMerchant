import React from "react";
import './search.css';
import lazyani from '../../animations/lazy404.json';
import Lottie from 'lottie-react';

function Search() {
    return (
        <div className="container rule-search">
            <div className="category text-center">
                <h3>Select the category of your product..</h3>
                <div className="row cat-btns">
                    <div className="col-6 col-sm-4 col-md-2 mb-2">
                        <button className="btn btn-outline-success w-100">Food</button>
                    </div>
                    <div className="col-6 col-sm-4 col-md-2 mb-2">
                        <button className="btn btn-outline-success w-100">Electronics</button>
                    </div>
                    <div className="col-6 col-sm-4 col-md-2 mb-2">
                        <button className="btn btn-outline-success w-100">Agriculture</button>
                    </div>
                    <div className="col-6 col-sm-4 col-md-2 mb-2">
                        <button className="btn btn-outline-success w-100">Hardware</button>
                    </div>
                    <div className="col-6 col-sm-4 col-md-2 mb-2">
                        <button className="btn btn-outline-success w-100">General</button>
                    </div>
                </div>
            </div>
            <div className="searchbar text-center mt-4">
                <form className="d-flex justify-content-center" role="search">
                    <input className="form-control me-2 w-50" type="search" placeholder="Search your product" aria-label="Search"/>
                    <button className="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
            <div className="rules mt-4 text-center">
                <Lottie animationData={lazyani} style={{ width: '50%'}} />
                <button className="btn btn-primary pro-btn mt-3">
                    Verify your product
                </button>
            </div>
        </div>
    );
}

export default Search;
