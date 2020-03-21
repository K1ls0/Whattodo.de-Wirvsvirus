import React from 'react';
import ReactDOM from 'react-dom';
import "./stylesheets/styles-main.css";
import {Header} from "./header.js";
import {Button} from "./button";

const Source = (props) => {
    return <div>
        <Button className={"button"} >SPRACHE</Button>
        <Header className={"header"} ></Header>
    </div>;
};

ReactDOM.render(<Source lang={"ENG"} />, document.getElementById("root"));