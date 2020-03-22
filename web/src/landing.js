import React from 'react';
import "./stylesheets/styles-main.css";

export const Landing = (props) => {
    return <div>
        <div className={"landing-wrapper"} >
            <div className={"landing-container"} >
                <div className={"landing-text"} >
                    <p>Nicht wissen was tun?</p>
                    <p>Der richtige Zeitvertreib wartet genau hier!</p>
                </div>
                <div className={"landing-introduction"} >
                    <img src={"static/img/WirVsVirus.png"} alt={"WirVsVirus-Header"} />
                    <p>In Zeiten von "Social Distancing" und dem ständigen Zuhausebleiben kann es schon mal schwer fallen sich zu beschäftigen. Im Zuge des Hackathons #WirVsVirus der
                        Bundesregierung vom 20.03.2020 haben wir dieses Projekt entwickelt. Wir wollen es einfacher machen, interessante Aufgaben zu finden um den Krieg gegen die ewige
                        Langeweile ein für alle Mal zu gewinnen! Ob nun für 20 Minuten, eine Stunde oder auch noch länger, hier findet Ihr die passende Idee zu euren Interessen: Spiele,
                        Musik, Hausarbeiten und noch viel mehr.</p>
                </div>
            </div>
        </div>
    </div>;
};
