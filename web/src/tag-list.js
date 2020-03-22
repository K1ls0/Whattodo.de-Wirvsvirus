import React from 'react';
import "./stylesheets/styles-main.css";

export const TagList = (props) => {
    return <div>
        <div className={"flag-wrapper"} >
            <div className={"black"}></div>
            <div className={"red"}></div>
            <div className={"yellow"}></div>
        </div>
        <p>Hallo, ich bin ein Tag</p>
    </div>;
};
