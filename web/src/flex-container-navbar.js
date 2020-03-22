import React from 'react';
import "./stylesheets/styles-main.css";

export const FlexContainerNavbar = (props) => {
    return <div>
        <div className={"flex-container-navbar"}>
            <a id={"home"} className={"active"} href={"/"}>Informationen</a>
            <a id={"recom"} className={"link"} href={"/recommendations"}>Unsere Vorschläge</a>
        </div>
    </div>;
};