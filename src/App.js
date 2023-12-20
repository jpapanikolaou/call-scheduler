import React, { useState } from 'react';
import 'antd/dist/reset.css';
import PhysicianForm from './components/PhysicianForm';
import PhysicianList from './components/PhysicianList';


const App = () => {
  const [physicians, setPhysicians] = useState([]);

  const addPhysician = (physician) => {
    setPhysicians([...physicians, physician]);
  };

  return (
    <div>
      <PhysicianForm onAddPhysician={addPhysician} />
      <PhysicianList physicians={physicians} />
    </div>
  );
};

export default App;
