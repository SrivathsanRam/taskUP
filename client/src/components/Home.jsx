/* eslint-disable react/prop-types */
import Sidebar from "./homepage/Sidebar";
import Tag from "./homepage/Tag";
import ErrandsPage from "./homepage/Errandpage";
import 'bootstrap/dist/css/bootstrap.css';

const Home = ({ user }) => {
    //age,prev_matched,phone,name,nric,postal
    return (
      <div>
        {user ? (
          <div className="container-fluid">
          <div className="row">
            <div className="col-3">
              <Sidebar userName={user.name} score={JSON.parse(user.prev_matched).length/3} />
            </div>
            <div className="col-9">
              <h1>Select Your Task!</h1>
              <Tag></Tag>
              <ErrandsPage userPostcode={user.postal} userPrevMatched={user.prev_matched}/>
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
  