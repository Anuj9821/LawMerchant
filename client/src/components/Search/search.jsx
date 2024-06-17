import React from "react";
import './search.css'
import lazyani from '../../animations/lazy404.json';
import Lottie from 'lottie-react';

function Search(){
    return(
        <div className="rule-search">
            <div className="searchbar">
                <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>   

            <div className="rules">
            <Lottie  animationData={lazyani} style={{ width: '50%'}} />
            </div>
        </div>
    )
}

export default Search;