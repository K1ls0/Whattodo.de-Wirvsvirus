import React from 'react';
import "./stylesheets/styles-main.css";
import {getText} from "./language";

export const Header = (props) => {
    return <div>
        <div className={"flex-container-logo"}>
            <img src={""} alt={"logo"} />
            <p className={"logo-text"}>ERROR</p>
        </div>
        <div className={"flex-container-navbar"}>
            <a id={"home"} className={"active"} href={"/"}>{getText("t_info")}</a>
            <a id={"recom"} className={"link"} href={"/recommendations"}>{getText("t_recom")}</a>
        </div>
    </div>
};
