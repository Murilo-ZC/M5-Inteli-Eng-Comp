import React from "react";
import './ProfileCard.css';

const ProfileCard = ({ name,description,mail,photo }) => {
    return <div class="profile-card">
    <div class="profile-card-image">
      <img src={photo} alt="user photo" class="profile-card-image-pic"/>
    </div>
    <div class="profile-card-data">
      <h2>{name}</h2>
      <span>{description}</span>
    </div>
    <div class="profile-card-buttons">
      <a href={`mailto:${mail}`} class="btn">Message</a>
      <a href="#" class="btn">Github</a>
    </div>
  </div>
};

export default ProfileCard;

