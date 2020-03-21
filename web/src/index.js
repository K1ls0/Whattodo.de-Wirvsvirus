import React from 'react';
import ReactDOM from 'react-dom';
import "./stylesheets/styles-main.css";
import {Header} from "./header.js";
import {Button} from "./button";
import {LangComponent} from "./language";

class Source extends LangComponent {
    constructor(props) {
        super(props);
        this.state = {lang: "DE"};
    }

    render() {
        return <div>
            <Button className={"button"} lang={this.state.lang} ></Button>
            <Header className={"header"} lang={this.state.lang} ></Header>
        </div>;
    }
}

ReactDOM.render(<Source lang={"ENG"} />, document.getElementById("root"));