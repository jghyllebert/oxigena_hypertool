import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  withRouter
} from 'react-router-dom';
import App from './App';
import Login from './Login';
import registerServiceWorker from './registerServiceWorker';


const Routing = () => (
  <Router>
    <Route path="/login" component={Login} />
    <PrivateRoute path="/" component={App} />
  </Router>
)



ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
