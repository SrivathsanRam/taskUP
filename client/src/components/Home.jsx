/* eslint-disable react/prop-types */
const Home = ({ user }) => {
    return (
      <div>
        <h2>Home</h2>
        {user ? (
          <div>
            <p>User: {JSON.stringify(user)}</p>
            <p>Name: {user.name}</p>
            <p>Age: {user.age}</p>
          </div>
        ) : (
          <p>No user data</p>
        )}
      </div>
    );
  };
  
  export default Home;
  