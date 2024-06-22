/* eslint-disable react/prop-types */

import { useState, useEffect } from 'react';
import Errand from './Errand'; // Ensure the Errand component is in the same folder or adjust the path
import "./Errandpage.css"


const ErrandsPage = ({ tags, userPostcode, userPrevMatched }) => {
  const [errands, setErrands] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchErrands = async () => {
      try {
        const response = await fetch(`/api/errands?user_postcode=${userPostcode}&user_prev_matched=${userPrevMatched}`);
        if (!response.ok) {
          throw new Error('Failed to fetch errands');
        }
        const data = await response.json();
        setErrands(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching errands:', error);
        setError(error);
        setLoading(false);
      }
    };

    fetchErrands();
  }, [userPostcode, userPrevMatched]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }
  const filteredErrands = errands.filter(errand => tags.includes(errand.tag));
  return (
    <div className="errand-list scrollable-container">
      {filteredErrands.map((errand) => (
        <Errand
          key={errand.id}
          proximity={errand.proximity}
          postcode={errand.postcode}
          duration={errand.duration}
          description={errand.description}
          tag={errand.tag}
        />
      ))}
    </div>
  );
};

export default ErrandsPage;
