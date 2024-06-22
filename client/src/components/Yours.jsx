/* eslint-disable react/prop-types */
import { useState } from "react";

const YourTasks = ({
  phoneNumber,
  proximity,
  fullName,
}) => {
  // State for tip amount
  const [tipAmount, setTipAmount] = useState(0);
  const [imageUrl, setImageUrl] = useState('');
  // Function to handle tip submission
  const handleSubmitTip = () => {
    if (parseFloat(tipAmount) > 0) {
      const url = `https://sgqrcode.com/paynow?mobile=${phoneNumber}&uen=&editable=1&amount=${tipAmount}&expiry=2024%2F06%2F25%2008%3A00&ref_id=reference&company=`;
      setImageUrl(url);
    }
    console.log("Submitting tip:", tipAmount);

  };

  
  
  const getInitials = (name) => {
    return name
      .split(" ")
      .map((word) => word.charAt(0))
      .join("")
      .toUpperCase();
  };

  return (
    <div className="your-tasks card">
      <div className="card-body">
        <div className="initials text-center mb-3"><strong>{getInitials(fullName)} is on the way!</strong></div>
        <div className="proximity mb-3">
          <strong>Proximity:</strong> {proximity} mins
        </div>
        <div className="contact mb-3">
          <strong>Phone:</strong>{" "}
          <a href={`tel:${phoneNumber}`}>{phoneNumber}</a>
        </div>
        <div className="tip-section">
          <label htmlFor="tipAmount">Enter tip amount (optional):</label>
          <div className="input-group mb-3">
            <input
              type="number"
              className="form-control"
              id="tipAmount"
              value={tipAmount}
              onChange={(e) => setTipAmount(e.target.value)}
            />
            <div className="input-group-append">
              <button
                className="btn btn-outline-primary"
                onClick={handleSubmitTip}
              >
                Submit Tip
              </button>
            </div>
          </div>
        </div>
      </div>
      <div>
        {imageUrl && (
          <div className="image-section mt-3 text-center">
            <img width={200} src={imageUrl} alt="QR Code" className="img-fluid" />
          </div>
        )}
      </div>
    </div>
  );
};

export default YourTasks;
