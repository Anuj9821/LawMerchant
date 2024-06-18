import React from "react";
import './abt-crd.css';

function Abt({ title, description }) {
    return (
        <div className="abtcrd">
            <div className="abthead">
                <h3>{title}</h3>
            </div>
            <div className="abtdes">
                <p>{description}</p>
            </div>
        </div>
    );
}

export default Abt;
