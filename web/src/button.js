import React from 'react';
import "./stylesheets/styles-main.css";
import {LangComponent} from "./language";

export class Button extends LangComponent {
    constructor(props) {
        super(props);
        this.state = {
            lang: "ENG"
        };
        this.switchLang = this.switchLang.bind(this);
    }

    switchLang(e) {
        this.toggleLang();
    }

    render() {
        return <div>
            <button onClick={this.switchLang} className={"langButton"}>{this.state.lang}</button>
        </div>;
    }
}
