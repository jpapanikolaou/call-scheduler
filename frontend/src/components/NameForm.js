import React, { useState } from 'react';
import { Form, Input, Button, List } from 'antd';

const NameForm = () => {
  const [names, setNames] = useState([]);
  const [form] = Form.useForm();

  const onFinish = (values) => {
    const { firstName, lastName } = values;
    const newNames = [...names, { firstName, lastName }];
    setNames(newNames);

    fetch('http://localhost:5001/submit-name', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newNames),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      } else if (!response.headers.get('content-type')?.includes('application/json')) {
        throw new Error(`Expected JSON, got ${response.headers.get('content-type')}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });

    form.resetFields();
  };

  return (
    <div>
      <Form form={form} onFinish={onFinish} layout="inline">
        <Form.Item
          name="firstName"
          rules={[{ required: true, message: 'Please input your first name!' }]}
        >
          <Input placeholder="First Name" />
        </Form.Item>
        <Form.Item
          name="lastName"
          rules={[{ required: true, message: 'Please input your last name!' }]}
        >
          <Input placeholder="Last Name" />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Add Name
          </Button>
        </Form.Item>
      </Form>

      <List
        size="small"
        header={<div>Names List</div>}
        bordered
        dataSource={names}
        renderItem={item => (
          <List.Item>
            {item.firstName} {item.lastName}
          </List.Item>
        )}
      />
    </div>
  );
};

export default NameForm;
