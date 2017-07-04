import React from 'react';

import firebase from '../firebase';

import QuickView from './QuickView';


class App extends React.Component {
  componentWillUnmount() {
      firebase.removeBinding(this.ref);
  }
  render() {
    return (
      <div className="Dashboard">
          <QuickView />
      </div>
    );
  }
}

export default App;
