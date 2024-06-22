/* eslint-disable react/prop-types */

import { useState, useEffect } from 'react';
import Errand from './Errand'; // Ensure the Errand component is in the same folder or adjust the path

const ErrandsPage = ({ userPostcode, userPrevMatched }) => {
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
  }, [userPostcode]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className="errand-list">
      {errands.map((errand) => (
        <Errand
          key={errand.id}
          proximity={errand.proximity}
          duration={errand.duration}
          description={errand.description}
          tag={errand.tag}
        />
      ))}
    </div>
  );
};

export default ErrandsPage;
