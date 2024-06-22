/* eslint-disable react/prop-types */

const BadgeImage = ({ badgeNumber }) => {
  return (
    <img
      src={`badge_${badgeNumber}.png`}
      alt={`Badge_${badgeNumber}`}
      className="badge-image"
    />
  );
};

export default BadgeImage;
