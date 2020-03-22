import React from 'react';
import "./stylesheets/styles-main.css";

export class Button extends React.Component {
    constructor(props) {
        super(props);
        this.switchLang = this.switchLang.bind(this);
    }

    switchLang(e) {

    }

    render() {
        return <div>
            <button type={"button"} onClick={this.switchLang} className={"langButton"}>DE</button>
        </div>;
    }
}
