import React, { useEffect, useState } from 'react';
import './App.css';
import { withAuthenticator } from 'aws-amplify-react'
import Amplify, { Auth } from 'aws-amplify';
import '@aws-amplify/ui/dist/style.css';
import aws_exports from './aws-exports'
import ReactJson from 'react-json-view'

Amplify.configure(aws_exports);

function App() {
  const [me, setMe] = useState(null)

  const callme = async () => {
    const res = await fetch("http://mylxc/api/one/v1/me/", {headers: {
      Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}`
    }})
    setMe(await res.json())
  }

  return (
    <div className="App">
      <button onClick={callme}>Call /me</button>
      {me && <ReactJson src={me!} />}
    </div>
  );
}

export default withAuthenticator(App, true);