import React from "react";
import './ProfileCard.css';

const ProfileCard = ({ name,description,mail,photo }) => {
    return <div className="upc">
        <div className="gradiant"></div>
        <div className="profile-down">
            <img src={photo} alt="user photo"/>
            <div className="profile-title">{name}</div>
            <div className="profile-description">{description}</div>
            <div className="profile-button"><a href={`mailto:${mail}`} className="mailto">Entre em Contato</a></div>
        </div>
    </div>
};

export default ProfileCard;