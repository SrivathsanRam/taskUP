import PropTypes from 'prop-types';
import BadgeImage from './Badge';

const Sidebar = ({ userName, score }) => {
  const renderBadges = () => {
    let badges = [];
    for (let i = 1; i <= score; i++) {
      badges.push(<BadgeImage key={i} badgeNumber={i} />);
    }
    return badges;
  };

  return (
    <div className="sidebar">
      <div className="user-info">
        <h3>{userName}</h3>
      </div>
      <div className="badges">
        {score > 0 && renderBadges()}
      </div>
    </div>
  );
};

Sidebar.propTypes = {
  userName: PropTypes.string.isRequired,
  score: PropTypes.number.isRequired,
};

export default Sidebar;
