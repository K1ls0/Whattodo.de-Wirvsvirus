import React from 'react';

let lang = "ENG";

let dEn = {
    "t_info": "INFORMATION",
    "t_recom": "OUR RECOMMENDATIONS"
};

let dDe = {
    "t_info": "INFORMATIONEN",
    "t_recom": "UNSERE EMPFEHLUNGEN"
};

export const setLang = (l) => {
    lang = l;
};

export const toggleLangStatic = () => {
    if (lang === "ENG") setLang("DE");
    else setLang("ENG");
};

export const getText = (key) => {
    return lang === "ENG" ? dEn[key] : dDe[key];
};

export class LangComponent extends React.Component {
    toggleLang() {
        toggleLangStatic();
        this.forceUpdate();
    }

}