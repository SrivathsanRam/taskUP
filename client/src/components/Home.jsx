/* eslint-disable react/prop-types */
import Sidebar from "./homepage/Sidebar";

const Home = ({ user }) => {
    //age,,1500,name,nric,postal
    return (
      <div>
        <h2>Home</h2>
        {user ? (
          <div className="container-fluid">
          <div className="row">
            <div className="col-3">
              <Sidebar userName={user.name} score={user.prev_matched} />
            </div>
            <div className="col-9">
              <h1>Main Content</h1>
            </div>
          </div>
        </div>
        ) : (
          <p>No user data</p>
        )}
      </div>
    );
  };
  
  export default Home;
  