import React from 'react';
import ReactDOM from 'react-dom';
import "./stylesheets/styles-main.css";
import {FlexContainerLogo} from "./flex-container-logo";
import {Landing} from "./landing";
import {Button} from "./button";
import {TagList} from "./tag-list";

const Source = (props) => {
    return <div>
        <div className={"header"}>
            <FlexContainerLogo />
            <Button />
        </div>
        <div className={"content"}>
            <Landing />
            <div className={"tag-wrapper"} >
                <TagList />
            </div>
        </div>
    </div>
};

ReactDOM.render(<Source />, document.getElementById("root"));