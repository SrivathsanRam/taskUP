/* eslint-disable react/prop-types */

const BadgeImage = ({ badgeNumber }) => {
  return (
    <img
      src={`/images/badges/badge_${badgeNumber}.png`}
      alt={`Badge ${badgeNumber}`}
      className="badge-image"
    />
  );
};

export default BadgeImage;
