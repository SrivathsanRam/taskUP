/* eslint-disable react/prop-types */
import Sidebar from "./homepage/Sidebar";
import Tag from "./homepage/Tag";
import ErrandsPage from "./homepage/Errandpage";
import 'bootstrap/dist/css/bootstrap.css';
import "./Home.css"
import { useState } from "react";
import YourTasks from "./Yours";

const Home = ({ user }) => {
    //age,prev_matched,phone,name,nric,postal
    const [selected,setSelected] = useState(["gardening", "cleaning", "pick-up", "share food"]);


    return (
      <div>
        {user ? (
          <div className="container-fluid">
          <div className="row">
            <div className="col-3">
              <Sidebar userName={user.name} score={JSON.parse(user.prev_matched).length/3} />
            </div>
            <div className="col-5">
              <h1 className="text-center">Select Your Task!</h1>
              <Tag selected={selected} setSelected={setSelected}/>
              <ErrandsPage tags={selected} userPostcode={user.postal} userPrevMatched={user.prev_matched}/>
            </div>
            <div className="col-4">
              <h1 className="text-center">Your Tasks</h1>
              <YourTasks phoneNumber={82923370} fullName={"Shankar Balaji"} proximity={5}/>
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
  