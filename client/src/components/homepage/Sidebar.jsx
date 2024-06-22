import PropTypes from 'prop-types';
import BadgeImage from './Badge';
import './Sidebar.css';

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
      <div className="mt-5">
        <h3>Welcome {userName}!</h3>
      </div>
      <div className="mt-5">
        {score > 0 && renderBadges()}
      </div>
      <div className="mt-5">
        You are in the top {score*3+1}% of users this month!
      </div>
    </div>
  );
};

Sidebar.propTypes = {
  userName: PropTypes.string.isRequired,
  score: PropTypes.number.isRequired,
};

export default Sidebar;
