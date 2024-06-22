/* eslint-disable react/prop-types */
import badge_1 from '../../public/badge_1.png'
import badge_2 from '../../public/badge_2.png'
import badge_3 from '../../public/badge_3.png'
//import badge_4 from '../../public/badge_4.png'
//import badge_5 from '../../public/badge_5.png'

const BadgeImage = ({ badgeNumber }) => {
  const lst = [badge_1,badge_2,badge_3];
  return (
    <img
      src={lst[badgeNumber-1]}
      alt={`Badge_${badgeNumber}`}
      className="badge-image"
      width={75}
    />
  );
};

export default BadgeImage;
