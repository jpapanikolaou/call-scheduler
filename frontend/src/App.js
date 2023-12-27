import React from 'react';
import 'antd/dist/reset.css'; // Import Ant Design styles
import NameForm from './components/NameForm'; // Import the NameForm component

function App() {
  return (
    <div className="App">
      <h1>Enter names here</h1>
      <NameForm />
    </div>
  );
}

export default App;
