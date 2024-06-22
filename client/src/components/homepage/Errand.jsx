import PropTypes from 'prop-types';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const Errand = ({ proximity, duration, description, tag }) => {
  return (
    <Card>
      <Card.Body>
        <Card.Title>{description}</Card.Title>
        <Card.Text>
          <strong>Proximity:</strong> {proximity} mins<br />
          <strong>Duration:</strong> {duration} mins<br />
          <strong>Tag:</strong> {tag}
        </Card.Text>
        <Button variant="primary">Accept</Button>
      </Card.Body>
    </Card>
  );
};

Errand.propTypes = {
  proximity: PropTypes.number.isRequired,
  duration: PropTypes.number.isRequired,
  description: PropTypes.string.isRequired,
  tag: PropTypes.string.isRequired,
};

export default Errand;
