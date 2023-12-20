import 'antd/dist/reset.css'; // Import Ant Design styles
import React from 'react';
/* Ant design imports */
import { List, Card } from 'antd';

const PhysicianList = ({ physicians }) => {
    return (
      <div>
        <h2>Finished</h2>
        <List
          grid={{ gutter: 16, column: 1 }}
          dataSource={physicians}
          renderItem={physician => (
            <List.Item>
              <Card title={physician.name}>
                <p><strong>Availability:</strong> {physician.availability}</p>
              </Card>
            </List.Item>
          )}
        />
      </div>
    );
  };
  
  export default PhysicianList;
