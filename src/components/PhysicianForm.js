import React, { useState } from 'react';

const PhysicianForm = ({ onAddPhysician }) => {
  const [name, setName] = useState('');
  const [availability, setAvailability] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddPhysician({ name, availability });
    setName('');
    setAvailability('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
        placeholder="Physician Name" 
        required 
      />
      <input 
        type="text" 
        value={availability} 
        onChange={(e) => setAvailability(e.target.value)} 
        placeholder="Availability" 
        required 
      />
      <button type="submit">Add Physician</button>
    </form>
  );
};

export default PhysicianForm;