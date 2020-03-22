import React from 'react';
import {requestTags} from "./requests";
import "./stylesheets/styles-main.css";

export class TagItem extends React.Component {
    render() {
        return <p className={"tag"}>{this.props.label}</p>
    }
}

export class TagList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {allTags: []};
        requestTags(this.handleTags, this);
        this.renderTagItems = this.renderTagItems.bind(this);
    }

    handleTags(responseData, thisC) {
        thisC.setState({allTags: responseData['tags']});
        thisC.forceUpdate();
    }

    renderTagItems() {
        let itemList = [];
        console.log('State: ');
        console.log(this.state.allTags);

        for(let i = 0; i < this.state.allTags.length; i++) {
            itemList.push(<TagItem label={this.state.allTags[i]} />);
        }
        console.log('Here2');
        console.log(itemList);

        return itemList;
    }

    render() {

        return <div>
            <div className={"flag-wrapper"} >
                <div className={"black"}></div>
                <div className={"red"}></div>
                <div className={"yellow"}></div>
            </div>
            <div className={"tag-container"} >
                {this.renderTagItems()}
            </div>
            <p className={"tag"}>Hier klicken um die Auswahl zu bestätigen</p>
        </div>;
    }
}